# Quiz Questions

## 1. What happens if the filename specified in `cv2.imwrite` already exists?

- [ ] An error is raised
- [x] The existing file is overwritten correct
- [ ] A new file is created
- [ ] None of the above

## 2. Given a colored image `image.jpeg` which of these will result in an error?

- [ ] img = cv2.imread("image.jpeg", 0) img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)

- [ ] img = cv2.imread("image.jpeg", 1) img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

- [ ] img = cv2.imread("image.jpeg", 1) img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

- [x] img = cv2.imread("image.jpeg", 0) img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

## 3. What is the difference between `cv2.IMREAD_COLOR` and `cv2.IMREAD_GRAYSCALE`?

- [ ] cv2.IMREAD_COLOR is used to read the image as a grayscale image, while cv2.IMREAD_GRAYSCALE is used to read the image as a color image.
- [x] cv2.IMREAD_GRAYSCALE is used to read the image as a grayscale image, while cv2.IMREAD_COLOR is used to read the image as a color image. correct
- [ ] There is no difference in using cv2.IMREAD_COLOR or cv2.IMREAD_GRAYSCALE
- [ ] None of the above

## 4. What is the purpose of the `cv2.cvtColor()`function?

- [x] To convert an image from one color space to another. correct
- [ ] To resize an image.
- [ ] To crop an image.
- [ ] To apply a filter to an image.

## 5. What is the return type of `plt.imshow()` of Matplotlib?

- [x] matplotlib.image.AxesImage object correct
- [ ] NumPy array
- [ ] PIL Image object
- [ ] None of the above
