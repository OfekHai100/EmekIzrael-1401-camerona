import cv2
import os
from Coffe import *

def main():
	face_detector = Coffe()
	path = "vid.mp4"
	dst = "good\\"
	i = len(os.listdir(dst)) + 1
	j = 0
	cap = cv2.VideoCapture('vid.mp4')
	while(cap.isOpened()):
		ret, frame = cap.read()
		frame2 = frame
		if ret == False:
			break
		l = face_detector.countFaces(frame2)
		if l > 0 and j%5 == 0:
			output_path = os.path.join(dst, str(i)+'.jpg')
			cv2.imwrite(output_path, frame)
			i += 1
		j += 1
	cap.release()
	cv2.destroyAllWindows()

if __name__ == '__main__':
    main()