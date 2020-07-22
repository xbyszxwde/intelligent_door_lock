import cv2
import time

#实现拍照
def baizhao():
	cap = cv2.VideoCapture(0)
	shumu=1
	while shumu<11:
		ret, frame = cap.read()
		cv2.imshow("capture", frame)
		if cv2.waitKey(1):
			cv2.imwrite("./lock_data{}.jpg".format(str(shumu)), frame)
			time.sleep(1)
			shumu+=1
	cap.release()
	cv2.destroyAllWindows()

baizhao()