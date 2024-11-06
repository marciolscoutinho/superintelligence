from tensorflow.keras import layers, Model

def create_audio_model(input_shape=(44100, 1)):
    inputs = layers.Input(shape=input_shape)
    x = layers.Conv1D(64, 3, activation="relu")(inputs)
    x = layers.MaxPooling1D(2)(x)
    x = layers.Conv1D(128, 3, activation="relu")(x)
    x = layers.GlobalAveragePooling1D()(x)
    x = layers.Dense(64, activation="relu")(x)
    outputs = layers.Dense(10, activation="softmax")(x)
    return Model(inputs, outputs)
