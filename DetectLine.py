import cv2
import numpy as np

gray_ime = [[0] * 640] * 340


def DetectStraightLine(src):

    def Grayscale(src):
        for i in range(0, 639):
            for j in range(0, 339):
                gray_ime[i][j] = src[i][j].B - (src[i][j].R + src[i][j].G)
                if gray_ime[i][j] < 0:
                    gray_ime[i][j] = 0
    # GrayScale로 변환
    grayscale1 = cv2.cvtColor(src, cv2.COLOR_BGR2HSV_FULL)

    # 모서리 검출
    can = cv2.Canny(Grayscale(frame), 50, 200, None, 3)

    height = can.shape[0]
    rectangle = np.array([[(0, height), (120, 200), (520, 200), (640, height)]])
    mask = np.zeros_like(can)
    cv2.fillPoly(mask, rectangle, 255)
    masked_image = cv2.bitwise_and(can, mask)
    ccan = cv2.cvtColor(masked_image, cv2.COLOR_GRAY2BGR)


    # 원본에 합성
    outcome = cv2.addWeighted(src, 1, ccan, 1, 0)
    return outcome

cam = cv2.VideoCapture(0)

if not cam.isOpened():
    print("Could not open webcam")
    exit()




while cam.isOpened():

    status, frame = cam.read()

    if status:
        frame = cv2.resize(frame, (640, 360))
        cv2.imshow('test', DetectStraightLine(frame))

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cv2.destroyAllWindows()