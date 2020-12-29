from tensorflow.keras import models
import numpy as np
import cv2
import os
import random

#with mask = 1
#without mask = 0

def main():
	model_path = 'models\\base_model.h5'
	model = models.load_model(model_path)

	print(model.summary())

if __name__ == '__main__':
	main()