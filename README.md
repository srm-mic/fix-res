# fixing-train-test-resolution-discrepancy-implementation
This is an implementation of the research paper ["fixing the train test resolution discrepancy"](https://arxiv.org/pdf/1906.06423.pdf) for MIC rescon

We tried it on two models:
1. A CNN Binary Classifier
2. A CNN Multiclass Classifier

## Binary Classifier

Dataset:["https://www.kaggle.com/techsash/waste-classification-data"](https://www.kaggle.com/techsash/waste-classification-data)

The model is used for classifiying image of waste into either Recyclable or Organic

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
