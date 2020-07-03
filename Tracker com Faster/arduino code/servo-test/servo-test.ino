#include "Arduino.h"
#include <Servo.h>
#include "classes.h"

Servo servo_width;    // Horizontal
Servo servo_height;   // Vertical

//config params
int pos_width;    // Variável de posição na horizontal
int pos_height;   // Variável de posição na vertical
int speed;
int numerical_speed;

void setup() {
  
  Serial.begin(9600);      // Velocidade padrão para comunicação
  
  //servo init config
  servo_width.attach(9);   // Horizontal no pino 9
  servo_height.attach(10); // Vertical no pino 10
  servo_width.write(90);     // Posição padrão setado em 90 graus (no meio)
  servo_height.write(90);
}
/*
void velocity(int pos, int ms){
  for (pos = pos; pos <= 45; pos += 1) { // vai de 0 a 45 degrees na vertical
          servo_width.write(pos_height) 
          Serial.println("Centralizando");
          delay(ms);
  }
}

int python(){ // Função que retorna a direção + velocidade
 if (Serial.available() > 0){
     char direcao = Serial.read()

     if(direcao == "t"){ //Direção de rotação
       for (pos_height = pos_height; pos_height <= 135; pos_height += 1) { // vai de 90 a 135 degrees na vertical
         servo_width.write(pos_height) 
         Serial.println("Centralizando para cima");
         delay(15);                                                        // espera 15ms para o Servo alcançar a posição
       }
     }

     if(direcao == "b"){ //Direção de rotação
       for (pos_height = pos_height; pos_height >= 45; pos_height -= 1) { // vai de 90 a 45 degrees na vertical
         servo_width.write(pos_height) 
         Serial.println("Centralizando para baixo");
         delay(15);
       }
     }

     if(direcao == "r"){ //Direção de rotação
       for (pos_widht = pos_widht; pos_widht <= 135; pos_widht += 1) { // vai de 90 a 135 degrees na horizontal
         servo_width.write(pos_widht) 
         Serial.println("Centralizando para direita");
         delay(15);
       }
     }

     if(direcao == "l"){ //Direção de rotação
       for (pos_widht = pos_widht; pos_widht >= 45; pos_widht -= 1) { // vai de 90 a 45 degrees na horizontal
         servo_width.write(pos_widht) 
         Serial.println("Centralizando para esquerda");
         delay(15);
       }
     }
}
*/

void loop(){

  speed = piton.bringSpeed();
  numerical_speed = piton.setSpeed(speed);
  piton.followTarget(int numerical_speed)

  /*
  if (Serial.available() > 0){
      char direcao = Serial.read();
  
      if(direcao == 't'){ // Centralizando para cima
        for (int pos_height = pos_height; pos_height <= 135; pos_height += 1) { // vai de 90 a 135 degrees na vertical
          servo_width.write(pos_height);
          Serial.println("Centralizando para cima");
          delay(15);                                                        // espera 15ms para o Servo alcançar a posição
        }
      }
  
      if(direcao == 'b'){ // Centralizando para baixo
        for (int pos_height = pos_height; pos_height >= 45; pos_height -= 1) { // vai de 90 a 45 degrees na vertical
          servo_width.write(pos_height);
          Serial.println("Centralizando para baixo");
          delay(15);
        }
      }
  
      if(direcao == 'r'){ // Centralizando para direita
        for (int pos_widht = pos_widht; pos_widht <= 135; pos_widht += 1) { // vai de 90 a 135 degrees na horizontal
          servo_width.write(pos_widht);
          Serial.println("Centralizando para direita");
          delay(15);
        }
      }
  
      if(direcao == 'l'){ // Centralizando para esquerda
        for (int pos_widht = pos_widht; pos_widht >= 45; pos_widht -= 1) { // vai de 90 a 45 degrees na horizontal
          servo_width.write(pos_widht); 
          Serial.println("Centralizando para esquerda");
          delay(15);
        }
      }
  }  
  */  
}
