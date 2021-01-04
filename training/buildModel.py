import tensorflow.keras as keras

def loadVGG16():
	model = keras.applications.VGG16(
		include_top = False,
		weights ="imagenet",
		input_tensor = None,
		input_shape = (256,256,3),
		pooling=None)
	return model

def buildModel():
	vgg16_backbone = loadVGG16()

	#making the backbone untrainable
	for layer in vgg16_backbone.layers:
		layer.trainable = False

	####SSD layers
	ssd = keras.layers.Conv2D(1024, 3, dilation_rate=6, activation='relu', padding='same', name = "ssd_block1_conv1")(vgg16_backbone.output)

	ssd = keras.layers.Conv2D(1024, 1, activation='relu', padding='same', name = "ssd_block2_conv1")(ssd)

	ssd = keras.layers.Conv2D(256, 1, activation='relu', padding='same', name = "ssd_block3_conv1")(ssd)
	ssd = keras.layers.Conv2D(512, 3, strides=2, activation='relu', padding='same', name = "ssd_block3_conv2")(ssd)

	ssd = keras.layers.Conv2D(128, 1, activation='relu', padding='same', name = "ssd_block4_conv1")(ssd)
	ssd = keras.layers.Conv2D(256, 3, strides=2, activation='relu', padding='same', name = "ssd_block4_conv2")(ssd)

	ssd = keras.layers.Conv2D(128, 1, activation='relu', padding='same', name = "ssd_block5_conv1")(ssd)
	ssd = keras.layers.Conv2D(256, 3, activation='relu', padding='same', name = "ssd_block5_conv2")(ssd)#

	ssd = keras.layers.Conv2D(128, 1, activation='relu', padding='same', name = "ssd_block6_conv1")(ssd)
	ssd = keras.layers.Conv2D(256, 3, activation='relu', padding='same', name = "ssd_block6_conv2")(ssd)#

	####output layers
	ssd = keras.layers.Flatten()(ssd)
	class_output = keras.layers.Dense(20, activation='sigmoid', name='output_class')(ssd)
	loc_output1 = keras.layers.Dense(40, activation='relu', name='output_loc_x')(ssd)
	loc_output2 = keras.layers.Dense(40, activation='relu', name='output_loc_y')(ssd)

	model = keras.Model(inputs=vgg16_backbone.input, outputs=[class_output, loc_output1, loc_output2])
	opt = keras.optimizers.Adam()
	model.compile(optimizer = opt, loss = ['binary_crossentropy', 'mean_squared_error', 'mean_squared_error'], metrics=["accuracy"])

	return model


def main():
	path = 'models\\base_model.h5'
	model = buildModel()
	print(model.summary())
	model.save(path)

if __name__ == '__main__':
	main()