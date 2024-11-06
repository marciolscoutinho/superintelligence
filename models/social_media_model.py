from tensorflow.keras import layers, Model

def create_social_media_model(vocab_size=10000, embed_dim=128):
    inputs = layers.Input(shape=(None,), dtype="int32")
    x = layers.Embedding(vocab_size, embed_dim)(inputs)
    x = layers.Bidirectional(layers.LSTM(64))(x)
    x = layers.Dense(64, activation="relu")(x)
    outputs = layers.Dense(3, activation="softmax")
    return Model(inputs, outputs)
