import cv2
from Coffe import *
import imutils
import os

def main():
	path = "data\\without_mask\\"
	dst = "a\\"
	i = len(os.listdir(dst)) + 1
	j = 1
	images = os.listdir(path)
	for image in images:
		if j%100 == 0:
			print("{0}/{1}".format(j, len(images)))
		j += 1
		input_path = os.path.join(path, image)
		im = cv2.imread(input_path)
		output_path = os.path.join(dst, str(i)+'.jpg')
		os.rename(input_path, output_path)
		i += 1
		for angle in np.arange(10, 30, 5):
			rotated = imutils.rotate(im, angle)
			output_path = os.path.join(dst, str(i)+'.jpg')
			cv2.imwrite(output_path, rotated)
			i += 1
		for angle in np.arange(330, 360, 5):
			rotated = imutils.rotate(im, angle)
			output_path = os.path.join(dst, str(i)+'.jpg')
			cv2.imwrite(output_path, rotated)
			i += 1

if __name__ == '__main__':
    main()