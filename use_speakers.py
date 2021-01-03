import winsound
import time

def play(gender):
	time.sleep(5)
	if gender:
		winsound.PlaySound("voices/wear mask for male.wav", winsound.SND_FILENAME)
	else:
		winsound.PlaySound("voices/wear mask for male.wav", winsound.SND_FILENAME)