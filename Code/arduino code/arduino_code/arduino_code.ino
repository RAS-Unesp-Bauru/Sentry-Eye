#include "Arduino.h"
#include <Servo.h>

int contador;
Servo servo_width;    // Horizontal
Servo servo_height;   // Vertical

//config params
int pos_width;    // Variável de posição na horizontal
int pos_height;   // Variável de posição na vertical
int jump;
char direcao;

void setup(){
  Serial.begin(9600);      // Velocidade padrão para comunicação
  //servo init config
  servo_width.attach(8);   // Horizontal no pino 9
  servo_height.attach(9); // Vertical no pino 10
  servo_width.write(90);     // Posição padrão setado em 90 graus (no meio)
  servo_height.write(90);
  pos_width = pos_height = 90;
  jump = 0;
  direcao = 5;
}

void loop(){
    
    if (Serial.available() > 0){
      
        String data_string = Serial.readString();

        if (data_string == "zero"){
          servo_width.write(90);     // Posição padrão setado em 90 graus (no meio)
          servo_height.write(90);

        }
        else{
          direcao = data_string.charAt(0);
          jump =  data_string.charAt(1) - 48;
          jump *= 10;
          Serial.println(direcao);
          Serial.println(jump);

          if(direcao == 't' && pos_height < 180 - jump){ // Centralizando para cima
              pos_height += jump;
              servo_height.write(pos_height);
              Serial.println(pos_height);
              direcao = 'n';
          }
        
          if(direcao == 'b' && pos_height > jump){ // Centralizando para baixo
              pos_height -= jump;  
              servo_height.write(pos_height);
              Serial.println(pos_height);
              direcao = 'n';
          }
          if(direcao == 'r' && pos_width < 180 - jump){ // Centralizando para direita
              pos_width += jump;  
              servo_width.write(pos_width);
              Serial.println(pos_width);
              direcao = 'n';
          }
          if(direcao == 'l' && pos_width > jump){ // Centralizando para esquerda
              pos_width -= jump;
              servo_width.write(pos_width); 
              Serial.println(pos_width);
              direcao = 'n';
          }
      }
    }
  }
