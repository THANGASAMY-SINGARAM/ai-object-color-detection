import cv2
import numpy as np
from util import get_limits

colors = {
    "yellow": ([0, 255, 255], (0, 255, 255)),
    "blue":   ([255, 0, 0],   (255, 0, 0)),
    "green":  ([0, 255, 0],   (0, 255, 0)),
    "red":    ([0, 0, 255],   (0, 0, 255))
}

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    for name, (bgr, box_color) in colors.items():
        limits = get_limits(bgr)

        if isinstance(limits[0], tuple):
            mask1 = cv2.inRange(hsv, limits[0][0], limits[0][1])
            mask2 = cv2.inRange(hsv, limits[1][0], limits[1][1])
            mask = mask1 | mask2
        else:
            lower, upper = limits
            mask = cv2.inRange(hsv, lower, upper)

        contours, _ = cv2.findContours(
            mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
        )

        for cnt in contours:
            if cv2.contourArea(cnt) > 800:
                x, y, w, h = cv2.boundingRect(cnt)
                cv2.rectangle(frame, (x, y), (x+w, y+h), box_color, 3)
                cv2.putText(
                    frame, name,
                    (x, y-10),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.6,
                    box_color,
                    2
                )

    cv2.imshow("Multi-Color Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
