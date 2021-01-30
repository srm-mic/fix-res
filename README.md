# Fixing the Train-Test Resolution Discrepancy implementation
This is an implementation of the research paper ["fixing the train test resolution discrepancy"](https://arxiv.org/pdf/1906.06423.pdf) for MIC rescon.

## Introduction

The paper Fixing the Train-Test Resolution Discrepancy talks about how reducing the train resolution and increasing the test resolution has an improvement on a given cnn model’s performance for classification purposes. However, there is a direct clash with the way the model interprets images after training on cropped images, and so needs minor and computationally inexpensive finetuning at the end of the convolutional blocks to adapt to that change during higher test resolutions to avoid a domain shift. 

<hr>

We tried it on two models:
1. A CNN Binary Classifier
2. A CNN Multiclass Classifier

<hr>

## Binary Classifier

Dataset : ["https://www.kaggle.com/techsash/waste-classification-data"](https://www.kaggle.com/techsash/waste-classification-data)

The model is used for classifying image of waste into either Recyclable or Organic

### Results:
<img src="https://github.com/GAmuzak/fixing-train-test-resolution-discrepancy-implementation/blob/main/Binary%20Classification-%20FixRes/results/table.png" height="800"/>

<img src="https://github.com/GAmuzak/fixing-train-test-resolution-discrepancy-implementation/blob/main/Binary%20Classification-%20FixRes/results/table2.png" height="750"/>

**Original Model**

![original](https://github.com/GAmuzak/fixing-train-test-resolution-discrepancy-implementation/blob/main/Binary%20Classification-%20FixRes/results/original.png)

**Without augmentation:**

Base Model

![base](https://github.com/GAmuzak/fixing-train-test-resolution-discrepancy-implementation/blob/main/Binary%20Classification-%20FixRes/results/no%20aug%20base%20model.png)

On fine tuning

![fine tuned](https://github.com/GAmuzak/fixing-train-test-resolution-discrepancy-implementation/blob/main/Binary%20Classification-%20FixRes/results/no%20aug%20fine%20tuning%20same.png)

**With augmentation:**

Base Model

![base](https://github.com/GAmuzak/fixing-train-test-resolution-discrepancy-implementation/blob/main/Binary%20Classification-%20FixRes/results/with%20aug%20base%20model.png)

On fine tuning

![fine tuned](https://github.com/GAmuzak/fixing-train-test-resolution-discrepancy-implementation/blob/main/Binary%20Classification-%20FixRes/results/with%20aug%20fine%20tuning%20half.png)

<hr>

## Multiclass Classifier

Dataset : ["https://www.kaggle.com/asdasdasasdas/garbage-classification"](https://www.kaggle.com/asdasdasasdas/garbage-classification)

The Garbage Classification Dataset contains 6 classifications:
- cardboard (393)
- glass (491)
- metal (400)
- paper(584)
- plastic (472)
- trash (127)

### Results:

**Original Model**

![original](https://github.com/GAmuzak/fix-res/blob/main/Multiclass%20FixRes/graphs/original.png)

**Without augmentation:**

Base Model

![base](https://github.com/GAmuzak/fix-res/blob/main/Multiclass%20FixRes/graphs/only%20crops_base.png)

On fine tuning

![fine tuned](https://github.com/GAmuzak/fix-res/blob/main/Multiclass%20FixRes/graphs/crop_finetune.png)

**With augmentation:**

Base Model

![base](https://github.com/GAmuzak/fix-res/blob/main/Multiclass%20FixRes/graphs/aug_base.png)

On fine tuning

![fine tuned](https://github.com/GAmuzak/fix-res/blob/main/Multiclass%20FixRes/graphs/aug_fine.png)

<hr>

## Related Work -- Fixing the train-test resolution discrepancy by Image Compression using SVD:

We have found that on compressing the images, the validation and test accuracy improves.

### Table:

<img src = "https://github.com/GAmuzak/fix-res/blob/main/ImageCompression/table/comparisontable.png">

### Results:

Original Dataset

![original](https://github.com/GAmuzak/fix-res/blob/main/ImageCompression/graphs/original.jpeg)

Compressed Images

![compressed](https://github.com/GAmuzak/fix-res/blob/main/ImageCompression/graphs/finetune.jpeg)
