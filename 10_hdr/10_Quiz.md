# Quiz Questions

## 1. The purpose of `cv2.createAlignMTB` is:

- [ ] To create a multi-threaded image blending object for stitching images
- [ ] To create a camera calibration object for determining camera parameters
- [x] To create an object for aligning images based on brightness differences
- [ ] To create an object for color correction and white balancing of images

## 2. What is the purpose of the tone mapping process?

- [ ] To map the gradients of an image, with respect to the target image.
- [x] To reduce the dynamic range of the HDR image for display on a low dynamic range monitor
- [ ] To sharpen the edges and details of the HDR image
- [ ] To convert the HDR image to a grayscale format

## 3. For an object of class `createCalibrateDebevec()`, which method is used to estimate camera response function?

- [ ] calibrateDebevec.calculate(times, images)
- [ ] calibrateDebevec.process(times, images)
- [ ] calibrateDebevec.calculate(images, times)
- [x] calibrateDebevec.process(images, times)

## 4. Which OpenCV function is used to merge exposures into an HDR image?

- [ ] cv2.merge()
- [ ] cv2.cvtColor()
- [ ] cv2.stitcher()
- [x] cv2.createMergeDebevec()

## 5. How does `cv2.createMergeDebevec` handle over- and under-exposed pixels?

- [ ] By discarding them
- [ ] By compressing their values
- [x] By using an adaptive weighting function
- [ ] By interpolating their values

## 6. Which of the following is a potential issue when using `cv2.createMergeDebevec`?

- [x] Motion blur in the input images
- [ ] Overlapping regions in the input images
- [ ] Low contrast in the input images
- [ ] None of the above
