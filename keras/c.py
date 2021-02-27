from tensorflow.keras import models

model_path = "models/gender.h5"

m = models.load_model(model_path)

m.summary()

for layer in m.layers:
	try:
		print(layer.filters)
		print(layer.kernel_size)
		print(layer.strides)
	except:
		continue