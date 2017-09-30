# Pimostat
Pi controlled HVAC

Our approach to a "smart" thermostat. This is our take on the Raspberry Pi thermostat. Complete with Web interface and Android app to set desired temperature and pre-schedule temperatures. 


The project is split into 3 levels by hardware.

Raspbery Pi - Turns on/off the AC and returns current temperature

Server - Hosts the REST API to communicate with web and Android apps. Logs temperature and on/off commands. And attemps to achieve the desired temp. 

Web/Android app - The interface to set the desired temperature and set up scheduled times. Also view graphical representation of logs

