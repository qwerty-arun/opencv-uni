# Quiz Questions

## 1. Which of the following line types is not supported by `cv2.line`?
- [ ] cv2.LINE_AA
- [ ] cv2.LINE_8
- [ ] cv2.LINE_4
- [x] cv2.LINE_16 correct

## 2. The purpose of the pt1 and pt2 parameters in `cv2.rectangle` is:
- [x] To specify the coordinates of the top-left and bottom-right corners of the rectangle 
- [ ] To specify the center and radius of the rectangle
- [ ] To specify the length and width of the rectangle
- [ ] To specify the angle and size of the rectangle

## 3. What happens if the specified fontScale in `cv2.putText()` is negative?
- [x] The text is mirrored or reversed
- [ ] The text will not be displayed
- [ ] The function will return an error
- [ ] The text size will be proportional to the image size

## 4. Which of the following is expected when thickness = -2 is passed in `cv2.circle()`?
- [ ] The size of the circle is shrunk by 2 times.
- [ ] The thickness of the circle is shrunk by 2 times.
- [ ] The brightness of the color is reduced.
- [x] The color fills the complete circle. 

## 5. When the thickness parameter is set to a negative value in `cv2.rectangle`, then:
- [x] The rectangle is filled with color instead of being outlined 
- [ ] The rectangle is not drawn
- [ ] An error is thrown
- [ ] The thickness is set to the absolute value of the negative value