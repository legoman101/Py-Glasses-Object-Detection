# import necessary packages
import cvlib as cv
from cvlib.object_detection import draw_bbox
import cv2

# open webcam
webcam = cv2.VideoCapture(0)

if not webcam.isOpened():
    print("Could not open webcam")
    exit()
    

# loop through frames
while webcam.isOpened():

    # read frame from webcam 
    status, frame = webcam.read()

    if not status:
        break

    # apply object detection
    bbox, label, conf = cv.detect_common_objects(frame, confidence=0.25, model='yolov3-tiny')
    
    #print the boxes and labels around the objects
    print(bbox, label, conf)


    # draw bounding box over detected objects
    out = draw_bbox(frame, bbox, label, conf, write_conf=True)

    # display output
    cv2.imshow("Real-time object detection", out) 
    
    #need to somehow stream this to a ip address
    
        
    # press "Q" to stop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
# release resources
webcam.release()
cv2.destroyAllWindows()