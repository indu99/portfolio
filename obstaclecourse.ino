#include <Servo.h>

Servo servoLeft;
Servo servoRight;

void setup()                                 // Built-in initialization block
{
  pinMode(7, INPUT);                         // Set right whisker pin to input
  pinMode(5, INPUT);                         // Set left whisker pin to input  
  
  Serial.begin(9600);                        // Set data rate to 9600 bps (i.e. 
  servoLeft.attach(13);
  servoRight.attach(12);

}  
 
void loop()                                  // Main loop auto-repeats
{                                            
  byte wLeft = digitalRead(5);               // Copy left result to wLeft  
  byte wRight = digitalRead(7);              // Copy right result to wRight
  if (wLeft == 1 ) {
    servoLeft.writeMicroseconds(1700);
    servoRight.writeMicroseconds(1300);
    delay(100);
  }
  else if (wLeft == 0 ) {
    servoLeft.writeMicroseconds(1500);
    servoRight.writeMicroseconds(1700);
    Serial.println ("Left whisker in contact");
    delay(300);
  }
  if (wRight == 1) {
    servoLeft.writeMicroseconds(1700);
    servoRight.writeMicroseconds(1300);
    delay(100);
  }
  else if (wRight == 0) {
    servoLeft.writeMicroseconds(1500);
    servoRight.writeMicroseconds(1300);
    Serial.println ("Right whisker in contact");
    delay(300);
  }
  if (wRight == 0 && wLeft == 0) {
    servoLeft.writeMicroseconds(1500);
    servoRight.writeMicroseconds(1700);
    delay (300);
  }

 

  delay(50);



}

 




 

