import winsound
import time

def play(gender):
	if gender:
		winsound.PlaySound("voices/wear mask for male.wav", winsound.SND_FILENAME)
	else:
		winsound.PlaySound("voices/wear mask for male.wav", winsound.SND_FILENAME)