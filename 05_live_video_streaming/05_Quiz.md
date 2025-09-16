# Quiz Questions

## 1. What is the correct way to release the resources used by `cv2.VideoCapture()` when done with the webcam? Here `cap` is an object of

- [x] cap.release()
- [ ] cap.end()
- [ ] cap.close()
- [ ] None of the above.

## 2. Which of the following is not a valid way to call `cv2.VideoCapture()`?

- [x] cap = cv2.VideoCapture('https://www.youtube.com/watch?v=xxxxxxxxxxx')
- [ ] cap = cv2.VideoCapture("video.avi") # video.avi is present at the same location
- [ ] cap = cv2.VideoCapture(0)
- [ ] cap = cv2.VideoCapture("images/img\_%02d.jpg") #where images folder contains sequences of images

## 3. What is the purpose of `cv2.waitKey(1) != 27` in OpenCV?
- [ ] To pause the execution of the program until a key is pressed
- [ ] To wait for 1 second before executing the next frame
- [x] To check if the Esc key has been pressed 
- [ ] To check if the Enter key has been pressed