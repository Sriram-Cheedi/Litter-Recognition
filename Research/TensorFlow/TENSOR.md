# Research and guidance on how to use tensorflow for object detection

## Videos and Guides:
- https://www.youtube.com/playlist?list=PLAs-3cqyNbIjqaTLHNSu2g4kpaw6TGCud
- https://tensorflow-object-detection-api-tutorial.readthedocs.io/en/latest/install.html
- https://tensorflow-object-detection-api-tutorial.readthedocs.io/en/latest/auto_examples/object_detection_camera.html#sphx-glr-auto-examples-object-detection-camera-py

## Repos used:
- https://github.com/tensorflow/models (Some sample models for object detection in TensorFlow)

## Tools and Programs used
- miniconda (https://docs.anaconda.com/miniconda/miniconda-install/)
- protobuf (https://github.com/protocolbuffers/protobuf/releases)

# Installation Guide
## Install miniconda
Go to https://docs.anaconda.com/miniconda/miniconda-install/ and install the right version for your machine.
Run the following in a new command prompt to test the install:
```
conda list
```
If conda is not found then search for the anaconda prompt and type the following:
```
where conda
```
Copy the path that contains the 'bin' file and then add that to your machines PATH in your system's environment variables. Now check again in a new terminal if the 'conda list' command does not error.

## Create the conda environment
Enter the following in a terminal to create a conda environment:
```
conda create -n tensorflow pip python=3.9
```
Then enter the following to activate the environment
```
conda activate tensorflow
```
The terminal should now show what environment you are in at the beginning of the path like this
```
(tensorflow) C:\Users\user>
```

## Installing Tensorflow
First make sure you are in your tensorflow conda environment, then use pip to install the tensorflow package:
```
pip install --ignore-installed --upgrade tensorflow==2.5.0
```

To test the installation of tensorflow run the following:
```
python -c "import tensorflow as tf;print(tf.reduce_sum(tf.random.normal([1000, 1000])))"
```
This will probably print a lot of warnings but then print something similar to,
```
tf.Tensor(-136.50531, shape=(), dtype=float32)
```

This means that the tensorflow library is correctly installed on the machine.

## Using the tensorflow models
Now you need to download the tensorflow models repository from https://github.com/tensorflow/models, download it as a ZIP or git clone into this directory. Make sure the folder it is in is called "models" as the gitignore will make sure that this directory is not added to the repo, the file organisation should be like this:
```
TensorFlow/
└─ models/
   ├─ community/
   ├─ official/
   ├─ orbit/
   ├─ research/
   └── ...
├─ test.py
└── ...
```


