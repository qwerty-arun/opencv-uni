import cv2 as cv
import sys

s = 0 # device index of 0, default camera on your system
if len(sys.argv) > 1:
    s = sys.argv[1]

source = cv.VideoCapture(s)

win_name="Camera Preview"
cv.namedWindow(win_name, cv.WINDOW_NORMAL)

while cv.waitKey(1) != 27: # Escape
    has_frame, frame = source.read()
    if not has_frame:
        break
    cv.imshow(win_name, frame)

source.release()
cv.destroyWindow(win_name)

# Which of the following is not a valid way to call cv2.VideoCapture()?
# cap = cv2.VideoCapture('https://www.youtube.com/watch?v=xxxxxxxxxxx') correct
# cap = cv2.VideoCapture("video.avi") # video.avi is present at the same location
# cap = cv2.VideoCapture(0)
# cap = cv2.VideoCapture("images/img_%02d.jpg") #where images folder contains sequences of images