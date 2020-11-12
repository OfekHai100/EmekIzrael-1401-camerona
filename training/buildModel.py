import tensorflow.keras as keras

def buildModel():
	model = keras.models.Sequential([
		keras.layers.Input(shape=[64,64,3]),
		keras.layers.Conv2D(64, (3,3), strides=(1,1), activation='relu', padding='same'),
		keras.layers.MaxPool2D(2),
		keras.layers.Conv2D(32, (3,3), strides=(1,1), activation='relu', padding='same'),
		keras.layers.MaxPool2D(2),
		keras.layers.Flatten(),
		keras.layers.Dense(32, activation="relu"),
		keras.layers.Dense(1, activation="sigmoid"),
	])

	model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
	return model

def main():
	path = 'models\\base_model.h5'
	model = buildModel()
	model.save(path)

if __name__ == '__main__':
	main()