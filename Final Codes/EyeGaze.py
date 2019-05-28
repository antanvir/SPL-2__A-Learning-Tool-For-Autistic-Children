from PyQt5.QtWidgets import QPushButton, QSizePolicy, QSlider, QStyle, QVBoxLayout, QWidget
from PyQt5.QtWidgets import QApplication, QFileDialog, QHBoxLayout, QLabel
from PyQt5.QtWidgets import QMainWindow, QWidget, QPushButton, QAction
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtCore import QDir, Qt, QUrl
from imutils.video import VideoStream
from keras.models import load_model
from tkinter import *
import mysql.connector
from imutils import face_utils
from PyQt5.QtGui import QIcon
from PyQt5.QtGui import QIcon
from time import sleep
import numpy as np
import datetime
import argparse
import imutils
import tkinter
import math
import time
import dlib
import cv2
import sys


class GazeEstimator():

    def __init__(self):
        self.detector = dlib.get_frontal_face_detector()
        self.predictor = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')
        
    
    def face_orientation(self, frame, landmarks):
        size = frame.shape

        image_points = np.array([
            (landmarks[33][0], landmarks[33][1]),   # Nose tip
            (landmarks[8][0], landmarks[8][1]),     # Chin
            (landmarks[36][0], landmarks[36][1]),   # Left eye left corner
            (landmarks[45][0], landmarks[45][1]),   # Right eye right corne
            (landmarks[48][0], landmarks[48][1]),   # Left Mouth corner
            (landmarks[54][0], landmarks[54][1])    # Right mouth corner
        ], dtype="double")

        model_points = np.array([
            (0.0, 0.0, 0.0),                        # Nose tip
            (0.0, -330.0, -65.0),                   # Chin
            (-165.0, 170.0, -135.0),                # Left eye left corner
            (165.0, 170.0, -135.0),                 # Right eye right corne
            (-150.0, -150.0, -125.0),               # Left Mouth corner
            (150.0, -150.0, -125.0)                 # Right mouth corner
        ])

        center = (size[1] / 2, size[0] / 2)
        focal_length = center[0] / np.tan(60 / 2 * np.pi / 180)
        camera_matrix = np.array([
             [focal_length, 0, center[0]],
             [0, focal_length, center[1]],
             [0, 0, 1]
        ], dtype="double")

        dist_coeffs = np.zeros((4, 1))
        (success, rotation_vector, translation_vector) = cv2.solvePnP(model_points, image_points, camera_matrix, dist_coeffs, flags=cv2.SOLVEPNP_ITERATIVE)

        axis = np.float32([[500, 0, 0], [0, 500, 0], [0, 0, 500]])
        imgpts, jac = cv2.projectPoints(axis, rotation_vector, translation_vector, camera_matrix, dist_coeffs)
        modelpts, jac2 = cv2.projectPoints(model_points, rotation_vector, translation_vector, camera_matrix, dist_coeffs)
        rvec_matrix = cv2.Rodrigues(rotation_vector)[0]

        proj_matrix = np.hstack((rvec_matrix, translation_vector))
        eulerAngles = cv2.decomposeProjectionMatrix(proj_matrix)[6]

        pitch, yaw, roll = [math.radians(_) for _ in eulerAngles]
        pitch = math.degrees(math.asin(math.sin(pitch)))
        roll = -math.degrees(math.asin(math.sin(roll)))
        yaw = math.degrees(math.asin(math.sin(yaw)))

        return imgpts, modelpts, (str(int(roll)), str(int(pitch)), str(int(yaw))), (landmarks[33][0], landmarks[33][1])
    
    
    def detectFace(self, gray_frame):
        rects = self.detector(gray_frame)
        rect = None
        
        for rect in rects:
            return rect
        
        return rect
        
        
    def create_two_eye_frames(self, frame, landmarks):
        max_left_x = max(landmarks[36][0], landmarks[37][0], landmarks[38][0], landmarks[39][0], landmarks[40][0], landmarks[41][0])
        min_left_x = min(landmarks[36][0], landmarks[37][0], landmarks[38][0], landmarks[39][0], landmarks[40][0], landmarks[41][0])
        max_left_y = max(landmarks[36][1], landmarks[37][1], landmarks[38][1], landmarks[39][1], landmarks[40][1], landmarks[41][1])
        min_left_y = min(landmarks[36][1], landmarks[37][1], landmarks[38][1], landmarks[39][1], landmarks[40][1], landmarks[41][1])
        
        max_right_x = max(landmarks[42][0], landmarks[43][0], landmarks[44][0], landmarks[45][0], landmarks[46][0], landmarks[47][0])
        min_right_x = min(landmarks[42][0], landmarks[43][0], landmarks[44][0], landmarks[45][0], landmarks[46][0], landmarks[47][0])
        max_right_y = max(landmarks[42][1], landmarks[43][1], landmarks[44][1], landmarks[45][1], landmarks[46][1], landmarks[47][1])
        min_right_y = min(landmarks[42][1], landmarks[43][1], landmarks[44][1], landmarks[45][1], landmarks[46][1], landmarks[47][1])
        
        crop_left_eye = frame[min_left_y:max_left_y, min_left_x:max_left_x]
        crop_right_eye = frame[min_right_y:max_right_y, min_right_x:max_right_x]
        dim = (200, 80)
        resized_left_eye = cv2.resize(crop_left_eye, dim, interpolation = cv2.INTER_AREA)
        resized_right_eye = cv2.resize(crop_right_eye, dim, interpolation = cv2.INTER_AREA)
        
        return resized_left_eye, resized_right_eye
    
    
    def detectVisualPreference(self, left_eye_center, right_eye_center, head_pose_rotation, bias_const):
        eye_location = left_eye_center[0] + right_eye_center[0] - bias_const
        rotation = 5
        
        if head_pose_rotation < -rotation or head_pose_rotation > rotation:
            eye_location = eye_location - (2*head_pose_rotation)
            
        eye_location = 0 - eye_location

        return eye_location
    
    
    def gazeDetection(self, gray_frame, rect, frame, bias_const):
        shape = self.predictor(gray_frame, rect)
        shape = face_utils.shape_to_np(shape)
        imgpts, modelpts, rotate_degree, nose = self.face_orientation(frame, shape)
        
        left_eye_frame, right_eye_frame = self.create_two_eye_frames(frame, shape)
        left_eye_center = self.pupil_detection(left_eye_frame)
        right_eye_center = self.pupil_detection(right_eye_frame)
        eye_location = self.detectVisualPreference(left_eye_center, right_eye_center, int(rotate_degree[2]), bias_const)
        
        return eye_location
        
        
    def find_largest_contour(self, contours):
        pupil = (100, 40)
        distanceX = []
        distanceY = []

        if len(contours) >= 1:
            max_area = 0
            m_a_index = 0
            current_index = 0

            for cnt in contours:
                area = cv2.contourArea(cnt)
                center = cv2.moments(cnt)
                if center['m00'] <= 0:
                    continue

                cx, cy = int(center['m10'] / center['m00']), int(center['m01'] / center['m00'])

                distanceX.append(cx)
                distanceY.append(cy)

                if area > max_area:
                    max_area = area
                    m_a_index = current_index

                current_index = current_index + 1

            if len(distanceX) == 0:
                return pupil

            pupil = (distanceX[m_a_index], distanceY[m_a_index])

        return pupil
        
    def pupil_detection(self, eye_frame):
        pupil = None
        actual_eye = eye_frame.copy()
    
        eye_frame = cv2.cvtColor(eye_frame, cv2.COLOR_RGB2GRAY)
        eye_frame = cv2.equalizeHist(eye_frame)
        eye_frame = cv2.cvtColor(eye_frame, cv2.COLOR_GRAY2RGB)
        eye_frame = cv2.cvtColor(eye_frame, cv2.COLOR_RGB2HSV)

        hue, saturation, value = cv2.split(eye_frame)
        value = cv2.equalizeHist(value)
        val = np.array(value)
        val = np.sort(val, axis=None)
        threshold_pt = int(val.size*0.25)
        threshold = val[threshold_pt]

        lower_black = np.array([0, 0, 0])
        upper_black = np.array([255, 255, threshold])

        eye_frame = cv2.inRange(eye_frame, lower_black, upper_black)

        kernel = np.ones((2, 2), np.uint8)
        eye_frame = cv2.erode(eye_frame, kernel, iterations=2)
        eye_frame = cv2.dilate(eye_frame, kernel, iterations=2)

        _, contours, hierarchy = cv2.findContours(eye_frame, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
        pupil = self.find_largest_contour(contours)
        cv2.circle(actual_eye, tuple(pupil), 2, (0, 0, 255), -1)

        return pupil
                        

class EmotionPredictor():

    def __init__(self):
        self.model = load_model('fer-2013.hdf5')
    
    
    def getExpression(self, face_frame):
        face_frame = cv2.resize(face_frame, (48, 48))
        face_frame = face_frame.astype('float32') / 255
        face_frame = np.asarray(face_frame)
        face_frame = face_frame.reshape(1, 1, face_frame.shape[0], face_frame.shape[1])
        facial_expression = self.model.predict(face_frame)
        
        return facial_expression
    

class VideoWindow(QMainWindow):

    def preliminaryHistogramEqualization(self, frame):
        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2HSV)
        h, s, v = cv2.split(frame)
        v = cv2.equalizeHist(v)
        frame = cv2.merge([h, s, v])
        frame = cv2.cvtColor(frame, cv2.COLOR_HSV2RGB)
        
        return frame
        
    
    def find_parameters(self):
        try:
            dataFile = open('gaze.conf', 'r')
            lines = dataFile.read().split('\n')[:-1]

            for i in range(len(lines)):
                lines[i] = lines[i].split(', ')
        
            line = lines[0]
            eye_width_sum = int(line[0])
            width_range = int(line[1])
        
            return eye_width_sum, width_range
        
        except:
            return self.bias_const, self.width_bias
            
            
    
    def fileNameFromTime(self):
        date_time = datetime.datetime.now()
        date_time = str(date_time)
        date_time = date_time.replace(":", "-")
        date_time = date_time.replace(" ", "-")
        date_time = date_time.replace(".", "")
        date_time = "Output/" + date_time + ".txt"
        
        return date_time
        
        
    def gaze_position_estimation(self, eye_location, width, width_range):
        bias = width_range
        gaze_result = (eye_location + bias) * (width / (2*bias))
        
        return gaze_result
        
    
    def setDimention(self):
        root = tkinter.Tk()
        width = root.winfo_screenwidth()
        height = root.winfo_screenheight()
        dim = (width, height)
        
        return dim  
    
    
 
        
    def openFile(self):
        object_id = 1
        #fileName = "video.mp4"
        mydb = mysql.connector.connect(
                host = 'localhost',
                user = "root",
                #passwd = "ant904",
                database = "spl"
                #auth_plugin='mysql_native_password'
                )
        myCursor = mydb.cursor(buffered=True)
        sql = "SELECT video, realExpression FROM expressiveContent where conteent_id=%s"
        val=(object_id,)
        myCursor.execute(sql,val)
        row=myCursor.fetchone()

        fileName = row[0]
        realExpression = row[1]

        bias_const, width_range = self.find_parameters()
        
        video_file_flag = (fileName != '') & fileName.endswith(".mp4")
        
        if video_file_flag == False:
            self.showMessage("Choose a valid video(.mp4) file.")
            return 
        
        cap = cv2.VideoCapture(fileName)
        capWebCam = cv2.VideoCapture(0)
            
        if (capWebCam.isOpened() != True):
            self.showWebcamError()
            return 
            
        cv2.namedWindow(fileName)
        cv2.moveWindow(fileName, 0, 0)
        tots = cap.get(cv2.CAP_PROP_POS_FRAMES)
            
        status = 'play'
        emotionModel = EmotionPredictor()
        gazeModel = GazeEstimator()
        
        preference = 'center'
        show_prefer = np.array([500, 500])
        visual_prefer_x = np.array([0, 0, 0, 0, 0])
        target = ['angry', 'disgust', 'fear', 'happy', 'sad', 'surprise', 'neutral']

        facial_expression = np.array([0.14, 0.14, 0.14, 0.14, 0.14, 0.14, 0.16])
        w_file_name = self.fileNameFromTime()
        fileWriter = open(w_file_name, "w")
            
        frame_index = -1
        face_identified = 0
        result = 'neutral'
        dim = self.setDimention()
        scrn_width = dim[0]
        show_prefer[1] = dim[1]//2

        outputFileName = "EyeGazeOutput/Object" + str(object_id) + "_data.txt"
        file = open(outputFileName, "a+")

        start_time = datetime.datetime.now().replace(microsecond = 0)
            
        while (cap.isOpened()):
            frame_index = frame_index + 1
            cv2.setWindowProperty(fileName, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
            visual_prefer_x[(frame_index % 5)] = 0
            
            try:
                ret, image = cap.read()
                
                if image is None:
                    file.close()
                    fileWriter.close()
                    capWebCam.release()
                    cv2.destroyWindow(fileName)
                    return 
                      
                image = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)

                if frame_index % 5 == 0:
                    face_identified = 0
                
                if face_identified == 0:
                    result = " "
                    
                status = {ord('q'): 'exit', ord('Q'): 'exit',
                          -1: status, 27: 'exit'}[cv2.waitKey(1)]

                retWebCam, frame = capWebCam.read()
                frame = self.preliminaryHistogramEqualization(frame)
                    
                gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
                
                rect = gazeModel.detectFace(gray)  
                if rect is None:
                    cv2.imshow(fileName, image)
                    continue     

                # facial expression recognition
                face_crop = gray[rect.top():rect.bottom(), rect.left():rect.right()]
                facial_expression = facial_expression + emotionModel.getExpression(face_crop)
                
                eye_gaze_location = gazeModel.gazeDetection(gray, rect, frame, bias_const)
                visual_prefer_x[(frame_index % 5)] = eye_gaze_location
                        
                if frame_index % 5 == 0:
                    show_prefer[0] = np.sum(visual_prefer_x) // 5
                    preference = 'center'
                    face_identified = 1
                    
                    if show_prefer[0] < -10:
                        preference = 'left'
                    elif show_prefer[0] > 10:
                        preference = 'right'
                            
                    if (show_prefer[0] < -width_range) or (show_prefer[0] > width_range):
                        preference = 'ignore'
                    
                    result = target[np.argmax(facial_expression)]
                    facial_expression = np.array([0.14, 0.14, 0.14, 0.14, 0.14, 0.14, 0.16])
                            
                    info = str(frame_index) + ", " + preference + ", " + result + "\n"
                    fileWriter.write(info)
                
                avg_eye_gaze_location = np.sum(visual_prefer_x) // 5
                show_prefer[0] = self.gaze_position_estimation(avg_eye_gaze_location, scrn_width, width_range)
                
                if (show_prefer[0] < 0):
                    show_prefer[0] = 0
                if(show_prefer[0] > scrn_width):
                    show_prefer[0] = scrn_width     
                
                cur_time = datetime.datetime.now().replace(microsecond = 0)
                time_slice = (cur_time - start_time).total_seconds()
                #print(start_time, " ", cur_time, " ", time_slice)
                finalResult = None

                if time_slice >= 1.0:
                    print(show_prefer)
                    finalResult = str(cur_time) + ":  " + str(show_prefer[0]) + ", " + str(show_prefer[1])
                    #print("Final result: ", finalResult)
                    file.write(finalResult + "\n")

                    start_time = cur_time
                    time_slice = 0
                

                cv2.circle(image, tuple(show_prefer), 50, (0, 0, 150), -1)
                cv2.circle(image, tuple(show_prefer), 20, (0, 0, 255), -1)
                cv2.imshow(fileName, image)
                
                if status == 'play':
                    frame_rate = cv2.getTrackbarPos('F', 'image')
                    continue

                if status == 'exit':
                    fileWriter.close()
                    capWebCam.release()
                    cv2.destroyWindow(fileName)
                    return 

            except:
                pass
        file.close()
        fileWriter.close()
        capWebCam.release()
        cv2.destroyWindow(fileName)
    
    
    
    
    def showMessage(self, msg):
        master = tkinter.Tk()
        w_message = Message(master, text=msg, width=700)
        w_message.pack(padx=10, pady=20)
        Button(master, text='Close', command=lambda:self.remove_ui(master)).pack(pady=4)
        master.resizable(False, False)
        master.mainloop()
    
    
    def showWebcamError(self):
        error_master = tkinter.Tk()
        w_message = Message(error_master, text="Can not open webcam.", width=700)
        w_message.pack(padx=10, pady=20)
        Button(error_master, text='Close', command=lambda:self.remove_ui(error_master)).pack(pady=4)
        error_master.resizable(False, False)
        error_master.mainloop()
    
    
    def __init__(self, parent=None):
        super(VideoWindow, self).__init__(parent)
        self.setWindowTitle("Eye Gaze Detection")

        self.width_bias = 30
        self.bias_const = 200
        self.openFile()
      
        
    
    def exitCall(self):
        sys.exit(app.exec_())


    

if __name__ == '__main__':
    app = QApplication(sys.argv)
    player = VideoWindow()
    player.resize(640, 480)
    player.show()
    sys.exit(app.exec_())





