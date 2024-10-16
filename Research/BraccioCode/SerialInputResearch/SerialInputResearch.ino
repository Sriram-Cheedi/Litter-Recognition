 /*
  testBraccio90.ino

 testBraccio90 is a setup sketch to check the alignment of all the servo motors
 This is the first sketch you need to run on Braccio
 When you start this sketch Braccio will be positioned perpendicular to the base
 If you can't see the Braccio in this exact position you need to reallign the servo motors position

 Created on 18 Nov 2015
 by Andrea Martino

 This example is in the public domain.
 */

#include <Braccio.h>
#include <Servo.h>


Servo base;
Servo shoulder;
Servo elbow;
Servo wrist_rot;
Servo wrist_ver;
Servo gripper;
char instruction;
boolean newData = false;

void setup() {  
  //Initialization functions and set up the initial position for Braccio
  //All the servo motors will be positioned in the "safety" position:
  //Base (M1):90 degrees
  //Shoulder (M2): 45 degrees
  //Elbow (M3): 180 degrees
  //Wrist vertical (M4): 180 degrees
  //Wrist rotation (M5): 90 degrees
  //gripper (M6): 10 degrees
  Braccio.begin();
  Serial.begin(9600);
  // Serial.println("Wall-e is ready for instructions...");
  Braccio.ServoMovement(20,         90, 90, 90, 90, 90, 90);
}

void loop() {
  
  receiveOneChar();

  switch(instruction) {
    case 'q':
      Braccio.ServoMovement(20,         90, 90, 90, 90, 0, 90);
      break;
    case 'e':
      Braccio.ServoMovement(20,         90, 90, 90, 90, 180, 90);
      break;
  }

}

void receiveOneChar() {
  if (Serial.available() > 0) {
    instruction = Serial.read();
    newData = true;
  }
}








