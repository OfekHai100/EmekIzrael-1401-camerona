from tensorflow.keras import models
import numpy as np

class genderDetector():
	def __init__(self, model_path = "models/gender-detection.h5"):
		self.model = models.load_model(model_path)

	def checkGenders(self, faces, faces_loc):
		predictions = self.model.predict(faces)
		for i in range(0, len(predictions)):
			print(predictions[i])
			faces_loc[i].append(predictions[i] < 0.5)
		return faces_loc
