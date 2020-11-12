from Coffe import *
from mask_detection import *

FACES_CONF_TH = 0.9
MASK_CONF_TH = 0.8

def drawNoMasks(no_maskers, img):
	for no_mask in no_maskers:
		color = (0,0,255)
		thick = 2
		cv2.rectangle(img, no_mask[0], no_mask[1], color, thick)

def main():
	model_path = 'models/mask-detection.h5'
	mask_detector = maskDetector(MASK_CONF_TH, model_path)
	face_detector = Coffe(FACES_CONF_TH)
	cap = cv2.VideoCapture(0)
	while True:
		faces = []
		faces_noMask = []
		_, frame = cap.read()
		faces = face_detector.detect_faces(frame)
		if len(faces) > 0:
			faces_noMask = mask_detector.checkNonmaskers(faces)
			drawNoMasks(faces_noMask, frame)
		cv2.imshow('show', frame)
		if cv2.waitKey(1) & 0xFF == ord('q'):
			break
	cap.release()
	cv2.destroyAllWindows()

if __name__ == '__main__':
	main()