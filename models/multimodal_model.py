from tensorflow.keras import layers, Model

def create_multimodal_model(vocab_size=10000, text_embed_dim=128):
    text_input = layers.Input(shape=(None,), dtype="int32", name="text")
    x = layers.Embedding(vocab_size, text_embed_dim)(text_input)
    x = layers.GlobalAveragePooling1D()(x)
    
    image_input = layers.Input(shape=(224, 224, 3), name="image")
    y = layers.Conv2D(32, 3, activation="relu")(image_input)
    y = layers.GlobalAveragePooling2D()(y)
    
    combined = layers.concatenate([x, y])
    z = layers.Dense(64, activation="relu")(combined)
    z = layers.Dense(10, activation="softmax")(z)
    
    return Model(inputs=[text_input, image_input], outputs=z)
