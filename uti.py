from tensorflow.keras import models
import numpy as np
import cv2
from time import time, sleep
import numpy as np

class People():
	def __init__(self):
		self.faces = []
		self.people = []

class Person():
	def __init__(self, startPoint, endPoint):
		self.start_pnt = startPoint
		self.end_pnt = endPoint
		self.gender = False
		self.glass = False
		self.sunglass = False
		self.beard = False