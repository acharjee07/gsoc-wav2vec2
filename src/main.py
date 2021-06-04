# __author__ = "Vasudev Gupta"
# __author_email__ = "7vasudevgupta@gmail.com"

"""Run this script to launch training"""

import tensorflow as tf
from trainer import Trainer
from wav2vec2 import Wav2Vec2ForCTC

MODEL_ID = "wav2vec2-base"


if __name__ == '__main__':

    model = Wav2Vec2ForCTC.from_pretrained(MODEL_ID)
    tr_dataset: tf.data.Dataset
    val_dataset: tf.data.Dataset

    T = Trainer(lr=2e-4, max_epochs=2)
    optimizer = tf.keras.optimizers.Adam(lr=T.lr)
    T.setup(model, optimizer)

    # let's do training
    T.train(tr_dataset, val_dataset)