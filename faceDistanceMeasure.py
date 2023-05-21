import install_requirements

import cv2
from faceMeshModule import faceMeshDetection

# font
font = cv2.FONT_HERSHEY_SIMPLEX

video = 'Video.mp4'
cap = cv2.VideoCapture(video)
detector = faceMeshDetection()

run = True
while run:
    success, img = cap.read()
    img, faces = detector.findFaceMesh(img, draw=False)

    if faces:
        face = faces[0]
        pointLeft = face[145]
        pointRight = face[374]

        # draw the eye dots and line
        # cv2.line(img, pointLeft, pointRight, (255,0,0), 3)
        # cv2.circle(img,pointLeft,5,(0,0,255),cv2.FILLED)
        # cv2.circle(img,pointRight,5,(0,0,255),cv2.FILLED)

        w, _ = detector.findDistance(pointLeft, pointRight)
        W = 6

        # find the focal lenght
        # f_list = []
        # d = 50
        # f = (w * d) / W
        # f_list.append(f)
        # print(sum(f_list)/len(f_list))
        # We decided it would be 2222

        # Find distance
        f = 2222
        d = (W * f) / w

        # Adding distance text
        img = cv2.putText(img, f'Distance : {d:.1f}cm', (face[10][0]-100, face[10][1]), font, 3, (255, 0, 0), 3, cv2.LINE_AA)


    img = cv2.resize(img, (640, 360))
    cv2.imshow("Image", img)
    cv2.waitKey(1)

#Explenation
# f = local lenght
# w = width in pixels
# d = distance in en
# W = width in em

# Focal Lenght
# f = (w * d) / W
# Distance 
# d = (W * f) / w