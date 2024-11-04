import os, subprocess, time, sys

arguments = sys.argv[1:]

commands = [
    """
    sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'
    """,
    "sudo apt install curl",
    "curl -s https://raw.githubusercontent.com/ros/rosdistro/master/ros.asc | sudo apt-key add -",
    "sudo apt update",
    "sudo apt install ros-noetic-desktop",
    "source /opt/ros/noetic/setup.bash",
    "sudo apt install python3-rosdep python3-rosinstall python3-rosinstall-generator python3-wstool build-essential",
    "sudo apt install python3-rosdep",
    "sudo rosdep init",
    "rosdep update",
    "mkdir -p /Documents/21BRS1264/catkin_ws/src",
    """echo "source /opt/ros/noetic/setup.bash" >> ~/.bashrc""",
    "source ~/.bashrc",
]


for command in commands:
    try:
        subprocess.run(command, shell=True, check=True)
        print(f"Command '{command}' executed successfully.")

    except subprocess.CalledProcessError as e:
        print(f"Error executing command '{command}': {e}")
        exit(0)

os.chdir(f"/Documents/21BRS1264/catkin_ws")


try:
    subprocess.run("catkin_make", shell=True, check=True)

except subprocess.CalledProcessError as e:
    print(f"Error executing command creating folder: {e}")

os.chdir("/src")

try:
    subprocess.run(
        f"catkin_create_pkg {arguments[0]} std_msgs rospy turtlesim",
        shell=True,
        check=True,
    )
except subprocess.CalledProcessError as e:
    print(f"Error executing command creating folder: {e}")

os.chdir("..")

try:
    subprocess.run("catkin_make", shell=True, check=True)
except subprocess.CalledProcessError as e:
    print(f"Error executing command creating folder: {e}")

print("successfully completed ros setup.")
