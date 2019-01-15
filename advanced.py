import RoboPiLib as RPL
import setup
import post_to_web as PTW

lmotor = 0
rmotor = 1

d1 = 16
d2 = 17

while True:
  d1read = RPL.digitalRead(d1)
  d2read = RPL.digitalRead(d2)
  
  
  if d1read == 1 and d2read == 1:
    RPL.servoWrite(lmotor,1400)
    RPL.servoWrite(rmotor,1600)
  elif d1read == 0 or d2read == 0:
    RPL.servoWrite(lmotor,1500)
    RPL.servoWrite(rmotor,1500)
  elif d1read == 0 and d2read == 0:
    RPL.servoWrite(lmotor,0)
    RPL.servoWrite(rmotor,0)
    print('so long comerade')
    exit()
    
    
  PTW.state['d1'] = d1read
  PTW.state['d2'] = d2read
  PTW.state['m1'] = RPL.servoRead(lmotor)
  PTW.state['m2'] = RPL.servoRead(rmotor)
  PTW.post()
