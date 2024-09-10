# spacemouse_ros

## Installation Instructions

1. **Install libhidapi-dev**:
     ```sh
     sudo apt-get install libhidapi-dev
     ```

2. **Install Pyspacemouse**:
     ```sh
     pip install pyspacemouse
     ```

3. **Set up SpaceMouse Permissions**:
     ```sh
     sudo echo 'KERNEL=="hidraw*", SUBSYSTEM=="hidraw", MODE="0664", GROUP="plugdev"' > /etc/udev/rules.d/99-hidraw-permissions.rules
	 sudo usermod -aG plugdev $USER
	 newgrp plugdev
     ```

4. **Clone this repository into your catkin workspace**:
     ```sh
     cd /path/to/catkin_ws/src
     git clone https://github.com/iamlab-cmu/spacemouse_ros.git
     ```

5. **Build the package using catkin_make or catkin build**:
     ```sh
     cd /path/to/catkin_ws
     catkin_make
     catkin build
     source devel/setup.bash
     ```

## Running Instructions
1. **Start the SpaceMouse Server**:
     ```sh
     rosrun spacemouse_ros spacemouse_server.py
     ```