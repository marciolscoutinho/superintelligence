import tensorflow as tf
from tensorflow.keras import layers

class TransformerModel(tf.keras.Model):
    def __init__(self, input_dim, output_dim, num_heads, ff_dim, num_layers):
        super(TransformerModel, self).__init__()
        self.embedding = layers.Embedding(input_dim=input_dim, output_dim=output_dim)
        self.transformer_blocks = [layers.MultiHeadAttention(num_heads=num_heads, key_dim=output_dim) for _ in range(num_layers)]
        self.ffn_layers = [layers.Dense(ff_dim, activation="relu") for _ in range(num_layers)]
        self.output_layer = layers.Dense(output_dim)

    def call(self, x):
        x = self.embedding(x)
        for i in range(len(self.transformer_blocks)):
            attn_output = self.transformer_blocks[i](x, x)
            x = attn_output + x
            x = self.ffn_layers[i](x) + x
        return self.output_layer(x)
