# Convolutional Neural Networks Training and Logits Saving

## Introduction
This repository contains all scripts needed to train neural networks (ResNet, DenseNet, Wide ResNet etc) and to generate logits for calibration. There are additional scripts for ResNet110, DenseNet40 and WideNet32 to generate weights and logits for every epoch.

## Structure
Structure of the repository:
- [train_lenet_cifar](train_lenet_cifar) - Training scripts for LeNet using CIFAR-10/100 data sets.
- [train_resnet_cifar](train_resnet_cifar) - Training scripts for ResNet using CIFAR-10/100 data sets.
- [train_resnet_densenet](train_resnet_densenet) - Training scripts for DenseNet using CIFAR-10/100 data sets.
- [train_resnet_sd](train_resnet_sd) - Training scripts for ResNet SD using CIFAR-10/100 and SVHN data sets.
- [train_resnet_wide](train_resnet_wide) - Training scripts for Wide ResNet using CIFAR-10/100 data sets.
- [utility](utility) - Scripts for evaluation, logit generation and to pickle logits.

## Requirements
- Python (3.7)
- Keras (>=2.2.4)
- Tensorflow (>=1.4.1)

## Datasets
Following datasets were used:
- CIFAR-10/100 - more information on https://www.cs.toronto.edu/~kriz/cifar.html
- SVHN - more information on http://ufldl.stanford.edu/housenumbers/

## Models
Following models were used and trained:
- ResNet - based on paper ["Deep Residual Learning for Image Recognition"](https://arxiv.org/abs/1512.03385)
- ResNet (SD) - based on paper ["Deep Networks with Stochastic Depth"](https://arxiv.org/abs/1603.09382)
- Wide ResNet - based on paper ["Wide Residual Networks"](https://arxiv.org/abs/1605.07146)
- DenseNet - based on paper ["Densely Connected Convolutional Networks"](https://arxiv.org/abs/1608.06993)
- LeNet - based on paper ["Gradient-based learning applied to document recognition"](https://ieeexplore.ieee.org/document/726791/)

The hyperparameters and data preparation suggested by the authors of the papers were used to train the models, except for LeNet.


## Author
	Markus Kängsepp, University of Tartu
