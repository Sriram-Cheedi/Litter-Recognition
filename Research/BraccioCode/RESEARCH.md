# Folder to Track Research into code for the BRaccio Arm

## Communicating via the Serial Bus

This section is dedicated to code that documents how to use the serial bus to communicate with the Arduino board.

### SerialInputResearch.ino

When a device sends serial data to the Arduino, it arrives at a speed set by the baud rate.

We set this rate to about 960 characters a second with:

```Serial.begin(9600)```

Next we need a function to receive characters from the input buffer. We will then call this function at the
beginning of every loop.

First, we check if the Serial bus has a character for us to receive. Then we set a global variable "instruction"
to this value for later use.

```
void receiveOneChar() {
  if (Serial.available() > 0) {
    instruction = Serial.read();
  }
}
```

Going back to our loop, we now check which instruction was last called by the Serial bus.

```
switch(instruction) {
    case 'q':
      Braccio.ServoMovement(20,         90, 90, 90, 90, 0, 90);
      break;
    case 'e':
      Braccio.ServoMovement(20,         90, 90, 90, 90, 180, 90);
      break;
  }
```

Currenttly the code will twist the wrist (fifth motor) of the arm based on when 'q' and 'e' are sent down the bus.

On the top right of the Arduino IDE are two symbols. Clicking on the cardiac sensor blip will open the Serial Plotter.

![image](https://github.com/user-attachments/assets/dbb019ab-c12f-418c-abfb-63f47e662cad)

By typing letters in the "send message" box and clicking "send", you will now be able to send instructions to the arm.




  
