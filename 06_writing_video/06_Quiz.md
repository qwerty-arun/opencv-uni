# Quiz Questions

## 1. VideoWriter in OpenCV is used to:

- [ ] To capture video from a webcam
- [ ] To play video files
- [x] To write frames to a video file
- [ ] To read frames from a video file

## 2. How can you check if `cap.read()` was successful? (Here: cap = cv2.VideoCapture())

- [ ] By checking the value of the isOpened() function.
- [ ] By checking the value of the capOpened() variable.
- [x] By checking the return value of the function cap.read().
- [ ] None of the above.

## 3. For a VideoWriter object output, how can we release it's memory at the end of the program
- [ ] output.erase()
- [ ] output.release_memory()
- [x] output.release() 
- [ ] output.releaseAllWindows()

## 4. How can you handle errors that may occur when using `cap.read()`?
- [ ] By checking the return value of the function and handling any errors accordingly.
- [ ] By using a try-except block to catch any exceptions that may be raised.
- [ ] By using the isOpened() function to check if the video capture object is still open before calling cap.read()
- [x] All of the above 

## 5. What does fourcc mean in `cv2.VideoWriter()`?
- [x] It refers to the four-character code used to specify the codec to be used for video compression 
- [ ] It is a parameter to set the frame rate of the output video
- [ ] It is the size of the video frame in pixels
- [ ] It is the file extension of the output video file
