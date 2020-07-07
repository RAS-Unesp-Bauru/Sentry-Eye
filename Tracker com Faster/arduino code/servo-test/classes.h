#include "Arduino.h"
#ifndef classes_h
#define classes_h

class Python{
    private:


    public:

        Python();

        char bringSpeed();
        int setSpeed(char speed);
        void followTarget(int numerical_speed);
        void survey();

}

extern Python piton;

#endif