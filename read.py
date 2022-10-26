import cv2

img = cv2.imread("butterfly.jpg")

cv2.imshow("Display image",img)
print(img)
cv2.waitKey(0)
