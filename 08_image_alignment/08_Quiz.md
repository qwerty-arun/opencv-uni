# Quiz Questions

## 1. Which feature detection algorithm is the fastest?

- [ ] SIFT
- [ ] SURF
- [x] ORB
- [ ] All have similar speed

## 2. Which of the following cv2 function can be used to visualize the keypoints detected in an image?

- [ ] cv2.visualizeKeypoints()
- [x] cv2.drawKeypoints()
- [ ] cv2.Keypoints.draw()
- [ ] cv2.drawMatches()

## 3. In `ORB.detectAndCompute()`, what is the role of the mask parameter?

- [x] It specifies a region of interest where keypoints should be detected
- [ ] It specifies the maximum number of keypoints to be detected
- [ ] It filters out keypoints that are not within the specified mask
- [ ] It has no role in ORB.detectAndCompute()

## 4. The role of `DescriptorMatcher` in feature matching is:

- [ ] It creates feature descriptors for the input image
- [x] It matches the feature descriptors of two images correct
- [ ] It removes the redundant features from an image
- [ ] It creates a binary mask for the matched features

## 5. Which method will be called for descriptor matching with the following code `matcher = cv2.DescriptorMatcher_create(2)` ?

- [x] Brute-Force
- [ ] Brute-Force-L1
- [ ] Brute-Force-Hamming
- [ ] FlannBased

## 6. The role of `cv2.getPerspectiveTransform()` in perspective transformation is:

- [x] It computes the homography matrix from the corresponding points
- [ ] It applies the homography matrix to the input image
- [ ] It specifies the region of interest in the input image
- [ ] It computes the inverse of the homography matrix
