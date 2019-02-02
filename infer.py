from tensorflow.python.keras.datasets import imdb
from tensorflow.python.keras.preprocessing.sequence import pad_sequences

from model_zoo.inferer import BaseInferer
import tensorflow as tf

tf.flags.DEFINE_string('checkpoint_name', 'model.ckpt', help='Model name')
tf.flags.DEFINE_integer('vocab_size', 10000, help='Vocab size')


class Inferer(BaseInferer):
    
    def build_word_index(self):
        """
        build word index for pad, start and other symbols
        :return:
        """
        word_index = imdb.get_word_index()
        word_index = {k: (v + 3) for k, v in word_index.items()}
        word_index['<PAD>'] = 0
        word_index['<START>'] = 1
        word_index['<UNK>'] = 2
        word_index['<UNUSED>'] = 3
        self.word_index = word_index
    
    def build_reverse_word_index(self):
        """
        build reverse word index
        :return:
        """
        reverse_word_index = dict([(value, key) for (key, value) in self.word_index.items()])
        self.reverse_word_index = reverse_word_index
    
    def build_text(self, seq):
        """
        seq to text
        :param seq:
        :return:
        """
        return ' '.join([self.reverse_word_index.get(i, '?') for i in seq])
    
    def build_comment(self, predict):
        """
        predict to comment
        :param predict:
        :return:
        """
        first = predict[0] if isinstance(predict, list) else predict
        return 1 if first > 0.5 else 0
    
    def prepare_data(self):
        """
        main prepare data
        :return:
        """
        (_, _), (x_test, y_test) = imdb.load_data(num_words=self.flags.vocab_size)
        # build word index and reverse word index
        self.build_word_index()
        self.build_reverse_word_index()
        self.x_test = x_test
        x_test = pad_sequences(x_test, maxlen=250, value=self.word_index['<PAD>'], padding='post')
        return x_test


if __name__ == '__main__':
    inf = Inferer()
    predicts = inf.run()
    for seq, predict in zip(inf.x_test, predicts):
        text = inf.build_text(seq)
        comment = inf.build_comment(predict)
        print('=' * 20)
        print('Text:', text)
        print('Comment:', comment)
