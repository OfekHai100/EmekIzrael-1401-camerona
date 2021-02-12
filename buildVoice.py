from gtts import gTTS 

text = "please wear a mask"
save_at = "voices/pwam.mp3"

lan = 'en'

speech = gTTS(text = text, lang = lan, slow = False)

speech.save(save_at)