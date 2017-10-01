#!/usr/bin/python
import sys
import Adafruit_DHT
import wiringpi
import time

class HVAC:

    def __init__(self):
        ###############################
        # Mapping relays to GPIO pins #
        ###############################
        self._FAN_PIN = 17
        self._COMPRESSOR_PIN = 27
        self._COOL_PIN = 22
        # Initialize WiringPi for GPIO usage
        wiringpi.wiringPiSetupGpio()
        wiringpi.pinMode(self._FAN_PIN, 1)
        wiringpi.pinMode(self._COMPRESSOR_PIN, 1)
        wiringpi.pinMode(self._COOL_PIN, 1)

    def turn_ac_on(self):
        self.turn_fan_on()
        self.turn_compressor_on()
        self.turn_cool_on()

    def turn_ac_off(self):
        self.turn_fan_off()
        self.turn_compressor_off()
        self.turn_cool_off()

    def get_temperature_humidity(self):
        humidity, temperature = Adafruit_DHT.read_retry(11, 4)
        return humidity, temperature

    def get_fan_status(self):
        return wiringpi.digitalRead(self._FAN_PIN)

    def get_compressor_status(self):
        return wiringpi.digitalRead(self._COMPRESSOR_PIN)

    def get_cool_status(self):
        return wiringpi.digitalRead(self._COOL_PIN)

    def turn_fan_on(self):
        wiringpi.digitalWrite(self._FAN_PIN, 0)

    def turn_fan_off(self):
        wiringpi.digitalWrite(self._FAN_PIN, 1)

    def turn_compressor_on(self):
        wiringpi.digitalWrite(self._COMPRESSOR_PIN, 0)

    def turn_compressor_off(self):
        wiringpi.digitalWrite(self._COMPRESSOR_PIN, 1)

    def turn_cool_on(self):
        wiringpi.digitalWrite(self._COOL_PIN, 0)

    def turn_cool_off(self):
        wiringpi.digitalWrite(self._COOL_PIN, 1)
