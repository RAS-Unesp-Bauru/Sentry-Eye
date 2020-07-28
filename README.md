<p align="center">
  <a href="https://sites.google.com/unesp.br/rasunespbauru/home">
    <img src="https://user-images.githubusercontent.com/50799373/88114032-6396b280-cb89-11ea-9de9-656eb9bc2d31.png" alt="RAS logo" width="500" height="140">
  </a>
</p>
<img width="2240" alt="Artboard 1sentry-eye" src="https://user-images.githubusercontent.com/50799373/88680061-7ac42b80-d0c6-11ea-8571-937653f87852.png">

# Mechanical-Tracking-Eye
Track a specifc person in the camera motion range by their face characteristics, if its lost, an object tracking mechanism is activated with the same coordinates as the last known face position. Built upon "**ageitgey**" *face_recognition* neural network.

## Introduction
The project Sentry eye is a IEEE RAS Unesp Bauru's proposal to develop a camera that is capable of moving in all cartesian axis while searching a previous registered person, named as "target". The user is requested to take a photo with the camera and will be registered in doing so, then he will be asked to chose between three values of velocity, small, medium or fast, that will change the "softness" of the camera's movement. After that, delimiters for the face position will be created and will act as a response for the target getting to the sides, farther or closer to the camera's visual range. If it identifies and recognize the face, the camera will start to follow the target by utilizing the delimiters response, if the face is obstructed or the person turn around, a object tracking algorithm will take place and, if neither is activated, it will start to move left and right in a sentry iddle mode.

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
![faceRec](https://user-images.githubusercontent.com/50799373/88597213-232dad80-d03d-11ea-9b07-23785beb1bba.gif)

With registration set, the program will start to run firstly the face recognition funtion and compare the targets position with the delimeters coordinates. If the positions intersect, a response will come out as a print in the terminal or as a servo movement, if you have the hardware functioning.

### Track registered target(s) with Object Tracking:
![objTracking](https://user-images.githubusercontent.com/50799373/88597653-19f11080-d03e-11ea-9929-7441fe0c8c1e.gif)

If the registered target is lost, the program will run the object tracking mechanism, that will use the last known face position as a new object to be tracked, this helps compensate some situations where the face recognition underperforms. The delimiters continue to interact with the current target coordinates to generate a response.   


## Installation

### Recommended

#### Anaconda
We recommend that you use Anaconda for organization purposes
- [How to install Anaconda on Linux, MacOS and Windows](https://github.com/Adribom/Mechanical-Tracking-Eye/blob/readme/installing-anaconda.md).

Then, create an environment with python 3.7
```
conda create -n envName python==3.7.0
```
And activate it
```
conda activate envName
```

### Requirements

The project was constructed in machines with Linux Ubuntu 16.04 LTS and superior. Alongside the following:

#### Python 3.7 and above
#### Git
- **Linux**:

  1. check if apt is up-to-date
  ```
  sudo apt-get update
  ```
  2. Then install git with the following command
  ```
  sudo apt-get install git-all
  ```
- **MacOS**:

  Most versions already come with git, but if you dont have it installed follow this steps

  1. Navigate to the latest [macOS Git Installer](https://sourceforge.net/projects/git-osx-installer/files/git-2.23.0-intel-universal-mavericks.dmg/download?use_mirror=autoselect) and download the latest version.
  2. Once the installer has started, follow the instructions as provided until the installation is complete.
  3. Open the command prompt "terminal" and type git version to verify Git was installed.

- **Windows**:
  1. Navigate to the latest [Git for Windows installer](https://gitforwindows.org/) and download the latest version.

  2. Once the installer has started, follow the instructions as provided in the **Git Setup** wizard screen until the installation is complete.

  3. Open the windows command prompt (or **Git Bash** if you selected not to use the standard Git Windows Command Prompt during the Git installation).

  4. Type git version to verify Git was installed.

More information [here](https://github.com/git-guides/install-git)

#### face-recognition 1.3.0

```
pip install face-recognition
```

>Note: it may take a while
#### OpenCV 4.1.0

```
pip install opencv-python
pip install opencv-contrib-python
```
#### Numpy 1.18.1
Usually comes with face-recognition or OpenCV, but you can also install with
```
pip install numpy
```
#### Imutils 0.5.3
```
pip install imutils
```
#### Pyserial 3.4
```
pip install pyserial
``` 

### Steps for execution:
1. Clone this repository
```
git clone https://github.com/Adribom/Mechanical-Tracking-Eye
```

2. Run `faster_cameraREC.py`, located inside the XXX folder
```
python faster_cameraREC.py
```
>Note: If the error `Gtk-Message: Failed to load module "canberra-gtk-module"` appear, enter `sudo apt-get install libcanberra-gtk-module`



## Hardware
Check this pdf over here :)

## Infos
This project is part of RAS's branches, specifically, a Bauru RAS's project with the intend to help the reasearch area with new ideias and, consequently, develop it's members ability to work with modern robotic and automation problems.

### Team

> Sentry Eye

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





