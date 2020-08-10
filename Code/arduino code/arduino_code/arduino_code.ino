#include "Arduino.h"
#include <Servo.h>

int contador;
Servo servo_width;    // Horizontal
Servo servo_height;   // Vertical

//config params
int pos_width;    // Horizontal position variable
int pos_height;   // Vertical position variable
int jump1;
int jump2;
char direction1;
char direction2;

void setup(){
  Serial.begin(9600);      // Standard velocity for communication
  
  //servo init config
  servo_width.attach(8);   // Horizontal servo on pin 9
  servo_height.attach(9); // Vertical servo on pin 10
  servo_width.write(90);     // Initial position set with 90 degrees (in the middle)
  servo_height.write(90);
  pos_width = pos_height = 90;
  jump1 = 0;
  direction1 = 5;
  jump2 = 0;
  direction2 = 5;
}

void loop(){
    
    if (Serial.available() > 0){
      
        String data_string = Serial.readStringUntil('\n');

        if (data_string == "center"){
          servo_width.write(90);     // Position set with 90 degrees (in the middle)
          servo_height.write(90);

        }
        else{
          direction1 = data_string.charAt(0);
          jump1 =  data_string.charAt(1) - 48;
          jump1 *= 10;
          Serial.println(direction1);
          Serial.println(jump1);
          direction2 = data_string.charAt(2);
          jump2 =  data_string.charAt(3) - 48;
          jump2 *= 10;
          Serial.println(direction2);
          Serial.println(jump2);

          if(direction1 == 't' && pos_height < 180 - jump1){ // Centering on top
              pos_height += jump1;
              servo_height.write(pos_height);
              Serial.println(pos_height);
              direction1 = 'n';
          }
        
          if(direction1 == 'b' && pos_height > jump1){ // Centering on bottom
              pos_height -= jump1;  
              servo_height.write(pos_height);
              Serial.println(pos_height);
              direction1 = 'n';
          }
          if(direction1 == 'r' && pos_width < 180 - jump1){ // Centering on the right
              pos_width += jump1;  
              servo_width.write(pos_width);
              Serial.println(pos_width);
              direction1 = 'n';
          }
          if(direction1 == 'l' && pos_width > jump1){ // Centering on the left
              pos_width -= jump1;
              servo_width.write(pos_width); 
              Serial.println(pos_width);
              direction1 = 'n';
          }
          
          if(direction2 == 't' && pos_height < 180 - jump2){ // Centering on top
              pos_height += jump2;
              servo_height.write(pos_height);
              Serial.println(pos_height);
              direction2 = 'n';
          }
        
          if(direction2 == 'b' && pos_height > jump2){ // Centering on bottom
              pos_height -= jump2;  
              servo_height.write(pos_height);
              Serial.println(pos_height);
              direction2 = 'n';
          }
          if(direction2 == 'r' && pos_width < 180 - jump2){ // Centering on the right
              pos_width += jump2;  
              servo_width.write(pos_width);
              Serial.println(pos_width);
              direction2 = 'n';
          }
          if(direction2 == 'l' && pos_width > jump2){ // Centering on the left
              pos_width -= jump2;
              servo_width.write(pos_width); 
              Serial.println(pos_width);
              direction2 = 'n';
          }
      }
    }
  }
