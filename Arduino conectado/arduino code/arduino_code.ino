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
String string;

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
  string = "";
}

void loop(){
    
    if (Serial.available() > 0){
      
        string = Serial.readString();
        direcao = string.charAt(0);
        jump =  string.charAt(1) - 48;
      	//Serial.println(direcao);
      	//Serial.println(jump);

        if(direcao == 't'){ // Centralizando para cima
            pos_height += jump;
          	servo_height.write(pos_height);
            Serial.println(pos_height);
        	  direcao = 'n';
        }
      
        if(direcao == 'b'){ // Centralizando para baixo
          	pos_height -= jump;  
         	  servo_height.write(pos_height);
            Serial.println(pos_height);
            direcao = 'n';
        }
        if(direcao == 'r'){ // Centralizando para direita
          	pos_width += jump;  
          	servo_width.write(pos_width);
            Serial.println(pos_width);
            direcao = 'n';
        }
        if(direcao == 'l'){ // Centralizando para esquerda
            pos_width -= jump;
          	servo_width.write(pos_width); 
            Serial.println(pos_width);
            direcao = 'n';
        }
    }
}
