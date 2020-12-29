import cv2
import os
from Coffe import *

def main():
	face_detector = Coffe(0.65)
	path = "val\\"
	dst = "val.txt"
	f = open(dst, 'w+')
	images = os.listdir(path)
	i = 1
	for img in images:
		f.write(path+img+' ')
		im = cv2.imread(path+img)
		(h, w) = im.shape[:2]
		ans = face_detector.getBbox(im)
		for p in ans:
			cnt = 0
			for val in p:
				if cnt%2 == 0:
					val = val/w
				else:
					val = val/h
				out = str(val)
				if cnt != 3:
					f.write(out+',')
				else:
					f.write(out+' ')
				cnt += 1
		f.write('\n')

if __name__ == '__main__':
    main()