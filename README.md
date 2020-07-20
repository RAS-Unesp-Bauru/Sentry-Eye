<p align="center">
  <a href="https://sites.google.com/unesp.br/rasunespbauru/home">
    <img src="https://lh6.googleusercontent.com/7MGu9_sdcTjHhBAZVLiFCo9OxALf8q2HeRyYoJAQgP-ikL6gg89vl_GHcY3cHynIv-5H-D8=w16383" alt="RAS logo" width="500" height="140">
  </a>
</p>

# Mechanical-Tracking-Eye
Track a specifc person in the camera motion range by their face characteristics, if its lost, an object tracking mechanism is activated with the same coordinates as the last known face position. Built upon "**ageitgey**" *face_recognition* neural network.

## Introduction
The project Sentry eye is a IEEE RAS Unesp Bauru's proposal to develop a camera that is capable of moving in all cartesian axis while searching a previous registered person, named as "target". The user is requested to take a photo with the camera and will be registered in doing so, then he will be asked to chose between three values of velocity, small, medium or fast, that will change the "softness" of the camera's movement. After that, delimiters for the face position will be created and will act as a response for the target getting to the sides, farther or closer to the camera's visual range. If it identifies the face, the camera will start to follow the target by utilizing the delimiters response, if it doesnt find it, it will start to move left and right in a sentry iddle mode.

The project's base ideia came from the haunted paintings present in animated shows, where it follows the protagonists when they walk nearby, and from the sentry turrets present in the game Portal 2. although the idea originally came from a comic perspective it was possible to see real life aplication, like permiting the camera to adjust the image of a professor doing lecture, removing the need for a operator always moving and positioning the best view angle.  

We belive that the project will help in disseminate technological interest and knowledge within the city we live in and even outside, besides helping anyone that finds this and wants to use it in any research activity.

## Features
### Set speed
![SetSpeed](https://user-images.githubusercontent.com/50799373/87962983-6b256100-ca8e-11ea-9323-0b8cdfa4bd4a.gif)

The chosen speed will determine the "softness" of the camera movement. Currently there are three options: slow, medium and fast. the code for this part is present in setSpeed.py. 

### Register the target(s):

![cadastro](https://user-images.githubusercontent.com/50799373/87958242-abcdac00-ca87-11ea-846c-bea392ff6ccd.gif)

The gif above show the process of creating a new folder records end registering a new person. The image you take is put on the folder and will be used later. The explict code is found in cadastro.py.



### Track registered target(s) with face recognition:
![part1](https://user-images.githubusercontent.com/50799373/87965162-b2612100-ca91-11ea-9ddf-b13c0c44826b.gif)

With registration set, the program will start to run firstly the face recognition funtion and compare the targets position with the delimeters coordinates. If the positions intersect, a response will come out as a print in the terminal or as a servo movement, if you have the hardware functioning.

### Track registered target(s) with Object Tracking:
![part2](https://user-images.githubusercontent.com/50799373/87966271-6c0cc180-ca93-11ea-8423-ddd048a7a9d9.gif)

If the registered target is lost, the program will run the object tracking mechanism, that will use the last known face position as a new object to be tracked, this helps compensate some situations where the face recognition underperforms. The delimiters continue to interact with the current target coordinates to generate a response.   


## Installation
### Requirements

The project was constructed in machines with Linux Ubuntu 16.04 LTS and superior. Alongside the following:
- 1


### Steps:
1. One
2. Two
3. Three

## Cheap camera building option
### Materias:
* X
* Y
* Z

### Building:
1. One
2. Two 
3. Three

## Conclusion
**Conluido**

## Infos
This project is part of RAS's branches, specifically, a Bauru RAS's project with the intend to help the reasearch area with new ideias and, consequently, develop it's members ability to work with modern robotic and automation problems.

### Team

> RAS Unesp Bauru

| <a href="https://github.com/Adribom" target="_blank">**Adriel Bombonato (Scrum Master)**</a> | <a href="https://github.com/paulo-gigliotti" target="_blank">**Paulo Gigliotti**</a> | <a href="https://github.com/ViniPilan" target="_blank">**Vinicius Pilan**</a> |
| :---: |:---:| :---:|
| [![FVCproductions](https://avatars3.githubusercontent.com/u/50799373?s=400&v=4)](http://fvcproductions.com)    | [![FVCproductions](https://avatars2.githubusercontent.com/u/54952751?s=400&v=4)](http://fvcproductions.com) | [![FVCproductions](https://avatars3.githubusercontent.com/u/62164353?s=400&v=4)](http://fvcproductions.com)  |
| <a href="https://github.com/Adribom" target="_blank">`github.com/Adribom`</a> | <a href="https://github.com/paulo-gigliotti" target="_blank">`github.com/paulo-gigliotti`</a> | <a href="https://github.com/ViniPilan" target="_blank">`github.com/ViniPilan`</a> |  
<br />
<br />

| <a href="https://github.com/Nodyer" target="_blank">**Nodyer dos Anjos**</a> | <a href="https://github.com/BrunoBicas" target="_blank">**Bruno Bicas**</a> | <a href="https://github.com/pecaldato" target="_blank">**Pedro Caldato (Product Owner)**</a> |
| :---: |:---:| :---:|
| [![FVCproductions](https://avatars0.githubusercontent.com/u/54998187?s=400&u=45d16bd7e80deba497d88e48095480315cf6555c&v=4)](http://fvcproductions.com)    | [![FVCproductions](https://avatars3.githubusercontent.com/u/54942242?s=400&v=4)](http://fvcproductions.com) | [![FVCproductions](https://avatars2.githubusercontent.com/u/28930766?s=400&u=f51ed8b47bf5fca020afa9967c51211b141a6dc6&v=4)](http://fvcproductions.com)  |
| <a href="https://github.com/Nodyer" target="_blank">`github.com/Nodyer`</a> | <a href="https://github.com/BrunoBicas" target="_blank">`github.com/BrunoBicas`</a> | <a href="https://github.com/pecaldato" target="_blank">`github.com/pecaldato`</a> |

### Support

- Website at <a href="https://sites.google.com/unesp.br/rasunespbauru/contato" target="_blank">`RAS Unesp Bauru`</a>
- Facebook at <a href="https://www.facebook.com/rasunespbauru/" target="_blank">`IEEE RAS Unesp Bauru`</a>
- Instagram at <a href="https://www.instagram.com/rasunespbauru/?hl=pt-br" target="_blank">`@rasunespbauru`</a>
- Email: rasbaurunesp@gmail.com





