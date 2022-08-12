
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
