# Quiz Questions

## 1. Given the following code ->

```python
arr1 = np.array([200, 250], dtype=np.uint8).reshape(-1, 1)
arr2 = np.array([40, 40], dtype=np.uint8).reshape(-1, 1)
add_numpy = arr1+arr2
add_cv2 = cv2.add(arr1, arr2)
```

Then the value of add_numpy and add_cv2 respectively are -

- [ ] [ [240, 290] ] , [ [240, 290] ]
- [ ] [ [240, 34] ] , [ [240, 290] ]
- [ ] [ [240, 255] ] , [ [240, 34] ]
- [x] [ [240, 34] ] , [ [240, 255] ]

## 2. Which of the following is not a valid threshold type in Opencv (type parameter in cv2.threshold)?

- [ ] cv2.THRESH_BINARY
- [x] cv2.THRESH_BINARY_ADV
- [ ] cv2.THRESH_BINARY_INV
- [ ] cv2.THRESH_OTSU

## 3. When `cv2.threshold()` function is applied to a grayscale image with a threshold value of 127 and maximum value of 255, then:

### Hint: Assume THRESH_BINARY being applied in the process.

- [ ] Pixels with intensity less than 127 are set to 0, and pixels with intensity greater than or equal to 127 are set to 255.
- [x] Pixels with intensity less than or equal to 127 are set to 0, and pixels with intensity greater than 127 are set to 255. 
- [ ] Pixels with intensity greater than 127 are set to 0, and pixels with intensity less than or equal to 127 are set to 255.
- [ ] Pixels with intensity greater than or equal to 127 are set to 0, and pixels with intensity less than 127 are set to 255
