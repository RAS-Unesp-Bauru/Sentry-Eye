#include "Arduino.h"
#include "classes.h"

Python::Python(){}

char Python::bringSpeed()
    {
        if (Serial.available() > 0)
        {
            char speed = Serial.read();
        }
        return speed;
    }

int Python::setSpeed(char speed)
    {
        int numerical_speed = 0;
        switch(speed)
        {
            case 's':
                numerical_speed = 1;
                break
            case 'm':
                numerical_speed = 5;
                break
            case 'f':
                numerical_speed = 10;
                break
        }
        return numerical_speed
    }

void Python::followTarget(int numerical_speed)
    {
        if (Serial.available() > 0){
        char direcao = Serial.read();
  
            if(direcao == 't'){ // Centralizando para cima
                for (int pos_height = pos_height; pos_height <= 135; pos_height += numerical_speed){ // vai de 90 a 135 degrees na vertical
                servo_width.write(pos_height);
                Serial.println("Centralizando para cima");
                delay(15);                                                        // espera 15ms para o Servo alcançar a posição
                }
            }
        
            if(direcao == 'b'){ // Centralizando para baixo
                for (int pos_height = pos_height; pos_height >= 45; pos_height -= numerical_speed) { // vai de 90 a 45 degrees na vertical
                servo_width.write(pos_height);
                Serial.println("Centralizando para baixo");
                delay(15);
                }
            }
        
            if(direcao == 'r'){ // Centralizando para direita
                for (int pos_widht = pos_widht; pos_widht <= 135; pos_widht += numerical_speed) { // vai de 90 a 135 degrees na horizontal
                servo_width.write(pos_widht);
                Serial.println("Centralizando para direita");
                delay(15);
                }
            }
        
            if(direcao == 'l'){ // Centralizando para esquerda
                for (int pos_widht = pos_widht; pos_widht >= 45; pos_widht -= numerical_speed) { // vai de 90 a 45 degrees na horizontal
                servo_width.write(pos_widht); 
                Serial.println("Centralizando para esquerda");
                delay(15);
                }
            }
        } 
    }

Python piton = Python();