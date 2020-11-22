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

def loadSingleData(start_at, end_at, path, num):
	ending = ".jpg"
	toRet = []
	for i in range(start_at, end_at+1):
		add = []
		img = cv2.imread(path+str(i)+'.jpg')
		img = cv2.resize(img, (64,64))/255
		add.append(img)
		add.append(num)
		toRet.append(add)
	return toRet

def combineArrays(arr1, arr2):
	for ob in arr2:
		arr1.append(ob)
	return np.array(arr1)

def getBest(models):
	highest = 0
	for model, acc in models:
		if acc>highest:
			highest = acc
			to_ret = model
	return to_ret

def main():
	model_path = 'models\\base_model.h5'
	save_model_at = "models\\best.h5"
	model = models.load_model(model_path)

	best = callbacks.ModelCheckpoint(save_model_at, save_best_only=True)

	paths_train = [["dataset_gender\\train\\male\\", 0], ["dataset_gender\\train\\female\\", 1]]
	paths_val = [["dataset_gender\\validation\\male\\", 0], ["dataset_gender\\validation\\female\\", 1]]

	x_valid, y_valid= splitAllData(getAllData(paths_val))
	print("loaded validation data")

	train_iterations = len(os.listdir(paths_train[1][0]))//1000
	train_female = 1000
	train_male = len(os.listdir(paths_train[0][0]))//train_iterations

	models_after = []

	for it in range(0, train_iterations):
		print("{} out of: {}".format(it+1, train_iterations))
		add = []
		female_train_data = loadSingleData(it*train_female + 1, (it + 1)*train_female, paths_train[1][0], paths_train[1][1])
		male_train_data = loadSingleData(it*train_male + 1, (it + 1)*train_male, paths_train[0][0], paths_train[0][1])
		training_data = combineArrays(female_train_data, male_train_data)

		x_train, y_train = splitAllData(training_data)
		print("loaded trainning data")

		history = model.fit(x_train, y_train, epochs=4, 
							validation_data=(x_valid,y_valid),
							callbacks=[best])

		add.append(models.load_model(save_model_at))
		loss, acc = model.evaluate(x_valid, y_valid)
		acc *= 100
		add.append(acc)
		models_after.append(add)

	model = getBest(models_after)
	model.save(save_model_at)

if __name__ == '__main__':
	main()