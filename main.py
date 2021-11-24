import shutil
from yolov5 import detect

file = "detect.py"

# Update yolov5 package directory (detect.py)
location = "C:\\Users\\nahvi\\AppData\\Local\\Programs\\Python\\Python39\\Lib\\site-packages\\yolov5\\detect.py"

shutil.copyfile(file, location)
print("detect.py has been successfully copied!")

# select the type of camera (0,1,2,.. for webcam / IP for IP cameras)

cam = "https://21.176.117.223:8080//video"
# cam = 0

eva = detect.run(source=cam, weights="best.pt", conf_thres=0.5, imgsz=640)

