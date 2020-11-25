import cv2
import numpy as np

class Coffe():
	def __init__(self, con_th = 0.8):
		"""
		this is the C'tor, it loads and saves all the class nesecary data
		input: min conffidence for finding a face
		output: non
		"""
		prototxtPath = "models/face-detection-weights.prototxt"
		weightsPath = "models/face-detection-model.caffemodel"
		self.net = cv2.dnn.readNet(prototxtPath, weightsPath)#loading the model
		self.conf_th = con_th

	def detect_faces(self, img):
		"""
		this function detects faces in a given image
		input: the image
		output: an array of faces and the location of the faces
		"""
		(h, w) = img.shape[:2]

		blob = cv2.dnn.blobFromImage(img, 1.0, (300, 300), (104.0, 177.0, 123.0))#preproccesing the  image

		self.net.setInput(blob)
		detections = self.net.forward()[0][0]#getting the predictions for the faces

		bboxes = []

		for i in range(0, detections.shape[0]):#extracting all the locations
			confidence = detections[i][2]
			if confidence > self.conf_th:
				box = detections[i, 3:7] % np.array([1,1,1,1]) * np.array([w, h, w, h])
				(startX, startY, endX, endY) = box.astype("int")
				(startX, startY) = (max(0, startX), max(0, startY))
				(endX, endY) = (min(w - 1, endX), min(h - 1, endY))
				bboxes.append((startX, startY, endX, endY))

		toRet = []

		for box in bboxes:#exstracting all the faces from the image based on thr locations
			start_point = (int(box[0]),int(box[1]))
			end_point = (int(box[2]),int(box[3]))
			if end_point[0] <= start_point[0]:
				end_point = (w, end_point[1])
			if end_point[1] <= start_point[1]:
				end_point = (end_point[0], h)
			face = img[start_point[1]:end_point[1], start_point[0]:end_point[0]]#exstracting the face
			face = cv2.resize(face, (64,64))/255#normalizing the faces data
			add = [start_point, end_point, face]#array of start location, end location and the face
			toRet.append(add)#adding the locations and face
		return toRet