from Coffe import *
from mask_detection import *
from gender_detection import *

#confidence mins
FACES_CONF_TH = 0.9
MASK_CONF_TH = 0.9

#image data consts
BOUNDING_BOX_COLOR = (0,0,255)
TEXT_COLOR = (255,255,255)
LINE_THICKNESS = 2
FONT = cv2.FONT_HERSHEY_SIMPLEX

def drawNoMasks(no_maskers, img):
	"""
	this function draws a rectangle around each location
	it is given and writes next to
	it the gender of the person in the rectangle
	input: an array of locations and True or False
	output: non
	"""
	for no_mask in no_maskers:#checking all the given locations and True or False values
		cv2.rectangle(img, no_mask[0], no_mask[1], BOUNDING_BOX_COLOR, LINE_THICKNESS)#drawing the rectangle around a face
		loc = (no_mask[0][0], no_mask[1][1])#building location for text
		text = 'F'
		if no_mask[2]:
			text = 'M'
		cv2.putText(img, text, loc, FONT, 1, TEXT_COLOR, LINE_THICKNESS)#writing the text in the rectngle

def main():
	mask_detector = maskDetector(MASK_CONF_TH)#loading the mask detector
	face_detector = Coffe(FACES_CONF_TH)#loading the face detector
	gender_detector = genderDetector()#loading the gender detector
	cap = cv2.VideoCapture(0)
	while True:
		faces = []
		faces_noMask = []
		_, frame = cap.read()
		faces = face_detector.detect_faces(frame)#detecting all the faces in an image
		if len(faces) > 0:
			faces_loc, faces = mask_detector.checkNonmaskers(faces)#getting all the faces without masks
			if len(faces) > 0:
				faces_loc = gender_detector.checkGenders(faces, faces_loc)#getting the gender of all the mask-less faces
				drawNoMasks(faces_loc, frame)#drawing the rectangle and writing the gender of each face without mask
		cv2.imshow('show', frame)
		if cv2.waitKey(1) & 0xFF == ord('q'):
			break
	cap.release()
	cv2.destroyAllWindows()

if __name__ == '__main__':
	main()