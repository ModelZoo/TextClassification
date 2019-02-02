import tensorflow as tf
from model_zoo.trainer import BaseTrainer
from tensorflow.python.keras.datasets import imdb
from tensorflow.python.keras.preprocessing.sequence import pad_sequences

tf.flags.DEFINE_integer('epochs', 50, 'Max epochs')
tf.flags.DEFINE_float('learning_rate', 0.001, 'Learning rate')
tf.flags.DEFINE_string('model_class', 'DenseModel', help='Model class name')
tf.flags.DEFINE_integer('vocab_size', 10000, help='Vocab size')
tf.flags.DEFINE_integer('embedding_size', 200, help='Embedding size')


class Trainer(BaseTrainer):
    
    def build_word_index(self):
        word_index = imdb.get_word_index()
        word_index = {k: (v + 3) for k, v in word_index.items()}
        word_index['<PAD>'] = 0
        word_index['<START>'] = 1
        word_index['<UNK>'] = 2
        word_index['<UNUSED>'] = 3
        return word_index
    
    def prepare_data(self):
        (x_train, y_train), (_, _) = imdb.load_data(num_words=self.flags.vocab_size)
        word_index = self.build_word_index()
        x_train = pad_sequences(x_train, maxlen=250, value=word_index['<PAD>'], padding='post')
        (x_train, x_eval) = x_train[:20000], x_train[20000:]
        (y_train, y_eval) = y_train[:20000], y_train[20000:]
        train_data, eval_data = self.build_generator(x_train, y_train), self.build_generator(x_eval, y_eval)
        return train_data, eval_data, len(x_train), len(x_eval)


if __name__ == '__main__':
    Trainer().run()
