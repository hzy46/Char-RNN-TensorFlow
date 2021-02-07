import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()
from read_utils import TextConverter
from model import CharRNN
import os
from IPython import embed

import warnings
warnings.filterwarnings('ignore')

FLAGS = tf.flags.FLAGS

tf.flags.DEFINE_integer('lstm_size', 128, 'size of hidden state of lstm')
tf.flags.DEFINE_integer('num_layers', 2, 'number of lstm layers')
tf.flags.DEFINE_boolean('use_embedding', False, 'whether to use embedding')
tf.flags.DEFINE_integer('embedding_size', 128, 'size of embedding')
tf.flags.DEFINE_string('converter_path', '', 'model/name/converter.pkl')
tf.flags.DEFINE_string('checkpoint_path', '', 'checkpoint path')
tf.flags.DEFINE_string('start_string', '', 'use this string to start generating')
tf.flags.DEFINE_integer('max_length', 30, 'max length to generate')

def remove_return(s):
    result = []
    for i in s:
        if i == "\r":
            result.append("\\r")
        elif i == "\n":
            result.append("\\n")
        else:
            result.append(i)
    return str().join(result)

def main(_):
    FLAGS.start_string = FLAGS.start_string
    converter = TextConverter(filename=FLAGS.converter_path)
    if os.path.isdir(FLAGS.checkpoint_path):
        FLAGS.checkpoint_path =\
            tf.train.latest_checkpoint(FLAGS.checkpoint_path)

    model = CharRNN(converter.vocab_size, sampling=True,
                    lstm_size=FLAGS.lstm_size, num_layers=FLAGS.num_layers,
                    use_embedding=FLAGS.use_embedding,
                    embedding_size=FLAGS.embedding_size)

    model.load(FLAGS.checkpoint_path)

    start = converter.text_to_arr(FLAGS.start_string)
    arr = model.predict(FLAGS.max_length, start, converter.vocab_size, 10)
    for c, p in arr:
        prediction = converter.arr_to_text(c)
        prediction = remove_return(prediction)

        # 如果有中文字生成，请将 {1:^14} 改为 {1:{4}^14} 以修复对齐问题。
        # {1:^14}中的 14 随着生成的字符数量而定，一般可以设为字符数+4

        print("{0} -> {1:^14} {2} {3}".format(FLAGS.start_string, prediction, "probability:", p, chr(12288)))


if __name__ == '__main__':
    tf.app.run()
