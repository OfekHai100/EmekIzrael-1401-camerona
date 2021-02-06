from uti import *

class maskClassifier():
	#mask - 1
	#no mask - 0
	def __init__(self, con_th = 0.8, model_path = "models/mask.h5"):
		self.model = models.load_model(model_path)
		self.conf_th = con_th

	def checkMask(self, people):
		check = np.array(people.faces)
		predictions = self.model.predict(check)

		toRet = People()
		for i in range(0, len(predictions)):
			if 1 - predictions[i] > self.conf_th:
				toRet.faces.append(people.faces[i])
				toRet.people.append(people.people[i])
		return toRet

class glassClassifier():
	#index 0 - sunglass
	#index 1 - glass
	#index 2 - nothing
	def __init__(self, model_path = "models/glass-model.h5"):
		self.model = models.load_model(model_path)

	def checkGlassType(self, people):
		check = np.array(people.faces)
		predictions = self.model.predict(check)
		for i in range(0, len(predictions)):
			index = np.argmax(predictions[i])
			people.people[i].sunglass = index == 0
			people.people[i].glass = index == 1
		return people

class genderClassifier():
	#1 - male
	#2 - female
	def __init__(self, model_path = "models/gender.h5"):
		self.model = models.load_model(model_path)

	def checkGenders(self, people):
		check = np.array(people.faces)
		predictions = self.model.predict(check)
		for i in range(0, len(predictions)):
			people.people[i].gender = predictions[i] > 0.5
		return people

class beardClassifier():
	def __init__(self, model_path = "models/beard.h5"):
		self.model = models.load_model(model_path)

	def checkBeard(self, people):
		check = np.array(people.faces)
		predictions = self.model.predict(check)
		for i in range(0, len(predictions)):
			people.people[i].beard = predictions[i] > 0.5
		return people