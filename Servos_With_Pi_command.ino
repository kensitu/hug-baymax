#include <Servo.h>

Servo rshoulder1;  // create servo object for each servo
Servo rshoulder2;
Servo relbow;

Servo lshoulder1;  
Servo lshoulder2;
Servo lelbow;

void setup() {
  rshoulder1.attach(0);  // attaches the servo on pin to the servo object
  rshoulder2.attach(1);
  relbow.attach(2);
  
  lshoulder1.attach(12);
  lshoulder2.attach(13);
  lelbow.attach(11);

  Serial.begin(9600);
}

void loop() {
  if (Serial.available()) {   //wait for a Serial command to initiate the hug
    int shouldHug = (Serial.read() - '0');
    if (shouldHug == 1) {
        //hug
      rshoulder1.write(100);
      rshoulder2.write(100);
      lshoulder1.write(80);
      lshoulder2.write(80); 
      
      delay(1500);
      
      relbow.write(160);
      lelbow.write(160);
      delay(1500);
    }
    else {
                                 //reset
      rshoulder1.write(20);
      rshoulder2.write(20);
      relbow.write(90);
      lshoulder1.write(160);
      lshoulder2.write(160);
      lelbow.write(90);
      delay(1500);
    }
  }
}

