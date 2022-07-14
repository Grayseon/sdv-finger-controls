import cv2
import mediapipe as mp
import pyautogui
pyautogui.FAILSAFE = False
cap = cv2.VideoCapture(0)
hand_detector = mp.solutions.hands.Hands()
drawing_utils = mp.solutions.drawing_utils
screen_width, screen_height = pyautogui.size()
radius = 30
index_y = 0
index_x = 0
indexf_x = 0
indexf_y = 0
indexfnew_x = 0
indexfnew_y = 0
x = 0
y = 0
while True:
    _, frame = cap.read()
    frame = cv2.flip(frame, 1)
    frame_height, frame_width, _ = frame.shape
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    output = hand_detector.process(rgb_frame)
    hands = output.multi_hand_landmarks
    cv2.circle(img=frame, center=(int(frame_width/2), int(frame_height/2)), radius=0, color=(0,0,0), thickness=frame_width+frame_height)
    if hands:
        for hand in hands:
            landmarks = hand.landmark
            drawing_utils.draw_landmarks(frame, hand)
            for id, landmark in enumerate(landmarks):
                x = int(landmark.x*frame_width)
                y = int(landmark.y*frame_height)
                if id == 8:
                    cv2.circle(img=frame, center=(x,y), radius=10, color=(0, 255, 255))
                    index_x = screen_width/frame_width*x
                    index_y = screen_height/frame_height*y
                    if abs(index_y - thumb_y) < radius:
                        pyautogui.keyUp("d")
                        pyautogui.keyUp('a')
                        pyautogui.keyUp('s')
                        pyautogui.keyUp('w')

                if id == 4:
                    cv2.circle(img=frame, center=(x,y), radius=10, color=(0, 0, 255))
                    thumb_x = screen_width/frame_width*x
                    thumb_y = screen_height/frame_height*y
                    pyautogui.moveTo(index_x, index_y+200)

                if id == 12:
                    cv2.circle(img=frame, center=(x,y), radius=10, color=(255, 255, 0))
                    indexfnew_x = screen_width/frame_width*x
                    indexfnew_y = screen_height/frame_height*y
                    
                    print(abs(indexf_y - thumb_y))
                    if abs(indexf_y - thumb_y) < radius and not indexf_x == 0:
                        if index_y > (screen_height / 2):
                            pyautogui.keyDown("s")
                            pyautogui.keyUp('w')
                        if index_y < (screen_height / 2):
                            pyautogui.keyDown("w")
                            pyautogui.keyUp('s')
                        if index_x < (screen_width / 2):
                            pyautogui.keyDown("a")
                            pyautogui.keyUp('d')
                        if index_x > (screen_width / 2):
                            pyautogui.keyDown("d")
                            pyautogui.keyUp('a')
                    indexf_x = screen_width/frame_width*x
                    indexf_y = screen_height/frame_height*y

                if id == 16:
                    cv2.circle(img=frame, center=(x,y), radius=10, color=(255, 0, 255))
                    index_x = screen_width/frame_width*x
                    index_y = screen_height/frame_height*y
                    if abs(index_y - thumb_y) < radius:
                        pyautogui.leftClick()

                if id == 20:
                    cv2.circle(img=frame, center=(x,y), radius=10, color=(255, 0, 0))
                    index_x = screen_width/frame_width*x
                    index_y = screen_height/frame_height*y
                    if abs(index_y - thumb_y) < radius:
                        pyautogui.rightClick()
    cv2.imshow('Virtual Mouse', frame)
    cv2.waitKey(1)
    if hands == None:
        pyautogui.keyUp("d")
        pyautogui.keyUp('a')
        pyautogui.keyUp('s')
        pyautogui.keyUp('w')