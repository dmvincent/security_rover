# security_rover
Simulation for a home-security rover using ROS and Gazebo

For Map Creation
Use security_rover_gmapping.launch to create a new map of your environment. 
This must be ran alongside keyboard_teleop.launch in ourder to control the rover.
DO NOT CHANGE THE LINEAR OR ANGULAR SPEED!
![Imgure Image](https://i.imgur.com/kJdzUuf.gif)


For Navigation
Use security_rover_navigation.launch to use Rviz to pass goal positions with the
"2D Nav Goal" button and watch as the rover navigates autonomously. This launch file
also starts up an HSV color filter demonstrating OpenCV image processing. Must have 
OpenCV libraries installed.
![Imgure Image](https://i.imgur.com/gPr1ExB.gif)
