from gtts import gTTS 

text = "with"
save_at = "voices/with.mp3"

lan = 'en'

speech = gTTS(text = text, lang = lan, slow = False)

speech.save(save_at)