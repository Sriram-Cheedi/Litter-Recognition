# Set-up Process of ArduCAM multi cam adapter v2.2 on a raspberry pi
This File is for the purpose of storing debugging information to do with the ArduCAM v2.2 multi camera adapter
## Hardware
- Raspberry Pi 4b (4GB RAM)
- 2x Pi Camera Module 2
- ArduCAM multicam adapter v2.2

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

Running ```libcamera-hello``` results in the following error:
```
pi@raspberrypi:~ $ libcamera-hello
[0:17:49.216135806] [2326]  INFO Camera camera_manager.cpp:327 libcamera v0.4.0+50-83cb8101
[0:17:49.344088173] [2333]  WARN RPiSdn sdn.cpp:40 Using legacy SDN tuning - please consider moving SDN inside rpi.denoise
[0:17:49.350039148] [2333]  INFO RPI vc4.cpp:447 Registered camera /base/soc/i2c0mux/i2c@1/pca@70/i2c@0/imx219@10 to Unicam device /dev/media0 and ISP device /dev/media2
[0:17:49.350277982] [2333]  INFO RPI pipeline_base.cpp:1121 Using configuration file '/usr/share/libcamera/pipeline/rpi/vc4/rpi_apps.yaml'
[0:17:49.380092602] [2333]  WARN RPiSdn sdn.cpp:40 Using legacy SDN tuning - please consider moving SDN inside rpi.denoise
[0:17:49.387904211] [2333]  INFO RPI vc4.cpp:447 Registered camera /base/soc/i2c0mux/i2c@1/pca@70/i2c@2/imx219@10 to Unicam device /dev/media0 and ISP device /dev/media2
[0:17:49.388351249] [2333]  INFO RPI pipeline_base.cpp:1121 Using configuration file '/usr/share/libcamera/pipeline/rpi/vc4/rpi_apps.yaml'
Made X/EGL preview window
Mode selection for 1640:1232:12:P
    SRGGB10_CSI2P,640x480/0 - Score: 4504.81
    SRGGB10_CSI2P,1640x1232/0 - Score: 1000
    SRGGB10_CSI2P,1920x1080/0 - Score: 1541.48
    SRGGB10_CSI2P,3280x2464/0 - Score: 1718
    SRGGB8,640x480/0 - Score: 5504.81
    SRGGB8,1640x1232/0 - Score: 2000
    SRGGB8,1920x1080/0 - Score: 2541.48
    SRGGB8,3280x2464/0 - Score: 2718
[0:17:51.341085580] [2326]  INFO Camera camera.cpp:1202 configuring streams: (0) 1640x1232-YUV420 (1) 1640x1232-SBGGR10_CSI2P
[0:17:51.341977137] [2333]  INFO RPI vc4.cpp:622 Sensor: /base/soc/i2c0mux/i2c@1/pca@70/i2c@2/imx219@10 - Selected sensor format: 1640x1232-SBGGR10_1X10 - Selected unicam format: 1640x1232-pBAA
[0:17:52.500268223] [2333]  WARN V4L2 v4l2_videodevice.cpp:2150 /dev/video0[22:cap]: Dequeue timer of 1000000.00us has expired!
[0:17:52.500445798] [2333] ERROR RPI pipeline_base.cpp:1367 Camera frontend has timed out!
[0:17:52.500485575] [2333] ERROR RPI pipeline_base.cpp:1368 Please check that your camera sensor connector is attached securely.
[0:17:52.500527113] [2333] ERROR RPI pipeline_base.cpp:1369 Alternatively, try another cable and/or sensor.
ERROR: Device timeout detected, attempting a restart!!!
```

The troubleshootng guide (linked above) states that this can be an error for pi model 5's using the camera module 1, but does not offer the solutions/correct drivers for the Camera Module 2's and Pi 4b that we are using.

```libcamera-hello --list``` returns the following information:
```
libcamera-hello --list
Available cameras
-----------------
0 : imx219 [3280x2464 10-bit RGGB] (/base/soc/i2c0mux/i2c@1/pca@70/i2c@2/imx219@10)
    Modes: 'SRGGB10_CSI2P' : 640x480 [206.65 fps - (1000, 752)/1280x960 crop]
                             1640x1232 [41.85 fps - (0, 0)/3280x2464 crop]
                             1920x1080 [47.57 fps - (680, 692)/1920x1080 crop]
                             3280x2464 [21.19 fps - (0, 0)/3280x2464 crop]
           'SRGGB8' : 640x480 [206.65 fps - (1000, 752)/1280x960 crop]
                      1640x1232 [83.70 fps - (0, 0)/3280x2464 crop]
                      1920x1080 [47.57 fps - (680, 692)/1920x1080 crop]
                      3280x2464 [21.19 fps - (0, 0)/3280x2464 crop]

1 : imx219 [3280x2464 10-bit RGGB] (/base/soc/i2c0mux/i2c@1/pca@70/i2c@0/imx219@10)
    Modes: 'SRGGB10_CSI2P' : 640x480 [206.65 fps - (1000, 752)/1280x960 crop]
                             1640x1232 [41.85 fps - (0, 0)/3280x2464 crop]
                             1920x1080 [47.57 fps - (680, 692)/1920x1080 crop]
                             3280x2464 [21.19 fps - (0, 0)/3280x2464 crop]
           'SRGGB8' : 640x480 [206.65 fps - (1000, 752)/1280x960 crop]
                      1640x1232 [83.70 fps - (0, 0)/3280x2464 crop]
                      1920x1080 [47.57 fps - (680, 692)/1920x1080 crop]
                      3280x2464 [21.19 fps - (0, 0)/3280x2464 crop]
```
```
pi@raspberrypi:~ $ dmesg | grep -E "imx477|imx219|arducam"
[    0.062621] /soc/i2c0mux/i2c@1/pca@70/i2c@2/imx219@10: Fixed dependency cycle(s) with /video-mux
[    0.062710] /soc/i2c0mux/i2c@1/pca@70/i2c@0/imx219@10: Fixed dependency cycle(s) with /video-mux
[    0.069557] /soc/i2c0mux/i2c@1/pca@70/i2c@2/imx219@10: Fixed dependency cycle(s) with /video-mux
[    0.069703] /soc/i2c0mux/i2c@1/pca@70/i2c@0/imx219@10: Fixed dependency cycle(s) with /video-mux
[    6.216496] /soc/i2c0mux/i2c@1/pca@70/i2c@2/imx219@10: Fixed dependency cycle(s) with /video-mux
[    6.217068] /soc/i2c0mux/i2c@1/pca@70/i2c@0/imx219@10: Fixed dependency cycle(s) with /video-mux
```
```
pi@raspberrypi:~ $ ls /dev/video0
/dev/video0
```
```
pi@raspberrypi:~ $ uname -a
Linux raspberrypi 6.6.74+rpt-rpi-v8 #1 SMP PREEMPT Debian 1:6.6.74-1+rpt1 (2025-01-27) aarch64 GNU/Linux
```
```
pi@raspberrypi:~ $ cat /etc/os-release
PRETTY_NAME="Debian GNU/Linux 12 (bookworm)"
NAME="Debian GNU/Linux"
VERSION_ID="12"
VERSION="12 (bookworm)"
VERSION_CODENAME=bookworm
ID=debian
HOME_URL="https://www.debian.org/"
SUPPORT_URL="https://www.debian.org/support"
BUG_REPORT_URL="https://bugs.debian.org/"
```
```
pi@raspberrypi:~ $ cat /proc/meminfo
MemTotal:        3888880 kB
MemFree:         1799292 kB
MemAvailable:    2791632 kB
Buffers:           37800 kB
Cached:          1161740 kB
SwapCached:            0 kB
Active:          1293964 kB
Inactive:         505768 kB
Active(anon):     766756 kB
Inactive(anon):        0 kB
Active(file):     527208 kB
Inactive(file):   505768 kB
Unevictable:      111212 kB
Mlocked:               0 kB
SwapTotal:        381948 kB
SwapFree:         381948 kB
Zswap:                 0 kB
Zswapped:              0 kB
Dirty:               936 kB
Writeback:             0 kB
AnonPages:        711404 kB
Mapped:           411716 kB
Shmem:            166564 kB
KReclaimable:      35556 kB
Slab:              74760 kB
SReclaimable:      35556 kB
SUnreclaim:        39204 kB
KernelStack:        7040 kB
PageTables:        16588 kB
SecPageTables:         0 kB
NFS_Unstable:          0 kB
Bounce:                0 kB
WritebackTmp:          0 kB
CommitLimit:     2326388 kB
Committed_AS:    4656192 kB
VmallocTotal:   257687552 kB
VmallocUsed:       24368 kB
VmallocChunk:          0 kB
Percpu:              720 kB
CmaTotal:         524288 kB
CmaFree:          476988 kB
```
```
pi@raspberrypi:~ $ cat /boot/firmware/config.txt
# For more options and information see
# http://rptl.io/configtxt
# Some settings may impact device functionality. See link above for details

# Uncomment some or all of these to enable the optional hardware interfaces
#dtparam=i2c_arm=on
#dtparam=i2s=on
#dtparam=spi=on

# Enable audio (loads snd_bcm2835)
dtparam=audio=on

# Additional overlays and parameters are documented
# /boot/firmware/overlays/README

# Automatically load overlays for detected cameras
camera_auto_detect=0

# Automatically load overlays for detected DSI displays
display_auto_detect=1

# Automatically load initramfs files, if found
auto_initramfs=1

# Enable DRM VC4 V3D driver
dtoverlay=vc4-kms-v3d
max_framebuffers=2

# Don't have the firmware create an initial video= setting in cmdline.txt.
# Use the kernel's default instead.
disable_fw_kms_setup=1

# Run in 64-bit mode
arm_64bit=1

# Disable compensation for displays with overscan
disable_overscan=1

# Run as fast as firmware / board allows
arm_boost=1

[cm4]
# Enable host mode on the 2711 built-in XHCI USB controller.
# This line should be removed if the legacy DWC2 controller is required
# (e.g. for USB device mode) or if USB support is not required.
otg_mode=1

[cm5]
dtoverlay=dwc2,dr_mode=host

[all]

# Multicam Adapter
dtoverlay=camera-mux-4port,cam0-imx219,cam2-imx219
```

