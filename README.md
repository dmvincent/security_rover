# security_rover
Security Rover ROS Gazebo Simulation

Use security_rover_gmapping.launch to create a new map of your environment. 
This must be ran alongside keyboard_teleop.launch in ourder to control the rover.
DO NOT CHANGE THE LINEAR OR ANGULAR SPEED!
![Imgure Image](https://i.imgur.com/kJdzUuf.gif)

Use security_rover_navigation.launch to use Rviz to pass goal positions with the
"2D Nav Goal" button and watch as the rover navigates autonomously. This launch file
also starts up an HSV color filter demonstrating OpenCV image processing.
![Imgure Image](https://i.imgur.com/SdeerUE.gif)
