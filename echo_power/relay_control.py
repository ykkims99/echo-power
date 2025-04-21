
import RPi.GPIO as GPIO

RELAY_PIN = 17

def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(RELAY_PIN, GPIO.OUT)

def trigger_relay(state=True):
    GPIO.output(RELAY_PIN, GPIO.HIGH if state else GPIO.LOW)
