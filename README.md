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
...
```

It runs only 42 epochs and stopped early, because there are no more good evaluation results for 20 epochs.

When finished, we can find two folders generated named `checkpoints` and `events`.

Go to `events` and run TensorBoard:

```
cd events
tensorboard --logdir=.
```

TensorBoard like this:

![](https://ws4.sinaimg.cn/large/006tNbRwgy1fvxrcajse2j31kw0hkgnf.jpg)

There are training batch loss, epoch loss, eval loss.

And also we can find checkpoints in `checkpoints` dir.

It saved the best model named `model.ckpt` according to eval score, and it also saved checkpoints every 2 epochs.

Next we can predict using existing checkpoints and `infer.py`.

Now we've restored the specified model `model.ckpt-38` and prepared test data, outputs like this:

```python
[[ 9.637125 ]
 [21.368305 ]
 [20.898445 ]
 [33.832504 ]
 [25.756516 ]
 [21.264557 ]
 [29.069794 ]
 [24.968184 ]
 ...
 [36.027283 ]
 [39.06852  ]
 [25.728745 ]
 [41.62165  ]
 [34.340042 ]
 [24.821484 ]]
```

OK, we've finished restoring and predicting. Just so quickly.

## License

MIT