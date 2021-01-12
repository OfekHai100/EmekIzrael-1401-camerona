from uti import *

class maskDetector():
	def __init__(self, con_th = 0.8, model_path = "models/mask-detection.h5"):
		self.model = models.load_model(model_path)
		self.conf_th = con_th

	def checkNonmaskers(self, faces):
		#getting only the faces
		check = []
		for face in faces:
			check.append(face.face)
		check = np.array(check)
		#checking the faces
		predictions = self.model.predict(check)
		toRet = []
		for i in range(0, len(check)):
			if 1 - predictions[i] > self.conf_th:
				toRet.append(faces[i])#adding faces without masks
		return toRet