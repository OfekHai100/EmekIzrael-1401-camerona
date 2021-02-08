from Coffe import *
from classifiers import *
import datetime
import time

PLAY_FROM = 0#vid.mp4

ATT_LIMIT = 10

FACES_CONF_TH = 0.9
MASK_CONF_TH = 0.9

BOUNDING_BOX_COLOR = (0,0,255)
TEXT_COLOR = (255,255,255)
TEXT_COLOR_OVER_LIMIT = (0,0,255)
LINE_THICKNESS = 2
FONT = cv2.FONT_HERSHEY_SIMPLEX

MASK_PATH = 'models/mask.h5'
GENDER_PATH = 'models/gender.h5'
GLASS_PATH = 'models/glass.h5'
BEARD_PATH = 'models/beard.h5'

def playVoices(people):
	cnt = 0
	while cnt < len(people.people):
		cnt += 1
		
def tooMuchPeople(frame):
	filename = "over_limit/" + str(datetime.datetime.now()).replace(':', '-').replace('.', '-') + ".jpg"
	#play voice that says there are too many people
	cv2.imwrite(filename, frame)

def main():
	#loading models
	face_detector = Coffe(FACES_CONF_TH)
	mask_classifier = maskClassifier(MASK_CONF_TH, MASK_PATH)
	metadata_models = metaData(GLASS_PATH, GENDER_PATH, BEARD_PATH)

	cap = cv2.VideoCapture(PLAY_FROM)
	while True:
		work, frame = cap.read()
		if not work:
			break
		people = face_detector.detectFaces(frame)
		if len(people.faces) > 0:
			if len(people.faces) > ATT_LIMIT:
				tooMuchPeople(frame)
			people = mask_classifier.checkMask(people)
			if len(people.faces) > 0:
				people = metadata_models.getMetaData(people)
				playVoices(people)
	cap.release()
	cv2.destroyAllWindows()

if __name__ == '__main__':
	main()