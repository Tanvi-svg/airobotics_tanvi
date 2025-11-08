from ultralytics import YOLO
from time import sleep
import cv2
from picamera2 import Picamera2

picam2=Picamera2()
picam2.preview_configuration.main.size=(640,480)
picam2.preview_configuration.main.format = "RGB888"
picam2.configure("preview")
picam2.start()

model= YOLO("yolo11n.pt")#pt= pytorch (object decting algorithim), and this is the file that hold it.

model.export(format="ncnn")#faster processing speed,novel convelutional neural network, a file format used in object detection made by tensten. this is the fastest file format for raspberry pi till now

ncnn_model= YOLO("yolo11n_ncnn_model")

while True:
    frame = picam2.capture_array()
    
    results = ncnn_model(frame)
    
    
    annotated_frame= results[0].plot()
    
    cv2.imshow("Frame", frame)
    cv2.imshow("Camera", annotated_frame)
    
    if cv2.waitKey(1)==ord("q"):
        break
    
cv2.destroyAllWindows()