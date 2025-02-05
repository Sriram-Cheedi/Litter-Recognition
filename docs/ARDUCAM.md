# Set-up Process of ArduCAM multi cam adapter v2.2 on a raspberry pi
## Starting with a fresh OS install
Enter the following to update pi and kernel:
```
sudo apt-get update
sudo apt-get upgrade
sudo apt full-upgrade
sudo reboot
```
Then edit the config file:
```
sudo nano /home/firmware/config.txt
```
config.txt:
```
#Find the line "camera_auto_detect=1" and modify it: 
camera_auto_detect=0

#add Following content: 
dtoverlay=camera-mux-4port,cam0-imx219,cam2-imx219
```
Then shutdown and unplug the pi, connect the cameras to the multicam module and then the module to the pi:

![ArduCAM_1](https://github.com/user-attachments/assets/59b1143b-312a-4cfb-ae2c-751ac8911244)
![ArduCAM_2](https://github.com/user-attachments/assets/56ab49e4-dc74-4958-807d-43d6741dc8b0)

Running ```sudo dmesg | grep arducam``` returns nothing (contrary to arducam quick setup guide https://docs.arducam.com/Raspberry-Pi-Camera/Multi-Camera-CamArray/Quick-Start-Guide-for-Multi-Adapter-Board/#for-quad-camera-adapter-boardb012001)
