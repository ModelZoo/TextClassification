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

Next we can use the best model to infer some results, run `infer.py`:

Output like this:

```
Text: <START> this is a crummy film a <UNK> to a genre of surprise ending movies and a genre that has been done so much better before the plot <UNK> along with a predictable ending yawn the characters are unlikeable and some are so unlikeable they are almost unwatchable matt dillon a fine intense actor is totally miscast here and is stiff and mannered the others are forgettable much of the dialog is <UNK> again a <UNK> trying to be witty i wouldn't hire the screenwriter to write my <UNK> list yes it's that bad <UNK> from misogynistic to just plain gross as in beyond frat house gross with so much real talent out there i'm really surprised this movie ever got made it shows the total lack of imagination of the office suits
Comment: 0
====================
Text: <START> i rented this film from because of the cover and title sounded intriguing this movie suffered because of the writing it needed more suspense the monsters needed more face time we needed them to have some sort of special power and definitely more oh sh moments the photography didn't bother me except for the scene where a re <UNK> blows up there were too many close ups but other than that the movie seemed to drag and the heroes didn't really work for their freedom overall i would say everyone put in a lot of time even the writers but this movie is definitely a below average rent br br there are definitely better picks i would recommend 1 or 2 over this pick
Comment: 1
```

Then we can get the emotion comment according to the source text.

result `1` means positive, result `0` means negative.

## License

MIT