# Quiz questions for TensorFlow Object Detection

## 1. What is a TF model?
- [ ] A dataset used for training machine learning models.
- [ ] A set of rules that a machine learning model uses to make predictions.
- [ ] A software library for developing and training machine learning models.
- [x] A machine learning model that has been trained on a specific task. 

## 2. The benefits of using TF is/are:
- [ ] Scalability and performance
- [ ] Flexibility and ease of use
- [ ] Wide range of supported platforms and languages
- [x] All of the above 

## 3. What is the default order of the channels in the output of cv2.dnn.blobFromImage function()?
- [ ] RGB
- [x] BGR
- [ ] GRB
- [ ] BRG

## 4. What is the effect of specifying the parameter crop = False in blobFromImage() ?
- [ ] Crops the image to the specified size
- [x] Resizes the image without cropping
- [ ] Performs center cropping of the image
- [ ] Performs random cropping of the image

## 5. Given objects = net.forward() , shape of the variable objects is (1, 1, n, 7), here n is the number of objects detected. For each detected object, we have an array of length 7 to describe it. How can we extract the score (or confidence) of nth detected object ?
- [ ] objects[0, 0, n-1, 1]
- [x] objects[0, 0, n-1, 2]
- [ ] objects[0, 0, n-1, 3]
- [ ] objects[0, 0, n-1, 4]