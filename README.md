# FMNISTpreparer

Why did you developed another (F)MNIST converter to CSV? 
- Because I needed to separate the labels from the actual dataset

Can I use the fashion MNIST data set too?
- that's what the F in FMNIST stands for

## Usage

0. get the [MNIST](#http://yann.lecun.com/exdb/mnist/) or [FMNIST](#https://github.com/zalandoresearch/fashion-mnist#get-the-data) dataset

1. use the [original converter](#https://pjreddie.com/projects/mnist-in-csv/) from darknet
```
python3 darknet_fmnist_to_csv.py
```

2. use the advanced converter from this reposiory to distinguish between the data and the labels
```
python3 better_fmnist_to_csv.py
```
