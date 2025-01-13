# Training a Pre-Defined Model
## 1. Choosing our Pre-Defined Model
The immediate standout when it came to researching an easy-to-train object detection framework was YOLO (You Only Look Once). This was due to its well documented reputation across the internet, with plenty of guides available on how to train the model using custom datasets.

The next design choice to make was to choose which version of YOLO to use for our training on our chosen dataset between v8 and v11 as they were the two  most recent that we could find informative documentation on. Using a range of sources, including [this website](https://www.datature.io/blog/yolo11-step-by-step-training-on-custom-data-and-comparison-with-yolov8), we decided upon using v11 due to the increase in detection accuracy with a small hit on latency.

All of this sounded great until it was too good to be true, as YOLO requires a paid license to be deployed commerically. Back to the drawing board!

## 2. Choosing our Custom Dataset
In our defeat in finding a commercially viable model to train for litter detection, we chose to set our sights on what dataset to use for the timebeing. As we had already researched potential datasets, we settled on using TACO for the timebeing as it has a large selection of annotated images as well as being free use so long as citation is given. 

Looking into the TACO repository there also appears to be its own detection model for litter that is also free-to-use, which will be good in the short build-up to the MVP.

The detector code can be found on the [taco repository](https://github.com/pedropro/TACO), however we are currently having compatibility issues due to the model code relying on older versions of software. 

## 3. The Rubber Room of Dependencies
After many hours of trying to get ANYTHING to work using dependencies, I have ended up migrating to attempting to use google colab to train a model instead. The first thing I have gotten to work is [the tensorflow test.py following this guide](https://colab.research.google.com/github/EdjeElectronics/TensorFlow-Lite-Object-Detection-on-Android-and-RaspberryPi/blob/master/Train_TFLite2_Object_Detction_Model.ipynb#scrollTo=wh_HPMOqWH9z). Hopefully this means that the rest of the notebook tutorial will work and we will be able to train a tf-lite model using the TACO data to be able to be placed onto a raspberry Pi.

## 4. Moving On
After struggling to train a model on the TACO dataset, our plan of custom training has been changed into just using a pre-trained model (due to our lack of experience). Moving on to finding a pre-trained model, we came across two web pages, [1](https://www.kaggle.com/code/bouweceunen/garbage-detection-with-tensorflow) and [2](https://www.kaggle.com/code/bouweceunen/training-ssd-mobilenet-v2-with-taco-dataset), which both contained pre-trained models perfect for our project. We will now move onto using this model on our Raspberry Pi to advance onto the next stage of the project.
