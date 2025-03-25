# Future Improvements

This document will cover potential improvements to the final release of our Software Engineering Project.

## Hardware Improvements

Below we will describe improvements that could be made to the hardware half of the project.

### Lidar

Using a lidar instead of two cameras was a consideration we made at the beginning of our tour of computer vision.
Unfortunately, due to the high cost for a high quality component we decided against it. For the genuine public release
of this product, a high quality lidar (potentially in conjunction with a dual camera system for movement purposes)
would make a lot of sense due to a higher degree of accuracy when assessing distances from objects - especially small ones.

### Raspberry Pi

Due to time constraints and seemingly random and rather annoying bugs, we were unable to get our Raspbberry Pi to work
within our system. Regrettably, this did mean we failed to meet a requirement we set ourselves at the start of the project.
A big first improvement would be to shrink the central computer from a laptop to a small computer like a Rapsberry Pi 5 (our
Raspberry Pi 4 had big issues with recognising two cameras of the same type) or a Jetson Nano.

### Higher Quality Arm

The current arm works perfectly for a proof of concept. As far as the possibility of it "roaming highways" goes, it's rather
bleak. A necessary improvement for the success of this product would be the upgrade of the arm so that it could withstand bad
weather, rough terrain and potential physical abuse from drivers or other animals. The current arm also struggle with precise
movements, making it rather poor at performing pickups at high ranges.


### A Movement System

In conjuntion with a higher wuality arm, having a system on which it can traverse roads is a necessity for the success of the
project as a legitimate product. Without it, the robot obviously cannot complete its intended purpose without great assistance
from a human - defeating the purpose. An agile X-like system which can handle difficult off and on-road terrain would be ideal.

## Software Improvements

Below we will describe improvements that could be made to the software half of the project.

### Specialised Model

We currently use a publicly available model for detecting litter. It has worked well for the purpose of providing a proof of
concept and allowing us to test the idea of an autonamous system that can pickup litter. However, a model that has been
specifically trained to detect litter in roadside environments would increase the success rate of the robot greatly. We,
of course, did not have time to train a model ourselves due to the huge time commitment collecting the data and training a 
model would have entailed. However, the real product would benefit greatly from this time investment.

### Parallelised UI and Robot

### Code To Handle a Movement System

