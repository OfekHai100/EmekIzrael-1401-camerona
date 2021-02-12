from uti import *

class ModelData():
	def __init__(self, model_path):
		self.model = tf.lite.Interpreter(model_path=model_path)
		self.input_tensor_index = self.model.get_input_details()[0]['index']
		self.output_tensor_index = self.model.get_output_details()[0]['index']
		self.model.allocate_tensors()

	def modelPredict(self, face):
		self.model.set_tensor(self.input_tensor_index, face)
		self.model.invoke()
		prediction = self.model.get_tensor(self.output_tensor_index)
		return prediction

class metaData():
	def __init__(self,
		mask_path="models/mask.tflite", mask_con_th = 0.8,
		glass_path = "models/glass.tflite",
		gender_path = "models/gender.tflite",
		beard_path = "models/beard.tflite"):
		#index 0 - sunglass
		#index 1 - glass
		#index 2 - nothing
		self.glass = ModelData(glass_path)
		#0 - female
		#1 - male
		self.gender = ModelData(gender_path)
		#0 - no beard
		#1 - beard
		self.beard = ModelData(beard_path)
		#0 - no mask
		#1 - mask
		self.mask = ModelData(mask_path)
		self.mask_th = mask_con_th

	def getMetaData(self, people):
		to_ret = People()
		j = 0
		for i in range(0, len(people.faces)):
			face = people.faces[i]
			#checking mask
			prediction = self.mask.modelPredict(face)[0][0]
			if 1 - prediction > self.mask_th:
				to_ret.faces.append(people.faces[i])
				to_ret.people.append(people.people[i])
				#checking beard
				prediction = self.beard.modelPredict(face)[0][0]
				to_ret.people[j].beard = prediction > 0.5
				#checking gender
				prediction = self.gender.modelPredict(face)[0][0]
				to_ret.people[j].gender = prediction > 0.5
				#checking glass
				prediction = self.glass.modelPredict(face)[0]
				index = np.argmax(prediction)
				to_ret.people[j].sunglass = index == 0
				to_ret.people[j].glass = index == 1

				j += 1
		return to_ret