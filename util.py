import cv2
import numpy as np

def get_limits(color):
    c = np.uint8([[color]])
    hsvC = cv2.cvtColor(c, cv2.COLOR_BGR2HSV)

    h, s, v = hsvC[0][0]

    # white/gray
    if s < 40:
        lower = np.array([0, 0, 180], dtype=np.uint8)
        upper = np.array([179, 40, 255], dtype=np.uint8)
        return lower, upper

    # red
    if h < 10:
        lower1 = np.array([0, 80, 80], dtype=np.uint8)
        upper1 = np.array([h + 10, 255, 255], dtype=np.uint8)

        lower2 = np.array([170, 80, 80], dtype=np.uint8)
        upper2 = np.array([179, 255, 255], dtype=np.uint8)

        return (lower1, upper1), (lower2, upper2)

    lower = np.array([h - 10, 80, 80], dtype=np.uint8)
    upper = np.array([h + 10, 255, 255], dtype=np.uint8)

    return lower, upper
