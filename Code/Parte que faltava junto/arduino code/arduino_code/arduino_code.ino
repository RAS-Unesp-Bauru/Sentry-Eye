#include "Arduino.h"
#include <Servo.h>

int contador;
Servo servo_width;    // Horizontal
Servo servo_height;   // Vertical

//config params
int pos_width;    // Variável de posição na horizontal
int pos_height;   // Variável de posição na vertical
int jump1;
int jump2;
char direcao1;
char direcao2;

void setup(){
  Serial.begin(9600);      // Velocidade padrão para comunicação
  //servo init config
  servo_width.attach(8);   // Horizontal no pino 9
  servo_height.attach(9); // Vertical no pino 10
  servo_width.write(90);     // Posição padrão setado em 90 graus (no meio)
  servo_height.write(90);
  pos_width = pos_height = 90;
  jump1 = 0;
  direcao1 = 5;
  jump2 = 0;
  direcao2 = 5;
}

void loop(){
    
    if (Serial.available() > 0){
      
        String data_string = Serial.readStringUntil('\n');

        if (data_string == "center"){
          servo_width.write(90);     // Posição padrão setado em 90 graus (no meio)
          servo_height.write(90);

        }
        else{
          direcao1 = data_string.charAt(0);
          jump1 =  data_string.charAt(1) - 48;
          jump1 *= 10;
          Serial.println(direcao1);
          Serial.println(jump1);
          direcao2 = data_string.charAt(2);
          jump2 =  data_string.charAt(3) - 48;
          jump2 *= 10;
          Serial.println(direcao2);
          Serial.println(jump2);

          if(direcao1 == 't' && pos_height < 180 - jump1){ // Centralizando para cima
              pos_height += jump1;
              servo_height.write(pos_height);
              Serial.println(pos_height);
              direcao1 = 'n';
          }
        
          if(direcao1 == 'b' && pos_height > jump1){ // Centralizando para baixo
              pos_height -= jump1;  
              servo_height.write(pos_height);
              Serial.println(pos_height);
              direcao1 = 'n';
          }
          if(direcao1 == 'r' && pos_width < 180 - jump1){ // Centralizando para direita
              pos_width += jump1;  
              servo_width.write(pos_width);
              Serial.println(pos_width);
              direcao1 = 'n';
          }
          if(direcao1 == 'l' && pos_width > jump1){ // Centralizando para esquerda
              pos_width -= jump1;
              servo_width.write(pos_width); 
              Serial.println(pos_width);
              direcao1 = 'n';
          }
          
          if(direcao2 == 't' && pos_height < 180 - jump2){ // Centralizando para cima
              pos_height += jump2;
              servo_height.write(pos_height);
              Serial.println(pos_height);
              direcao2 = 'n';
          }
        
          if(direcao2 == 'b' && pos_height > jump2){ // Centralizando para baixo
              pos_height -= jump2;  
              servo_height.write(pos_height);
              Serial.println(pos_height);
              direcao2 = 'n';
          }
          if(direcao2 == 'r' && pos_width < 180 - jump2){ // Centralizando para direita
              pos_width += jump2;  
              servo_width.write(pos_width);
              Serial.println(pos_width);
              direcao2 = 'n';
          }
          if(direcao2 == 'l' && pos_width > jump2){ // Centralizando para esquerda
              pos_width -= jump2;
              servo_width.write(pos_width); 
              Serial.println(pos_width);
              direcao2 = 'n';
          }
      }
    }
  }
