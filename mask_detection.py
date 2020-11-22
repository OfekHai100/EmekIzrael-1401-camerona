from tensorflow.keras import models
import numpy as np

class maskDetector():
	def __init__(self, con_th = 0.8, model_path = "models/mask-detection.h5"):
		self.model = models.load_model(model_path)
		self.conf_th = con_th

	def checkNonmaskers(self, faces):
		check = []
		for i in range(0, len(faces)):
			check.append(faces[i][2])
		check = np.array(check)
		predictions = self.model.predict(check)
		toRet = []
		for i in range(0, len(check)):
			print(predictions[i])
			if 1 - predictions[i] > self.conf_th:
				toRet.append([faces[i][0], faces[i][1]])
		return toRet