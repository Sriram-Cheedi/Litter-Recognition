#include <Braccio.h>
#include <Servo.h>

String incomingByte;    
Servo base;
Servo shoulder;
Servo elbow;
Servo wrist_rot;
Servo wrist_ver;
Servo gripper;

void setup() {

  Serial.begin(115200);

  // Braccio
  Braccio.begin();
}

// debug information on the serial stream
void printString(String inp) {
  for (int i = 0; i < inp.length(); i++)
        {
        Serial.write(inp[i]);   // Push each char 1 by 1 on each loop pass
        }
   Serial.write("\n");
    }
  
void loop() {

  if (Serial.available() > 0) {

    incomingByte = Serial.readStringUntil('\n');

    // check whether it contains P
    // split at comma
    // set values for joints

    String start_of_string_robot = "P";

    // check if there is a substring
    // handles serial robot input
    if (strstr(incomingByte.c_str(), start_of_string_robot.c_str())) {
      int params[7];
      
      // remove first character 'P'
      String cleanString = incomingByte.substring(1,incomingByte.length());

      String delimiter = ",";
      int i = 0;
      while(strstr(cleanString.c_str(), delimiter.c_str())){
        int index = cleanString.indexOf(delimiter);
        String subTemp = cleanString.substring(0, index);
        cleanString = cleanString.substring(index + 1, incomingByte.length());

        params[i] = subTemp.toInt();
        i += 1;
      }
      
      Braccio.ServoMovement(params[0], params[1], params[2], params[3], params[4], params[5], params[6]);
      
      Serial.write("Moved Braccio with serial input\n");
      }
    else{
      Serial.write("invald input\n");
    }

  }
}