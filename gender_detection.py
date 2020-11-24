from tensorflow.keras import models
import numpy as np

class genderDetector():
	def __init__(self, con_th = 0.5, model_path = "models/gender.h5"):
		self.model = models.load_model(model_path)
		self.conf_th = con_th

	def checkNonmaskers(self, face):
		check = []
		for i in range(0, len(faces)):
			check.append(faces[i][2])
		check = np.array(check)
		predictions = self.model.predict(check)
		toRet = []
		for i in range(0, len(check)):
			print(predictions[i])
			if predictions[i] > self.conf_th:
				toRet.append(true)
			else:
				toRet.append(false)
		return toRet
