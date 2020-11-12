from tensorflow.keras import models, callbacks
import numpy as np
import cv2
import os
import random

def getAllData(paths):
	all_data = []
	for path, num in paths:
		goal = len(os.listdir(path))
		for i in range(1, goal+1):
			add = []
			img = cv2.imread(path+str(i)+'.jpg')
			img = cv2.resize(img, (64,64))/255
			is_wearing = num
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


def eval(model):
	paths = [["dataset_mask\\test\\with_mask\\", 0], ["dataset_mask\\test\\without_mask\\", 1]]
	x_test, y_test= splitAllData(getAllData(paths))

	loss, acc = model.evaluate(x_test, y_test)
	print("loss: {:.2f} accuracy: {:.2f}%".format(loss, acc*100))

def train(model):
	best = callbacks.ModelCheckpoint("models\\best.h5", save_best_only=True)

	paths = [["dataset_mask\\with_mask\\", 0], ["dataset_mask\\without_mask\\", 1]]
	x_train, y_train = splitAllData(getAllData(paths))

	paths = [["dataset_mask\\validation\\with_mask\\", 0], ["dataset_mask\\validation\\without_mask\\", 1]]
	x_valid, y_valid= splitAllData(getAllData(paths))

	"""history = model.fit(x_train, y_train, epochs=20, 
									validation_data=(x_valid,y_valid),
									callbacks=[best])"""

	print(x_train.shape)
	return model

def main():
	path = 'models\\base_model.h5'
	model = models.load_model(path)
	model = train(model)
	eval(model)

	

if __name__ == '__main__':
	main()