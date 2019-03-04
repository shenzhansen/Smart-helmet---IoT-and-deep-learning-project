# Smart-helmet---IoT-and-deep-learning-project
Includes codes for data transmission and RCNN object detecction

Our smart helmet is designed for cyclists that provides useful features and extra safety support. It employs cutting-edge navigation technology and state-of-the-art neural network object detection to steer the cyclists away from danger. 

Motivation
● More and more people enjoy cycling because it is healthy and environmentally friendly;
● Bikes generally don’t offer mounting space for assistance devices or smartphone; 
● Cyclists are interested in tracking their health status when considering cycling as a sport; 
● Few bikes have rear view mirrors, and cyclists are unaware of the traffic behind unless purposely looking back, which imposes danger.

Architecture
The whole system mainly consists of three parts: 
● The raspberry pi placed on top of the helmet provides voice interaction and navigation; the Google vision kit placed on the rear is incorporated to detect cars and provide safety warnings; a solar panel on top of the helmet provides the power. 
● AWS server and database are running on the cloud to process and store client trip information and health statistics. 
● All of the user formations can be visualized on our website: http://guosl.com/iot/.

Technical Components

● Raspberry Pi is used as the main controller;
● User portal website presents trip information and health statistics;
● Google API is used to provide audio navigation;
● User data is stored in a cloud database;
● Google vision kit is used to monitor the rear view;
● All components are powered by solar energy.

Prototype
We have developed a prototype for our smart helmet project as shown below. It provides most of the feature in our initial design. We have also made a custom case using 3D printing for the rearview camera and mounted it on the helmet. A solar power bank is placed on top of the helmet to provide power to both the raspberry pi and the rearview camera.

References
● AIY Vision Kit from Google. (n.d.). Retrieved from https://aiyprojects.withgoogle.com/vision/
● G. (2018, August 03). Google/aiyprojects-raspbian. Retrieved from https://github.com/google/aiyprojects-raspbian
● T. (2018, October 03). Tensorflow/models. Retrieved from https://github.com/tensorflow/models/tree/master/research/object_detection
● Google Map Platform. Retrieved from https://developers.google.com/maps/documentation/directions/intro
