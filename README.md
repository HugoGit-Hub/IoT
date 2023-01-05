--------------------------- PRESENTATION ---------------------------

Api used to receive data from sensors (temperature and humidity sensors)

The frame received is translated from hexadecimal frame to readable datas like :
  - purcentage of humidity
  - temperature in Celsuis
  - threshold point for humidity dans temperature
  
Then, you can configure it on Grafana by connecting them by InfluxDB Api

--------------------------- PREREQUISITES ---------------------------

- Python 3.11 & older
  - virtual environment
  - flask
  - influxdb-client
- Sensors simulator (devloped in javascript)
- NodeJs latest version
- InfluxDB 
- [Optoinal] Grafana

--------------------------- INSTALLATION ----------------------------

This project is devloped in python, using Flask framework, here are instructions of configurations :
  - create a virutal environnement :
    - cd /you/path/folder/
    - python3 -m venv venv
  - activate virtual environment :
    - ./venv/Scripts/activate
  - change directory to venv :
    - cd ./venv
  - create folder in venv, clone git repository on it, install libraries :
    - mkdir TP
    - git clone https://github.com/HugoGit-Hub/IoT
    - pip3 install flask influxdb-client
    
--------------------------- CONFIGURATION ---------------------------

Do not forget to change url, bucket and token, organisation in writeInfluxDB function
