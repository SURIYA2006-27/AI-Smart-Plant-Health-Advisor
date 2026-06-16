import cv2
import numpy as np

def is_leaf(image_path):
    img = cv2.imread(image_path)

    if img is None:
        return False

    img = cv2.resize(img, (224, 224))

    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    lower_green = np.array([25, 40, 40])
    upper_green = np.array([95, 255, 255])

    mask = cv2.inRange(hsv, lower_green, upper_green)

    green_ratio = np.sum(mask > 0) / (224 * 224)

    return green_ratio > 0.15