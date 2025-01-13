### Guides For Setting Up PiCams
* [Detailed Guide for Setting up a Raspberry Pi Camera](https://raspberrytips.com/install-camera-raspberry-pi/#:~:text=Here%20are%20the%20main%20steps%20required%20to%20use,also%20show%20you%20how%20to%20choose%20the%20camera.)
* [Also a good guide and mentions what to do with >1 camera](https://www.xda-developers.com/connect-a-camera-module-to-raspberry-pi-5/)
* [Guide that shows how to install OpenCV with PiCams](https://aleksandarhaber.com/how-to-install-and-use-opencv-and-usb-camera-on-raspberry-pi-5-and-linux-ubuntu/)
* [Shows how to use 2 PiCams concurrently](https://thepihut.com/blogs/raspberry-pi-tutorials/how-to-use-two-camera-modules-with-raspberry-pi-5)
* [Same as the above](https://www.tomshardware.com/raspberry-pi/how-to-use-dual-cameras-on-the-raspberry-pi-5)

## Small Extra Notes
- The ID of the cameras will be 0 and 1
- Should be able to write code directly onto the Raspberry Pi using these IDs to directly access the camera feed
- Example code for inference is very similar to just getting the cameras working and can be found in the following tutorial: [Here](https://tutorials-raspberrypi.com/using-tensorflow-lite-with-google-coral-tpu-on-raspberry-pi-4/)
