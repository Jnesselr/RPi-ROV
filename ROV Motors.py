__author__ = 'dbailey6'

import #my motor class

frontRightHorDir = 0 #Need to determine pin
frontRightHorPWM = 0 #Need to determine pin
frontLeftHorDir = 0 #Need to determine pin
frontLeftHorPWM = 0 #Need to determine pin
backRightHorDir = 0 #Need to determine pin
backRightHorPWM = 0 #Need to determine pin
backLeftHorDir = 0 #Need to determine pin
backLeftHorPWM = 0 #Need to determine pin

frontRightVerDir = 0 #Need to determine pin
frontRightVerPWM = 0 #Need to determine pin
frontLeftVerDir = 0 #Need to determine pin
frontLeftVerPWM = 0 #Need to determine pin
backRightVerDir = 0 #Need to determine pin
backRightVerPWM = 0 #Need to determine pin
backLeftVerDir = 0 #Need to determine pin
backLeftVerPWM = 0 #Need to determine pin


frontRightHor = motor(frontRightHorDir, frontRightHorPWM)
frontLeftHor = motor(frontLeftHorDir, frontLeftHorPWM)

backRightHor = motor(backRightHorDir, backRightHorPWM)
backLeftHor = motor(backLeftHorDir, backLeftHorPWM)

frontRightVer = motor(frontRightVerDir, frontRightVerPWM)
frontLeftVer = motor(frontLeftVerDir, frontLeftVerPWM)

backRightVer = motor(backRightVerDir, backRightVerPWM)
backLeftVer = motor(backLeftVerDir, backLeftVerPWM)


