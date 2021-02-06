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

class metaData():
	def __init__(self, glass_path = "models/glass.h5", gender_path = "models/gender.h5", beard_path = "models/beard.h5"):
		#index 0 - sunglass
		#index 1 - glass
		#index 2 - nothing
		self.glass_model = models.load_model(glass_path)
		#0 - female
		#1 - male
		self.gender_model = models.load_model(gender_path)
		#0 - no beard
		#1 - beard
		self.beard_model = models.load_model(beard_path)

	def getMetaData(self, people):
		check = np.array(people.faces)
		glass_prediction = self.glass_model.predict(check)
		gender_prediction = self.gender_model.predict(check)
		beard_prediction = self.beard_model.predict(check)
		for i in range(0, len(check)):
			people.people[i].gender = gender_prediction[i] > 0.5
			people.people[i].beard = beard_prediction[i] > 0.5
			index = np.argmax(glass_prediction[i])
			people.people[i].sunglass = index == 0
			people.people[i].glass = index == 1
		return people