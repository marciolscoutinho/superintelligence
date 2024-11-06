from tensorflow.keras import layers, Model

def create_pattern_recognition_model(input_shape=(None, 128)):
    inputs = layers.Input(shape=input_shape)
    x = layers.LSTM(128, return_sequences=True)(inputs)
    x = layers.LSTM(64)(x)
    x = layers.Dense(64, activation="relu")(x)
    outputs = layers.Dense(10, activation="softmax")(x)
    return Model(inputs, outputs)
