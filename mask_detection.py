from tensorflow.keras import models
import numpy as np

class maskDetector():
	def __init__(self, con_th = 0.8, model_path = "models/mask-detection.h5"):
		"""
		this method in the c'tor of the class
		loading the model
		input: min conffidence and model path
		output: non
		"""
		self.model = models.load_model(model_path)#loading the model
		self.conf_th = con_th

	def checkNonmaskers(self, faces):
		"""
		this method checks if given faces wear mask or not
		input: array of faces and faces locations
		output: an array that contains all faces locations and an array that contains all faces
		"""
		check = []
		for i in range(0, len(faces)):#getting only the faces from the array
			check.append(faces[i][2])
		check = np.array(check)
		predictions = self.model.predict(check)#predictinng the output for al the faces
		toRet = []
		toRet2 = []
		for i in range(0, len(check)):#checking all the predictions
			print(predictions[i])
			if 1 - predictions[i] > self.conf_th:#checking if the prediction is over the min limit
				toRet.append([faces[i][0], faces[i][1]])#adding the location to an array
				toRet2.append(check[i])#adding the face to an array
		return toRet, np.array(toRet2)