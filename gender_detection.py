from tensorflow.keras import models
import numpy as np

class genderDetector():
	def __init__(self, model_path = "models/gender-detection.h5"):
		self.model = models.load_model(model_path)

	def checkGenders(self, faces):
		predictions = self.model.predict(faces)
		toRet = []
		for i in range(0, len(predictions)):
			print(predictions[i])
			if predictions[i] > 0.5:
				toRet.append(True)
			else:
				toRet.append(False)
		return toRet
