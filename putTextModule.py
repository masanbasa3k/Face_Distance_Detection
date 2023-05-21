import cv2

def putText(image, text, org=(100, 100), font=cv2.FONT_HERSHEY_SIMPLEX,  fontScale=1, color=(255, 0, 0), thickness=2):
    return cv2.putText(image, text, org, font, fontScale, color, thickness, cv2.LINE_AA)