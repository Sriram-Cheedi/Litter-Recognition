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
