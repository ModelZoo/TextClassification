# TextClassification

TextClassification Model implemented by [ModelZoo](https://github.com/ModelZoo/ModelZoo).


## Installation

Firstly you need to clone this repository and install dependencies with pip:

```
pip3 install -r requirements.txt
```

## Dataset

We use IMDB dataset for example.

## Usage

We can run this model like this:

```
python3 train.py
```

Outputs like this:

```
Epoch 1/50
624/625 [============================>.] - ETA: 0s - loss: 0.4417 - acc: 0.8072
Epoch 00001: saving model to checkpoints/model.ckpt
625/625 [==============================] - 22s 35ms/step - loss: 0.4413 - acc: 0.8074 - val_loss: 0.2309 - val_acc: 0.8750
Epoch 2/50
623/625 [============================>.] - ETA: 0s - loss: 0.2265 - acc: 0.9138 Epoch 00002: saving model to checkpoints/model.ckpt
Epoch 00002: saving model to checkpoints/model.ckpt-2
625/625 [==============================] - 24s 39ms/step - loss: 0.2264 - acc: 0.9139 - val_loss: 0.2734 - val_acc: 0.9062
Epoch 3/50
623/625 [============================>.] - ETA: 0s - loss: 0.1685 - acc: 0.9382
Epoch 00003: saving model to checkpoints/model.ckpt
625/625 [==============================] - 19s 31ms/step - loss: 0.1685 - acc: 0.9383 - val_loss: 0.2043 - val_acc: 0.8750
Epoch 4/50
622/625 [============================>.] - ETA: 0s - loss: 0.1314 - acc: 0.9549
Epoch 00004: saving model to checkpoints/model.ckpt
Epoch 00004: saving model to checkpoints/model.ckpt-4
625/625 [==============================] - 19s 30ms/step - loss: 0.1313 - acc: 0.9550 - val_loss: 0.6623 - val_acc: 0.7812
```

When finished, we can find two folders generated named `checkpoints` and `events`.

Go to `events` and run TensorBoard:

```
cd events
tensorboard --logdir=.
```

TensorBoard like this:

![](https://ws3.sinaimg.cn/large/006tNc79ly1fzslrtg6oyj31f70u0wgy.jpg)

There are training batch loss, epoch loss, eval loss.

And also we can find checkpoints in `checkpoints` dir.

It saved the best model named `model.ckpt` according to eval score, and it also saved checkpoints every 2 epochs.

## License

MIT