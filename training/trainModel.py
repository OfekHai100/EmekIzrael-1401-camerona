from tensorflow.keras import models, callbacks
import numpy as np
import cv2

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
		y = np.zeros(40)#x1,x2
		y2 = np.zeros(40)#y1,y1
		cnt = 0
		for points in l:
			points = points.split(',')
			y[cnt] = float(points[0])
			y[cnt+1] = float(points[2])
			y2[cnt] = float(points[1])
			y2[cnt+1] = float(points[3])
			cnt += 2
		for i in range(0,cnt//2):
			y1[i] = 1
		y_guess.append(y1)
		y_x.append(y)
		y_y.append(y2)
	x, y_guess, y_x, y_y = np.array(x), np.array(y_guess), np.array(y_x), np.array(y_y)
	print(x.shape, y_guess.shape, y_x.shape, y_y.shape)
	return x, y_guess, y_x, y_y

def dataFromFile(path):
	f = open(path, 'r')
	ret = f.read().split('\n')
	f.close()
	return ret

def splitArrayToArrays(arr, am):
	l = len(arr)
	to_ret = []
	i = 0
	cnt = 0
	while i < l:
		cnt += 1
		a = []
		while i < am*cnt and i < l:
			a.append(arr[i])
			i+=1
		to_ret.append(a)
	return to_ret

def main():
	model_path = 'models\\base_model.h5'
	save_at = "models\\best.h5"
	val_text = "dataset\\val.txt"
	train_text = "dataset\\train.txt"
	test_text = "dataset\\test.txt"

	best_callback = callbacks.ModelCheckpoint(save_at, save_best_only=True)

	print("\n\nloding model")
	model = models.load_model(model_path)
	print("model loaded")

	print("\n\nloading val data")
	val_data = dataFromFile(val_text)
	val_x, val_y_guess, val_y_x, val_y_y = buildData(val_data)
	print("val data loaded")

	print("\n\nsorting train data")
	train_data = splitArrayToArrays(dataFromFile(train_text), 750)
	print("train data sorted")

	best_models = []

	cnt = 1
	l = len(train_data)
	for data in train_data:
		print("\n\niteration {0}/{1}".format(cnt, l))
		print("loading train data")
		train_x, train_y_guess, train_y_x, train_y_y = buildData(data)
		print("train data loaded")

		history = model.fit(train_x,
						[train_y_guess, train_y_x, train_y_y],
						epochs=8, 
						validation_data=(val_x, [val_y_guess, val_y_x, val_y_y]),
						callbacks=[best_callback],
						batch_size=3)
		best_models.append(models.load_model(save_at))
		cnt += 1

	##deleting unused data
	val_x, val_y_guess, val_y_x, val_y_y = 0,0,0,0
	train_data = 0

	print("\n\nloading test data")
	test_x, test_y_guess, test_y_x, test_y_y = buildData(dataFromFile(test_text))
	print("test data loaded")
	best_acc = 0
	best_model = None
	for model in best_models:
		loss, acc = model.evaluate(test_x, [test_y_guess, test_y_x, test_y_y])
		if acc > best_acc:
			print("accuracy: {0}".format(acc))
			best_acc = acc
			best_model = model
	model.save(save_at)

if __name__ == '__main__':
	main()