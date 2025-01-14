# Autonomous Litter Recognition System

## Contents:
- [Autonomus Litter Recognition System](https://github.com/spe-uob/2024-LitterRecognition1/blob/main/README.md#autonomous-litter-recognition-system)
   - [Problem Statement](https://github.com/spe-uob/2024-LitterRecognition1/tree/main?tab=readme-ov-file#problem-statement)
   - [Project Description](https://github.com/spe-uob/2024-LitterRecognition1/tree/main?tab=readme-ov-file#project-description)
   - [Project Requirements](https://github.com/spe-uob/2024-LitterRecognition1/tree/main?tab=readme-ov-file#project-requirements)
   - [Benefits and Impact](https://github.com/spe-uob/2024-LitterRecognition1/tree/main?tab=readme-ov-file#benifits-and-impact)
   - [Stakeholders](https://github.com/spe-uob/2024-LitterRecognition1/tree/main?tab=readme-ov-file#stakeholders)
   - [User Stories](https://github.com/spe-uob/2024-LitterRecognition1/tree/main?tab=readme-ov-file#user-stories)
   - [Links](https://github.com/spe-uob/2024-LitterRecognition1?tab=readme-ov-file#links)
   - [Project Structure](https://github.com/spe-uob/2024-LitterRecognition1?tab=readme-ov-file#project-structure)
   - [User Instructions](https://github.com/spe-uob/2024-LitterRecognition1?tab=readme-ov-file#user-instructions)
   - [Developer Instructions](https://github.com/spe-uob/2024-LitterRecognition1?tab=readme-ov-file#developer-instructions)
   - [Tech Stack](https://github.com/spe-uob/2024-LitterRecognition1?tab=readme-ov-file#tech-stack)
   - [Architecture Diagram](https://github.com/spe-uob/2024-LitterRecognition1?tab=readme-ov-file#architecture-diagram)
   - [License](https://github.com/spe-uob/2024-LitterRecognition1?tab=readme-ov-file#license)
   - [Group Members](https://github.com/spe-uob/2024-LitterRecognition1/tree/main?tab=readme-ov-file#group-members)


## Problem Statement:
Litter blights our major roads and highways leading to serious environmental and safety issues. Overwhelming litter on the roadsides is mainly attributed to increased use of non-biodegradable items, unattended
disposal from moving vehicles and regular detachment of plastic undercarriages or mobile vehicle parts (such as tyres). It not only threatens the endless fauna and fish of our life-filled rivers, but it also
poses a danger to road trafficfe when potential hazards form at shoulder level.

The way in which litter is managed now, it's wasteful and dangerous. There exists an urgency to counter this proliferating issue, with the development of a pioneering autonomous litter management solution that
can detect and clear road litter efficiently reducing human intervention while maintaining safety complying environmental impact as well.


## Project Description:
This proposal will investigate an advanced system for the identification and collection of litter that will automate the litter recognition, classification, and collecting process in roadside environments,
particularly in regions with
limited or precarious, such that accesses are restricted. It would be a system that utilizes advanced technologies of machine learning, computer vision, and robotics to automatically detect litter in rough
terrain, such as grasslands, shrubs, and trees along the road. The technology will be applied to smaller-scale autonomous vehicles that can safely work at the edge of the road in poor conditions.
The increasing volume of non-biodegradable packaging, the intensification of litter from vehicles, and frequent breakdown of vehicle parts (such as tyres).Apart from the plastic parts and tyres, there is also the big problem of litter accumulating along the roadsides.

**The System will leverage several cutting-edge technologies, including:**
**Computer Vision and Machine Learning:** For accurate detection and classification of litter. Convolutional neural networks (CNNs) will be employed to analyze video feeds or images captured by onboard cameras.
The system will be trained to recognize common types of litter and differentiate them from natural elements like leaves and rocks.

**Robotic Mechanisms:** The autonomous vehicle will be equipped with mechanical arms, to collect litter of various sizes and compositions. These systems will be designed to operate effectively in rough and
uneven terrain, typical of roadside verges.

**Autonomous Navigation:** The vehicle will be capable of navigating along the roadside without human intervention, using GPS and sensor technologies to stay within designated areas while avoiding obstacles
such as road signs, barriers, and natural features.

## Project Requirements:
**Litter Detection:** The system will use advanced image recognition and object detection techniques to identify man-made items scattered along the roadside. This includes detecting litter both on the ground
and entangled in roadside vegetation such as grass, shrubs, and trees. The detection system will be capable of operating in varying weather and lighting conditions typical of road environments.

**Litter Classification:** The detected litter will be classified into different sizes and categories, such as plastic, metal, paper, and other materials. The classification system will differentiate between
larger objects (e.g., plastic bottles, vehicle debris) and smaller, more dispersed litter (e.g., cigarette butts, snack wrappers). This classification will inform the optimal collection method for each type of
waste.

**Collection Methodology:** Based on the type and size of litter identified, the system will determine the most effective collection method. Larger items may require mechanical arms or grippers, while smaller
debris could be collected using vacuum systems or sweeping mechanisms. The collection system will be adaptable to different types of litter and their location on the roadside.

**Litter Storage:** Once collected, the system will place the litter into designated storage containers onboard the autonomous vehicle. These containers will be designed for easy disposal or recycling at
regular intervals, reducing the need for frequent manual intervention.

## Benefits and Impact
The development and deployment of this autonomous litter recognition and collection system will provide several key benefits:

**Increased Safety:** By reducing the need for manual litter collection in dangerous roadside conditions, this system minimizes the risk to workers.

**Cost Efficiency:** The automation of litter detection and collection will lower operational costs by reducing labor expenses and the need for expensive lane closures during manual cleanups.

**Environmental Protection:** The system will help maintain cleaner roadsides, preventing litter from polluting local ecosystems and waterways, while also contributing to waste management and recycling
initiatives.

**Scalability:** This solution can be scaled across highways and other high-traffic areas, creating a more systematic and consistent approach to litter management.


## Stakeholders:
**Moss&Gund Ltd:**
* Role: The commissioning group for this project. They will oversee its development and we will meet biweekly to go over our progress.
* Purpose for the System: They would like for the system to be able to recognize and discard 6 keys types of roadside litter into a bag. The group would take the autonomous system to market as a commercial 
  solution using AGILE X systems to make our system mobile.

**General Public:**
* Role: The deployment of the project will most likely affect them as the system will be working on the same roads.
* Purpose for the System: They are not direct users, but the general public do stand to benefit in terms of cleaner roads, reduced litter and improved public safety on the motorways and highways. The system 
  will be required to consider the needs of the public.

**Government Agencies and Road Maintenance Authorities:**
* Role: They are the biggest beneficiaries of the system, and they would ensure that their utilization of the system would lead to maintaining the roads and protecting the environmental 
  concerns associated with roadside litter.
* Purpose for the System: The groups will apply the system to improve their current workflow of dispatching groups of litter collectors late at night. They have to clean the road side by side, along with 
  closing the road and inefficient gathering. The new system is targeted to automate this process for cost reductions and efficiency.

**Environmental Research Institutes:**
* Role: Scientists will be more interested in the data generated through the implementation of the system and its effect on pollution and local wildlife.
* Purpose for the System: Institutions may be a keen observer of the system and the results to assess the ability of the system to respond effectively to the reduction in pollution and conservation of nature at 
  the local level. Data collected may be found useful in determining the progress made in conservation 

## User Stories:
**As a client, I want..**
 * A system that will identify a wide variety of roadside litter and identify how to deal with it

**As a Waste Management Contractor, I want to..**
 * Integrate autonomous litter collection vehicles into my operations, so that I can reduce the cost and risk of manual roadside litter collection.
 * Litter types classified correctly by the system so that I have better management of recycling and waste disposal processes.

**As a member of the public I want.**
 * A safe and contained system not impeding my use of the road.

**As an Environmental Protection Agency official, I want to..**
 * I want a system which has the capability for quick identification and collection of non-biodegradable litter so that I am able to ensure cleaner environments and reduction of the impact of pollution on wildlife and ecosystems as much as possible.

**As a student, I want to..**
 * Create a proof of concept for an autonomous litter detection and disposal system so that I can utilize knowledge in computer
   Integrate vision and robotics into some meaningful project.


  
## Links:
- [Kanban Board](https://github.com/orgs/spe-uob/projects/219)
- [Gantt Chart](https://github.com/orgs/spe-uob/projects/219/views/2)


## Project Structure


## User Instructions

Requirements: [Python](https://www.python.org/downloads/), [Arduino IDE](https://www.arduino.cc/en/software), Arduino UNO and a Braccio robot arm

Download interface.py, braccio_adapter.py and the arduino_script directory in "code". Place all three in the same directory on your machine.

Connect your arm to the Arduino and power it on.

Open the arduino_script.ino file in the arduino IDE and click Upload in the top right. The arm should now move to the safety position.

Now navigate to the directory the python files are stored in on your machine via command line and run 

```console
python interface.py
```
A PyGame window will now open.

To control the arm, click into the window and press the key corresponding to the desired servo you want to move:

   Servo 1 (rotate base): Q, A  
   Servo 2 (joint above the base): W, S  
   Servo 3 (elbow joint): E, D  
   Servo 4 (joint below the claw): R, F  
   Servo 5 (rotate claw): T, G  
   Servo 6 (close and open the claw): Z, H  
   Pickup Object (picks up an object and places in a box) Clockwise/Anti-clockwise: P, L
   Return to Safety Position: C

## Developer Instructions


## Tech Stack
### Hardware 
 - Sensors:
    - Cameras
    - LIDAR
 - Actuators:
    - Robotic Arms
    - Wheel
 - Microcontroller
    - Raspberry Pi
### Software 
 - Operating System
 - Python
 - Computer Vision
     - YOLO
 - Machine Learning
    - Pytorch
 - Image Processing
    - OPENCV
 - Robotics
 - Control Systems
 - Route Planning System
### Development Tools
 - GitHub


## Architecture Diagram
![image]([docs/Architecture-Diagrams/final architecture.jpeg](https://github.com/spe-uob/2024-LitterRecognition1/blob/4932df0f511f91ba4735814bd121921b5f6dbb32/docs/Architecture-Diagrams/final%20architecture.jpeg))


## License
This project uses the MIT license. For more information, you can view the [LICENSE](https://github.com/spe-uob/2024-LitterRecognition1/blob/dev/LICENSE) file.

## Group Members
|     Member     |         Email         |
| -------------- | --------------------- |
|  Ryan Venn     | oc23252@bristol.ac.uk |
|  Sriram Cheedi | dz23405@bristol.ac.uk |
|  Hanzhong Qiu  | dw22963@bristol.ac.uk |
|  Jude Beaton   | ww23682@bristol.ac.uk |
|  Jack Cains    | ep23722@bristol.ac.uk |
