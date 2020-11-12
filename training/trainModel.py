from tensorflow.keras import models, callbacks
import numpy as np
import cv2
import os
import random

#with mask = 0
#without mask = 1

def getAllData(paths):
	all_data = []
	for path, num in paths:
		goal = len(os.listdir(path))
		for i in range(1, goal+1):
			add = []
			img = cv2.imread(path+str(i)+'.jpg')
			img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
			img = cv2.resize(img, (64,64))/255
			img.reshape(img, (64,64,-1))
			print(img.shape)
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

def main():
	model_path = 'models\\base_model.h5'
	model = models.load_model(model_path)

	best = callbacks.ModelCheckpoint("models\\best.h5", save_best_only=True)

	paths = [["dataset_mask\\with_mask\\", 0], ["dataset_mask\\without_mask\\", 1]]
	x_train, y_train = splitAllData(getAllData(paths))

	paths = [["dataset_mask\\validation\\with_mask\\", 0], ["dataset_mask\\validation\\without_mask\\", 1]]
	x_valid, y_valid= splitAllData(getAllData(paths))

	history = model.fit(x_train, y_train, epochs=20, 
						validation_data=(x_valid,y_valid),
						callbacks=[best])

if __name__ == '__main__':
	main()