# Fixing the Train-Test Resolution Discrepancy implementation
This is an implementation of the research paper ["fixing the train test resolution discrepancy"](https://arxiv.org/pdf/1906.06423.pdf) for MIC rescon.

## Introduction

The paper Fixing the Train-Test Resolution Discrepancy talks about how reducing the train resolution and increasing the test resolution has an improvement on a given cnn model’s performance for classification purposes. However, there is a direct clash with the way the model interprets images after training on cropped images, and so needs minor and computationally inexpensive finetuning at the end of the convolutional blocks to adapt to that change during higher test resolutions to avoid a domain shift. 

To experiment for yourself, run the notebooks in the binary classification and the multiclass classification directories. Use the compression script on the dataset (link provided below) for crossvalidating the results across both notebooks.

The experiments were conducted on a local machine running a NVidia GTX 1050Ti, and validated over Google Colab running a NVIDIA Tesla K80

<hr>

## Requirements

tensorflow==2.4.0  
opencv_python==4.5.1.48  
numpy==1.19.2  
matplotlib==3.3.2  
compress==0.0.3  
keras==2.4.3  
Pillow==8.1.0  

<hr>

## Explanation and Intuition for the Math

The paper first makes the argument that for best results, the distribution for train and test should be the same. However most accuracy improvement techniques focus changes in only one or the other, resulting in a domain shift. With different regions of concentration or RoCs for train and test time, the distribution of data is skewed. This is explained by the simple physics problem, which is the apparent size of objects. When performing classification, the model must learn from the data. But if standard preprocessing techniques are followed, then the train time apparent object size is much larger than the test, thus causing a distribution shift in the data.

<img src = "https://github.com/GAmuzak/fix-res/blob/main/multiclass/graphs/example.png">

The solution is to either reduce the resolution of the train image, or increase the resolution of the test image, or both in moderate amounts, so as to make use of the individual gains made in each domain for improving accuracies therein.

The math shows the relation between the apparent sizes of the train size and the test size in section 3.1, with the conclusion that the coefficient of proportionality is alpha, where alpha is supposed to be as close to one as possible, but is normally around 0.8 for popular architectures such as AlexNet.

The essence of the paper is to fix this, and to make a minor finetuning change for the minor change in the network’s understanding of the differing overall resolutions in order to maintain the performance of the network.


We tried it on two models:
1. A CNN Binary Classifier
2. A CNN Multiclass Classifier

<hr>

## Binary Classifier

Dataset : ["https://www.kaggle.com/techsash/waste-classification-data"](https://www.kaggle.com/techsash/waste-classification-data)

The model is used for classifying image of waste into either Recyclable or Organic

### Results:
<img src="https://github.com/GAmuzak/fix-res/blob/main/binary_classification/results/table.png" height="800"/>

<img src="https://github.com/GAmuzak/fix-res/blob/main/binary_classification/results/table2.png" height="750"/>

**Original Model**

![original](https://github.com/GAmuzak/fix-res/blob/main/binary_classification/results/original.png)

**Without augmentation:**

Base Model

![base](https://github.com/GAmuzak/fix-res/blob/main/binary_classification/results/no%20aug%20base%20model.png)

On fine tuning

![fine tuned](https://github.com/GAmuzak/fix-res/blob/main/binary_classification/results/no%20aug%20fine%20tuning%20same.png)

**With augmentation:**

Base Model

![base](https://github.com/GAmuzak/fix-res/blob/main/binary_classification/results/with%20aug%20base%20model.png)

On fine tuning

![fine tuned](https://github.com/GAmuzak/fix-res/blob/main/binary_classification/results/with%20aug%20fine%20tuning%20half.png)

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

![original](https://github.com/GAmuzak/fix-res/blob/main/multiclass/graphs/original.png)

**Without augmentation:**

Base Model

![base](https://github.com/GAmuzak/fix-res/blob/main/multiclass/graphs/only%20crops_base.png)

On fine tuning

![fine tuned](https://github.com/GAmuzak/fix-res/blob/main/multiclass/graphs/crop_finetune.png)

**With augmentation:**

Base Model

![base](https://github.com/GAmuzak/fix-res/blob/main/multiclass/graphs/aug_base.png)

On fine tuning

![fine tuned](https://github.com/GAmuzak/fix-res/blob/main/multiclass/graphs/aug_fine.png)

<hr>

## Related Work -- Fixing the train-test resolution discrepancy by Image Compression using SVD:

The idea here was to see if compression of the images had a similar effect or not to cropping the image as per what the paper suggested. We have found that on compressing the images, the validation and test accuracy improves.

### Table:

<img src = "https://github.com/GAmuzak/fix-res/blob/main/image_compression/table/comparisontable.png">

### Results:

Original Dataset

![original](https://github.com/GAmuzak/fix-res/blob/main/image_compression/graphs/original.jpeg)

Compressed Images

![compressed](https://github.com/GAmuzak/fix-res/blob/main/image_compression/graphs/finetune.jpeg)
