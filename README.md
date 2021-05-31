Gesture Control Mouse Pointer using Color Detection - Version 1
===================================================================
+ The version 1 of this project used color detection technology to detect the position of the hand.
+ The project can be viewed [https://github.com/GhostlyPresence/GestureControlledMousePointer](here).
+ The problem with that approach was that user had to have something of green color in their hands.

Gesture Control Mouse Pointer using Hand Tracking - Version 2
===================================================================
+ This approach solves the problem of version 1.
+ The program used hand tracking technology to detect hands in the real time.
+ Mediapipe, a library buit by google, provides ready-to-use real time hand tracking and landmark estimation feature.
+ Although, using this model affects the FPS a little bit, but overall it was found to be a better solution.

To Run The Program
==================
+ The python version used here is python 3.8
+ Create a virtual enviroment with the python 3.8,
+ And simply run `pip install -r requirements.txt`
