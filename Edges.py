import cv2

image = cv2.imread(r"C:\Users\LEGION\Desktop\camera.jpg")
Gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

canny1 = cv2.Canny(Gray,100,170)
canny2 = cv2.Canny(Gray,100,170)

# sobelx = cv2.Sobel(Gray,cv2.64)

cv2.imshow("Canny1",canny1)
cv2.imshow("Canny2",canny2)
cv2.waitKey(0)
