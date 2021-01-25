from Coffe import *
from mask_detection import *
from gender_detection import *
from glass_classification import *
from use_speakers import *
import datetime
import time

ATT_LIMIT = 1

FACES_CONF_TH = 0.9
MASK_CONF_TH = 0.9

BOUNDING_BOX_COLOR = (0,0,255)
TEXT_COLOR = (255,255,255)
TEXT_COLOR_OVER_LIMIT = (0,0,255)
LINE_THICKNESS = 2
FONT = cv2.FONT_HERSHEY_SIMPLEX

MASK_PATH = 'models/mask-detection.h5'
GENDER_PATH = 'models/gender-detection.h5'
GLASS_PATH = 'models/glass-model.h5'

def drawNoMasks(faces, img):
	cnt = 1
	txt_clr = TEXT_COLOR
	for face in faces:
		#play(face.gender) - play sound with face features
		cv2.rectangle(img, face.start_pnt, face.end_pnt, BOUNDING_BOX_COLOR, LINE_THICKNESS)
		text = 'F'
		if face.gender:
			text = 'M'
		if face.glass:
			text += ' G'
		if face.sunglass:
			text += ' SG'
		if cnt > ATT_LIMIT:
			txt_clr = TEXT_COLOR_OVER_LIMIT
		text += ' ' + str(cnt)
		cnt+=1
		cv2.putText(img, text, (face.start_pnt[0], face.end_pnt[1]), FONT, 1, txt_clr, LINE_THICKNESS)
	#play sound saying 'please wear a mask'
		
def tooMuchPeople(frame):
	filename = "over_limit/" + str(datetime.datetime.now()).replace(':', '-').replace('.', '-') + ".jpg"
	cv2.imwrite(filename, frame)
	#play voice that says there are too many people

def main():
	mask_detector = maskDetector(MASK_CONF_TH, MASK_PATH)
	face_detector = Coffe(FACES_CONF_TH)
	gender_detector = genderDetector(GENDER_PATH)
	glass_classifier = glassClassifier(GLASS_PATH)
	cap = cv2.VideoCapture(0)
	
	while True:
		_, frame = cap.read()
		faces = face_detector.detectFaces(frame)
		if len(faces) > 0:
			if len(faces) > ATT_LIMIT:
				tooMuchPeople(frame)
			faces = mask_detector.checkNonmaskers(faces)
			if len(faces) > 0:
				faces = gender_detector.checkGenders(faces)
				faces = glass_classifier.checkGlassType(faces)
				drawNoMasks(faces, frame)
		cv2.imshow('show', frame)
		if cv2.waitKey(1) & 0xFF == ord('q'):
			break
	cap.release()
	cv2.destroyAllWindows()

if __name__ == '__main__':
	main()