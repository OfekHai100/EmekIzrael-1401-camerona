from tensorflow.keras import models
import numpy as np
import cv2
from time import time, sleep
import numpy as np

class Person():
	def __init__(self, face, startPoint, endPoint):
		self.face = face
		self.start_pnt = startPoint
		self.end_pnt = endPoint
		self.gender = False
		self.glass = False
		self.sunglass = False