from tensorflow.keras import models
import numpy as np

class maskDetector():
	def __init__(self, model_path = "models/glass-model.h5"):
		self.model = models.load_model(model_path)

	def checkGlossType(self, faces):
		#getting only the faces
		check = []
		for face in faces:
			check.append(face.face)
		check = np.array(check)
		predictions = self.model.predict(check)
		for i in range(0, len(predictions)):
			index = np.argmax(predictions[i])
			faces[i].sunglass = (index == 0)
			faces[i].glass = (index == 1)
		return faces