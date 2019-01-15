#    Add this code to index.html in the robo-html directory
#    <img src="https://192.168.21.XXX:8080/?action=stream">
###
#    start camera with /home/student/start_camera.sh
#    connect to 192.168.21.XXX
#    XXX = sd card number

import RoboPiLib as RPL
#controller code
import setup
#controller start
import post_to_web as PTW
#website

digital_sensor1 = 16

while True:
  PTW.state['d1'] = RPL.digitalRead(digital_sensor1)
  PTW.post()
