from tensorflow.keras import models
import numpy as np

class genderDetector():
	def __init__(self, model_path = "models/gender-detection.h5"):
		"""
		this is the C'tor of the class
		input: model path
		output: non
		"""
		self.model = models.load_model(model_path)#loading the model

	def checkGenders(self, faces, faces_loc):
		"""
		this method checks the gender of given faces
		input: an array of faces and an array of their locations
		output: the location and gender of the faces
		"""
		predictions = self.model.predict(faces)#getting the predictions for all the faces
		for i in range(0, len(predictions)):#going through the predictions
			faces_loc[i].append(predictions[i] < 0.5)#adding the gender to the location of the face
		return faces_loc
