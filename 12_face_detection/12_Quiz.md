# Quiz questions for Face Detection

## 1. Which of the following is **NOT** mandatory to use the function: cv2.dnn.readNetFromCaffe?

- [ ] The .caffemodel file containing the pre-trained weights of the model
- [ ] The .prototxt file containing the model's architecture and configuration
- [ ] The model needs to be first fine-tuned on a custom dataset.
- [x] GPU

## 2. Which of the following will give the same result as `cv2.flip(img, 1)`?
- [x] img[:, ::-1,:]
- [ ] img[::-1, :, :]
- [ ] img[:, :, ::-1]
- [ ] img[:, :1,:]

## 3. Which of the following is a challenge in face detection?
- [ ] Variation in lighting and background
- [ ] Low contrast in facial features
- [ ] Pose and occlusion
- [x] All of the above