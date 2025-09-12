import RPI.GPIO as GPIO # Import Raspberry Pi GPIO library
import time
from dotenv import load_dotenv
import os

class Movement: 
    DIR = 20   # Direction GPIO Pin
    STEP = 21  # Step GPIO Pin
    DELAY = 0.005 # Delay between steps
    CW = 1     # Clockwise Rotation
    CCW = 0    # Counterclockwise Rotation
    SPR = 200  # Steps per Revolution (360 / 1.8)
    current_position = 0  # Current position in steps
    LIMIT = int(os.getenv("LIMIT_PIN")) # GPIO pin sample can be replaced with any other pin 

    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.DIR, GPIO.OUT)
        GPIO.setup(self.STEP, GPIO.OUT)
        GPIO.setup(self.LIMIT, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.output(self.DIR, self.CW)
    
    def step(self, steps=100, direction=1):
        """Rotate motor a given number of steps unless limit is hit."""
        GPIO.output(self.DIR, direction)
        for _ in range(steps):
            if GPIO.input(self.LIMIT) == GPIO.LOW:  # Stop if switch is pressed
                print("⛔ Limit switch activated. Stopping.")
                break
            GPIO.output(self.STEP, GPIO.HIGH)
            time.sleep(self.DELAY)
            GPIO.output(self.STEP, GPIO.LOW)
            time.sleep(self.DELAY)