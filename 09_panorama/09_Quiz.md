# Quiz Questions

## 1. The purpose of image blending in image stitching is:
- [ ] To remove parallax errors in the images
- [ ] To align the images to a common reference frame
- [x] To seamlessly merge overlapping regions and remove visible seams
- [ ] To resize the images to the same size


## 2. What is the process of creating a panorama in OpenCV?
- [ ] Stacking multiple images on top of each other
- [x] Merging multiple images to create a wide-angle image 
- [ ] Cropping multiple images to create a panoramic view
- [ ] None of the above

## 3. Given `stitcher = cv2.Stitcher_create()`. What method of stitcher is used to create panaroma image?
- [ ] stitcher.apply(images)
- [ ] stitcher.create(images)
- [ ] stitcher.create_panaroma(images)
- [x] stitcher.stitch(images) 

## 4. Which technique is commonly used to ensure that the stitching process produces a seamless panorama?
- [ ] Image cropping
- [x] Image blending 
- [ ] Image scaling
- [ ] None of the above

## 5. What is the purpose of the `cv2.Stitcher()` class in OpenCV
- [ ] To detect features in an image
- [ ] To match features in two images
- [x] To stitch multiple images together to create a panorama 
- [ ] To crop an image