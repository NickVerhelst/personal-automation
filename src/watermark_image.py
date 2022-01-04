import cv2
watermark = cv2.imread("watermark.png")
img = cv2.imread("no-problem.jpg")


h_img, w_img, _ = img.shape
center_x = int(w_img/2)
center_y = int(h_img/2)

h_watermark, w_watermark, _ = watermark.shape
top_y = center_y - int(h_watermark/2)
left_x = center_x - int(w_watermark/2)
bottom_y = top_y + h_watermark
right_x = left_x + w_watermark

position = img[top_y:bottom_y, left_x:right_x]
result = cv2.addWeighted(position, 1, watermark, 0.5, 0)

img[top_y:bottom_y, left_x:right_x] = result
cv2.imwrite("watermarked_image.jpg", img)
cv2.imshow("Image With Watermark", img)
cv2.waitKey(0)
cv2.destroyAllWindows()