# 🐱🐶 Cat vs. Dog Image Classification using CNN

A Deep Learning project that trains a Convolutional Neural Network (CNN) using TensorFlow/Keras to accurately distinguish between images of cats and dogs.

---

## 📌 Features

- **Custom CNN Architecture:** Sequential convolutional and dense layers for binary image classification.
- **Model Training Pipeline:** Preprocesses image data, trains the network, and exports saved weights.
- **Inference Script:** Evaluates and predicts outcomes on custom test images.

---

## 📁 Repository Structure

```text
├── archive/              # Dataset directory containing image classes
├── cat_dog_model.h5      # Trained Keras CNN model weights
├── cat_dog_test.py       # Python script for model testing & inference
├── cat_dog_train.py      # Python script to build & train the CNN
└── README.md             # Project documentation
