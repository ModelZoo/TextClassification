from model_zoo.model import BaseModel
import tensorflow as tf


class DenseModel(BaseModel):
    def __init__(self, config):
        super(DenseModel, self).__init__(config)
        self.embedding = tf.keras.layers.Embedding(config['vocab_size'], config['embedding_size'])
        self.pool = tf.keras.layers.GlobalAveragePooling1D()
        self.dense1 = tf.keras.layers.Dense(16, activation=tf.nn.relu)
        self.dense2 = tf.keras.layers.Dense(1, activation=tf.nn.sigmoid)
    
    def call(self, inputs, training=None, mask=None):
        o = self.embedding(inputs)
        o = self.pool(o)
        o = self.dense1(o)
        o = self.dense2(o)
        return o
    
    def init(self):
        self.compile(optimizer=tf.train.AdamOptimizer(),
                     loss='binary_crossentropy',
                     metrics=['accuracy'])
