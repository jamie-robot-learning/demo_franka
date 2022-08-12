#!/bin/sh

if [ -n "$DESTDIR" ] ; then
    case $DESTDIR in
        /*) # ok
            ;;
        *)
            /bin/echo "DESTDIR argument must be absolute... "
            /bin/echo "otherwise python's distutils will bork things."
            exit 1
    esac
fi

echo_and_run() { echo "+ $@" ; "$@" ; }

echo_and_run cd "/home/gpupc3/demo_jm/src/mask_rcnn_ros"

# ensure that Python install destination exists
echo_and_run mkdir -p "$DESTDIR/home/gpupc3/demo_jm/install/lib/python2.7/dist-packages"

# Note that PYTHONPATH is pulled from the environment to support installing
# into one location when some dependencies were installed in another
# location, #123.
echo_and_run /usr/bin/env \
    PYTHONPATH="/home/gpupc3/demo_jm/install/lib/python2.7/dist-packages:/home/gpupc3/demo_jm/build/lib/python2.7/dist-packages:$PYTHONPATH" \
    CATKIN_BINARY_DIR="/home/gpupc3/demo_jm/build" \
    "/usr/bin/python2" \
    "/home/gpupc3/demo_jm/src/mask_rcnn_ros/setup.py" \
     \
    build --build-base "/home/gpupc3/demo_jm/build/mask_rcnn_ros" \
    install \
    --root="${DESTDIR-/}" \
    --install-layout=deb --prefix="/home/gpupc3/demo_jm/install" --install-scripts="/home/gpupc3/demo_jm/install/bin"
