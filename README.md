# robo-web
Basic files for posting camera and motor stakes on kitbot website
go to your dashboard https://192.168.21.XXX
XXX = sd card number

# Basic
run basic.py to see one digital sensor being read on the dashboard

# Advanced
run advanced.py to see 2 digital sensors and 2 motors on the dashboard

# Camera
Add this code to index.html in the robo-html directory
<img src="https://192.168.21.XXX:8080/?action=stream"
Then, on the RoboPi type /home/student/start_camera.sh into the shell to start the camera
