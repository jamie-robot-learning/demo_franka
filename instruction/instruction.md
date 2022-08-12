# On GPU Labtop

### Source workspace for all terminals
source /opt/ros/melodic/setup.bash 

### Launch master node
roscore

### Launch camera node
roslaunch realsense2_camera rs_camera.launch

### Launch Rviz
rosrun rviz rviz -d /home/gpupc3/demo_jm/launch/demo.rviz

### Launch object detection node
##### First source workspace and venv
source ~/demo_jm/dvel/setup.bash
source ~/demo_jm/venv38/bin/activate
rosrun mask_rcnn_ros mask_rcnn_node



### Tactile ML
source ~/catkin_tofu_demo/devel/setup.sh
source ~/demo_tofu/bin/activate
cd /home/gpupc3/catkin_tofu_demo/src/tacniq_tactile_demo_rls/src/grasp_controller/grasp_prediction
python grasp_pred_onegrasp_ecoflex020822.py


# On Franka PC
### On Franka PC ###

roscore

roslaunch main_demo robot_bringup.launch

#### PID controller for the sensor
roslaunch pid_demo_rls grasp_controller_demo_rls.launch

#### robotiq controller
rosrun robotiq_2f_gripper_control Robotiq2FGripperRtuNode.py /dev/ttyUSB1 

rosrun ma_demo robotiq_remapper.py

#### Robotic testing
rosrun robotiq_2f_gripper_control Robotiq2FGripperSimpleController.py
#### test gripper using r,a

#### Franka controller
rosrun tacniq_tactile_demo_rls robot_tac_control.py

#### Tactile publisher
rosrun tacniq_tactile_demo_rls tactile_publisher_2Ffastgrasp_onegrasp_strict.py

#### tactile visualizer
source ~/demo_tofu/bin/activate
rosrun tacniq_tactile_demo_rls visualizer_tactileimage_strict.py



#### get q states
rostopic echo /franka_state_controller/franka_states/q

#### pub action
rostopic pub -1 target std_msgs/String action2



