execute_process(COMMAND "/home/gpupc3/demo_jm/build/mask_rcnn_ros/catkin_generated/python_distutils_install.sh" RESULT_VARIABLE res)

if(NOT res EQUAL 0)
  message(FATAL_ERROR "execute_process(/home/gpupc3/demo_jm/build/mask_rcnn_ros/catkin_generated/python_distutils_install.sh) returned error code ")
endif()
