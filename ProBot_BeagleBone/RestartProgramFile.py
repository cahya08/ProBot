#!/usr/bin/python

# Python Standart Library Imports
import Adafruit_BBIO.GPIO as GPIO
import sys
import os
import math

# Local files
import ProBotConstantsFile
import SabertoothFile
import PWMFile
import mpu6050File

# Initialization of classes from local files
PWM = PWMFile.PWMClass()
Pconst = ProBotConstantsFile.Constants()
Sabertooth = SabertoothFile.SabertoothClass()
mpu6050=mpu6050File.mpu6050Class()

# Configuration the type of GPIO's
GPIO.setup(Pconst.RedLED, GPIO.OUT)


class RestartProgramClass():

    def RestartProgramRoutine(self):
	# Routine called when the angle is out of range or the admin stopped the mainRoutine and we need to restart the program
	Sabertooth.stopAndReset()
	PWM.PWMStop()
	
	GPIO.output(Pconst.GreenLED, GPIO.LOW)

	print "\nProBot angle's out of range or the admin stopped the mainRoutine!!!"
	print "\nRestarting the Program..."

   	python = sys.executable
    	os.execl(python, python, * sys.argv)
 
