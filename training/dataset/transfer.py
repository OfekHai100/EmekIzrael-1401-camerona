import os
from Coffe import *

def main():
	face_detector = Coffe()
	path = "dest\\"
	dst = "good\\"
	i = len(os.listdir(dst)) + 1
	images = os.listdir(path)
	print(len(images))
	for image in images:
		input_path = os.path.join(path, image)
		im = cv2.imread(input_path)
		cv2.imshow("cool", im)
		cv2.waitKey(1)
		f = input()
		if len(f) == 0:
			output_path = os.path.join(dst, str(i)+'.jpg')
			os.rename(input_path, output_path)
			i += 1
		else:
			os.remove(input_path)
	cv2.destroyAllWindows()

if __name__ == '__main__':
    main()