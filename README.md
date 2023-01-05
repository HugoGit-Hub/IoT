Api used to receive data from sensors (temperature and humidity sensors)

The frame received is translated from hexadecimal frame to readable datas like :
  - purcentage of humidity
  - temperature in Celsuis
  - threshold point for humidity dans temperature
  
Then, you can configure it on Grafana by connecting them by InfluxDB Api

This project is devloped in python, using Flask framework, here are instructions of configurations :
  create a virutal environnement :
    cd /you/path/folder/
    
