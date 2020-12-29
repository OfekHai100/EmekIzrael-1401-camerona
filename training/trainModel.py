from tensorflow.keras import models, callbacks
import numpy as np
import cv2
import wandb
from wandb.keras import WandbCallback

def buildData(data):
	x = []
	y_guess = []
	y_x = []
	y_y = []
	for line in data:
		l = line.split(' ')
		img = cv2.imread('dataset\\'+l[0])
		img = cv2.resize(img, (256,256))/255.0
		x.append(img)
		l = l[1:]
		y1 = np.zeros(20)
		y = []
		y2 = []
		for points in l:
			points = points.split(',')
			y.append(float(points[0]))
			y.append(float(points[2]))
			y2.append(float(points[1]))
			y2.append(float(points[3]))
		for i in range(len(y)//2):
			y1[i] = 1
		y_guess.append(y1)
		y_x.append(y)
		y_y.append(y2)
	return x, y_guess, y_x, y_y



def main():
	wandb.init(project="face_detector")
	model_path = 'models\\base_model.h5'
	save_at = "models\\best.h5"
	val_text = "dataset\\val.txt"
	train_text = "dataset\\train.txt"
	test_text = "dataset\\test.txt"

	best_callback = callbacks.ModelCheckpoint(save_at, save_best_only=True)
	wandb_callback = WandbCallback(data_type="images")

	model = models.load_model(model_path)

	f = open(val_text, 'r')
	val_data = f.read().split('\n')
	f.close()
	val_x, val_y_guess, val_y_x, val_y_y = buildData(val_data)

	f = open(train_text, 'r')
	train_data1 = f.read().split('\n')
	f.close()
	train_data = []
	l = len(train_data1)
	i = 0
	cnt = 0
	while i < l:
		cnt+=1
		a = []
		while i < 1000*cnt and i < l:
			a.append(train_data1[i])
			i += 1
		train_data.append(a)
		i += 1

	train_data1 = 0
	best_models = []

	for data in train_data:
		train_x, train_y_guess, train_y_x, train_y_y = buildData(data)

		history = model.fit(train_x,
						[train_y_guess, train_y_x, train_y_y],
						epochs=8, 
						validation_data=(val_x,[val_y_guess, val_y_x, val_y_y]),
						callbacks=[best, wandb_callback])
		best_models.append(models.load_model(save_at))

	val_x, val_y_guess, val_y_x, val_y_y = 0,0,0,0
	train_x, train_y_guess, train_y_x, train_y_y = 0,0,0,0
	train_data = 0

	f = open(test_text, 'r')
	test_data = f.read().split('\n')
	f.close()
	test_x, test_y_guess, test_y_x, test_y_y = buildData(test_text)
	best_acc = 0
	best_model = None
	for model in best_models:
		loss, acc = model.evaluate(test_x, [test_y_guess, test_y_x, test_y_y])
		if acc > best_acc:
			best_acc = acc
			best_model = model

	model.save(save_at)

if __name__ == '__main__':
	main()