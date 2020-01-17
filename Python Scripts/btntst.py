#!/usr/bin/env python3

from picamera import PiCamera
from time import sleep
from gpiozero import Button
import RPi.GPIO as GPIO
import time
import color_type as cT
import color_detect as cD
import color_match as cM
import read_model as rM
import image as im
import subprocess
from PIL import Image

def run_match(imgName):
    rgb = cD.get_average_color(imgName)
    cloth_type = rM.read_model(imgName)

    color_type = cT.Color_type(rgb)
    color_match = cM.colorMatch(2, color_type, cloth_type)

    #output = im.showClothing(cloth_type, color_match)
    #proc = subprocess.Popen("php /home/pi/OutfitRaspberryPi/index.php", shell=True, stdout=subprocess.PIPE)
    #script_response = proc.stdout.read()
    import slideshow as sL

def do_everything(name):
    GPIO.setup(18, GPIO.OUT)
    GPIO.output(18, GPIO.HIGH)
    camera.capture(name)
    camera.stop_preview()
    run_match(name)



GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

button = Button(17)
camera = PiCamera()

imgName = '/home/pi/Desktop/img5.jpg'

camera.start_preview()
button.wait_for_press()
button.when_pressed = do_everything(imgName)



