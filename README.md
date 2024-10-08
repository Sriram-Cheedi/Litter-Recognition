# Autonomous Litter Recognition System

## Contents:
- [Autonomus Litter Recognition System](https://github.com/spe-uob/2024-LitterRecognition1/blob/main/README.md#autonomous-litter-recognition-system)
   - [Problem Statement](https://github.com/spe-uob/2024-LitterRecognition1/tree/main?tab=readme-ov-file#problem-statement)
   - [Project Description](https://github.com/spe-uob/2024-LitterRecognition1/tree/main?tab=readme-ov-file#project-description)
   - [Project Requirements](https://github.com/spe-uob/2024-LitterRecognition1/tree/main?tab=readme-ov-file#project-requirements)
   - [Benifits and Impact](https://github.com/spe-uob/2024-LitterRecognition1/tree/main?tab=readme-ov-file#benifits-and-impact)
   - [Stakeholders](https://github.com/spe-uob/2024-LitterRecognition1/tree/main?tab=readme-ov-file#stakeholders)
   - [User Stories](https://github.com/spe-uob/2024-LitterRecognition1/tree/main?tab=readme-ov-file#user-stories)
   - [Links](https://github.com/spe-uob/2024-LitterRecognition1?tab=readme-ov-file#links)
   - [Tech Stack](https://github.com/spe-uob/2024-LitterRecognition1?tab=readme-ov-file#tech-stack)
   - [Group Members](https://github.com/spe-uob/2024-LitterRecognition1/tree/main?tab=readme-ov-file#group-members)


## Problem Statement:
Litter and debris accumulation on major roads and highways has become a significant environmental and safety concern. The increased use of non-biodegradable materials, the careless disposal of waste from
moving vehicles, and the frequent breakdown of vehicle components like plastic undertrays and tires have led to a rise in the volume of roadside litter. This poses a danger not only to the local ecosystem and
watercourses but also to road traffic, with potential hazards forming at the edge of the road.

The current methods of litter management are inefficient, dangerous, and resource-intensive. To combat this growing problem, there is a need for an innovative solution that can autonomously detect and manage
roadside litter, minimizing human intervention and improving safety, efficiency, and environmental outcomes.


## Project Description:
The proposed project aims to develop an Autonomous Litter Recognition and Collection System, specifically designed to detect, classify, and collect litter from roadside environments, particularly in areas where
access is limited or hazardous. This system would utilize advanced technologies, such as machine learning, computer vision, and robotics, to automatically identify litter in rough terrain, including grasslands,
shrubs, and trees near the road. The solution will be deployed on small autonomous vehicles that can safely operate on the roadside, even in challenging conditions.
With the rise of non-biodegradable packaging, an increase in littering from vehicles, and the frequent breakdown of vehicle components (such as plastic
parts and tyres), roadside litter accumulation has become a pressing issue. The challenge is exacerbated by smart motorways that eliminate the hard shoulder,
making manual collection costly, hazardous, and disruptive to traffic flow.

**The System will leverage several cutting-edge technologies, including:**
**Computer Vision and Machine Learning:** For accurate detection and classification of litter. Convolutional neural networks (CNNs) will be employed to analyze video feeds or images captured by onboard cameras.
The system will be trained to recognize common types of litter and differentiate them from natural elements like leaves and rocks.

**Robotic Mechanisms:** The autonomous vehicle will be equipped with mechanical arms, to collect litter of various sizes and compositions. These systems will be designed to operate effectively in rough and
uneven terrain, typical of roadside verges.

**Autonomous Navigation:** The vehicle will be capable of navigating along the roadside without human intervention, using GPS and sensor technologies to stay within designated areas while avoiding obstacles
such as road signs, barriers, and natural features.

## Project Requirements:
**Litter Detecgtion:** The system will use advanced image recognition and object detection techniques to identify man-made items scattered along the roadside. This includes detecting litter both on the ground
and entangled in roadside vegetation such as grass, shrubs, and trees. The detection system will be capable of operating in varying weather and lighting conditions typical of road environments.

**Litter Classification:** The detected litter will be classified into different sizes and categories, such as plastic, metal, paper, and other materials. The classification system will differentiate between
larger objects (e.g., plastic bottles, vehicle debris) and smaller, more dispersed litter (e.g., cigarette butts, snack wrappers). This classification will inform the optimal collection method for each type of
waste.

**Collection Methodology:** Based on the type and size of litter identified, the system will determine the most effective collection method. Larger items may require mechanical arms or grippers, while smaller
debris could be collected using vacuum systems or sweeping mechanisms. The collection system will be adaptable to different types of litter and their location on the roadside.

**Litter Storage:** Once collected, the system will place the litter into designated storage containers onboard the autonomous vehicle. These containers will be designed for easy disposal or recycling at
regular intervals, reducing the need for frequent manual intervention.

## Benifits and Impact
The development and deployment of this autonomous litter recognition and collection system will provide several key benefits:

**Increased Safety:** By reducing the need for manual litter collection in dangerous roadside conditions, this system minimizes the risk to workers.

**Cost Efficiency:** The automation of litter detection and collection will lower operational costs by reducing labor expenses and the need for expensive lane closures during manual cleanups.

**Environmental Protection:** The system will help maintain cleaner roadsides, preventing litter from polluting local ecosystems and waterways, while also contributing to waste management and recycling
initiatives.

**Scalability:** This solution can be scaled across highways and other high-traffic areas, creating a more systematic and consistent approach to litter management.


## Stakeholders:
**Moss&Gund Ltd**
* The group that would deploy the autonomous system as a commercial solution, using AGILE X systems to make our system mobile.

**The General Public**
* The general population will benefit from cleaner roads, reduced litter, and improved public safety on motorways and highways.

**Government Agencies**
* Responsible for maintaining roads and addressing environmental concerns related to roadside litter.

**Road Maintenance Authorities**
* Organizations responsible for maintaining roads and highways, who will benefit from the autonomous litter collection system.

**Environmental Research Institutes:**
* Institutions focused on pollution, waste management, and environmental preservation can benefit from the data collected by the system, offering insights into littering
  behaviors and environmental impacts.
  
**Waste Management Companies:** 
* Could utilize the system for efficient, automated collection of litter, minimizing manual labor and costs.

**Smart City Inititives:**
* The litter recognition system could be integrated into broader smart city infrastructures, improving urban environmental management.

**Regulators and Policy Makers:**
* Those involved in developing regulations and policies related to roadside safety, environmental protection, and smart city initiatives could influence or mandate the use of such technology on motorways and 
  highways.

**Venture Capitalists and Private Investors:**
* Individuals or firms looking to invest in cutting-edge technology that addresses environmental and safety challenges.



## User Stories:
**As a client, I want...**
  * A system that can identify a wide variety of roadside litter and can identify how to deal with it

**As a Department of Transportation official, I want to...**
  * Monitor litter levels along highways and motorways in real-time, so that I can schedule cleaning efforts more efficiently and reduce manual inspections.
  * Deploy an autonomous litter collection system, so that lane closures and disruptions are minimized, and road safety for workers is improved.

**As a Waste Management Contractor, I want to...**
  * Integrate autonomous litter collection vehicles into my operations, so that I can reduce the cost and risk of manual roadside litter collection.
  * Ensure that the system classifies litter types accurately, so that I can better manage recycling and waste disposal processes.

**As a Smart City Project Manager, I want to...**
  *  Implement a system that automatically detects and removes litter in public spaces and roadsides, so that I can maintain a clean city environment with minimal human intervention.
  *  Showcase the technology as part of our smart city initiatives, so that we can attract investors and improve the city’s reputation for innovation and environmental sustainability.

**As a member of the public I want...**
  * A safe and contained system so that it doesn't impede on my use of the road.

**As an Environmental Protection Agency official, I want to...**
  * I want a system that can efficiently detect and collect non-biodegradable litter so that I can ensure cleaner environments and minimize the impact of pollution on wildlife and ecosystems.

**As a road maintenance worker I want...** 
  * A autonomous system to detect and collect litter on the roadside, so that I can reduce the time and risk associated
    with manual litter collection.
**As a student, I want to...**
  * Develop a proof of concept for an autonomous litter detection and disposal system, so that I can apply my knowledge in computer
    vision and robotics to a meaningful project.
**As a transportation department official,I want**
  * A reliable and efficient system for maintaining clean roadsides, so that we can ensure road safety and comply
    with environmental regulations.
  
## Links:
- [Kanban Board](https://github.com/orgs/spe-uob/projects/219)
- [Gantt Chart](https://github.com/orgs/spe-uob/projects/219/views/2)

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


## Group Members
|     Member     |         Email         |
| -------------- | --------------------- |
|  Ryan Venn     | oc23252@bristol.ac.uk |
|  Sriram Cheedi | dz23405@bristol.ac.uk |
|  Hanzhong Qiu  | dw22963@bristol.ac.uk |
|  Jude Beaton   | ww23682@bristol.ac.uk |
|  Jack Cains    | ep23722@bristol.ac.uk |
