import tensorflow as tf

saved_at = "models/mask.h5"
save_at = "models/mask.tflite"

model = tf.keras.models.load_model(saved_at)

converter = tf.lite.TFLiteConverter.from_keras_model(model)
converter.optimizations = [tf.lite.Optimize.DEFAULT]
tflite_model = converter.convert()
open(save_at, "wb").write(tflite_model)