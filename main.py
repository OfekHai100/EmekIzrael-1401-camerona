from Coffe import *
from mask_detection import *
from gender_detection import *
from use_speakers import *
import threading
import datetime
import time

FACES_CONF_TH = 0.9
MASK_CONF_TH = 0.9

BOUNDING_BOX_COLOR = (0,0,255)
TEXT_COLOR = (255,255,255)
LINE_THICKNESS = 2
FONT = cv2.FONT_HERSHEY_SIMPLEX

def drawNoMasks(no_maskers, img):
	for no_mask in no_maskers:
		cv2.rectangle(img, no_mask[0], no_mask[1], BOUNDING_BOX_COLOR, LINE_THICKNESS)
		loc = (no_mask[0][0], no_mask[1][1])
		text = 'F'
		if no_mask[2]:
			text = 'M'
			playing = threading.Thread(target=play, args=(True,))
		else:
			playing = threading.Thread(target=play, args=(False,))
		playing.start()
		#playing.join()
		cv2.putText(img, text, loc, FONT, 1, TEXT_COLOR, LINE_THICKNESS)
		#time.sleep(10)
		
		

def main():
	att_limit = int(open("attendance_limit.txt", "r").read())
	model_path = 'models/mask-detection.h5'
	mask_detector = maskDetector(MASK_CONF_TH, model_path)
	face_detector = Coffe(FACES_CONF_TH)
	gender_detector = genderDetector()
	cap = cv2.VideoCapture(0)
	timer = 10.0 #set one minute for saving image and using speakers
	
	while True:
		started_timing = time.perf_counter() #starting timer
		faces = []
		faces_noMask = []
		_, frame = cap.read()
		faces = face_detector.detect_faces(frame)
		text_color = TEXT_COLOR
		if len(faces) > 0:
			timer += time.perf_counter() - started_timing #calculating elapsed time from last 
			if len(faces) >= att_limit:
				text_color = (0, 0, 255)
				if timer >= 10: #10 seconds has passed
					filename = "over limit/" + str(datetime.datetime.now()).replace(':', '-').replace('.', '-') + ".jpg"
					cv2.imwrite(filename, frame)
					timer = 0.0 #reseting the timer
			faces_loc, faces = mask_detector.checkNonmaskers(faces)
			if len(faces) > 0:
				faces_loc = gender_detector.checkGenders(faces, faces_loc)
				cv2.putText(frame, str(len(faces)), (faces_loc[0][0][0], faces_loc[0][1][1] - 30), FONT, 1, text_color, LINE_THICKNESS)
				drawNoMasks(faces_loc, frame)
		cv2.imshow('show', frame)
		if cv2.waitKey(1) & 0xFF == ord('q'):
			break
	cap.release()
	cv2.destroyAllWindows()

if __name__ == '__main__':
	main()