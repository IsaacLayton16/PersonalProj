#include "pitches.h"
#include "SR04.h"
#include <Stepper.h>
#include <Servo.h>


#define BUZZ 7
#define TRIG 12      
#define ECHO 13    

SR04 sr04 = SR04(ECHO, TRIG);
long measure;

const int stepsPerRevolution = 180;
Stepper myStepper(stepsPerRevolution, 8, 10, 9, 11); 
Servo myservo;
int pos = 0;

void setup() {
    Serial.begin(9600);
    myStepper.setSpeed(90);
    myservo.attach(6);  
}

void loop() {
    measure = sr04.Distance();


    // Distance > 5cm
    if (measure > 5) {
        noTone(BUZZ);                    // Buzzer off
        myservo.write(0);                // server @0deg
        myStepper.step(stepsPerRevolution); // Stepper to CW
    }

    // Distance <= 5cm
    if (measure <= 5) {
        tone(BUZZ, NOTE_A5);             // Buzzer on
        myservo.write(180);              // Servo @180deg
        myStepper.step(-stepsPerRevolution); // Stepper to CCW
    }
}
