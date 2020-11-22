from tensorflow.keras import models, callbacks
import numpy as np
import cv2
import os
import random

#female = 1
#male = 0

def getAllData(paths):
	all_data = []
	for path, num in paths:
		goal = len(os.listdir(path))
		for i in range(1, goal+1):
			add = []
			img = cv2.imread(path+str(i)+'.jpg')
			img = cv2.resize(img, (64,64))/255
			add.append(img)
			add.append(num)
			all_data.append(add)
	return all_data

def splitAllData(all_data):
	random.shuffle(all_data)
	x = []
	y = []
	for i in range(0,len(all_data)):
		x.append(all_data[i][0])
		y.append(all_data[i][1])
	x = np.array(x)
	y = np.array(y)
	return x,y

def main():
	model_path = 'models\\best.h5'
	model = models.load_model(model_path)

	test_paths = [["dataset_gender\\test\\male\\", 0], ["dataset_gender\\test\\female\\", 1]]

	x_test, y_test = splitAllData(getAllData(test_paths))

	loss, acc = model.evaluate(x_test, y_test)
	print("loss: {:.2f} accuracy: {:.2f}%".format(loss, acc*100))
		

if __name__ == '__main__':
	main()