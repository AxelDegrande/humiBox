# humiBox
humiBox is an automated humidity-control system for a box or enclosed environment. It uses a temperature and humidity sensor to monitor the conditions inside the box and Node-RED to control the system. The sensor data is continuously recorded, and a daily plot is automatically generated and sent by email.


## How it works
The system consists of a sensor, Python scripts, Node-RED, and a CSV data file.

             +---------------------+
             | Temperature /       |
             | Humidity Sensor     |
             +---------------------+
                        |
                        |
             +---------------------+
             | getTempHumSenor.py  |
             |                     |
             | Reads sensor data   |
             +---------------------+
                        |
                        |
             +---------------------+
             |      Node-RED       |
             |                     |
             | Control & logging   |
             +---------------------+
                        |
                        |
             +---------------------+
             |    measurements     |
             |       (.csv)        |
             +---------------------+
                        |
                  Every day 23:00
                        |
                        |
             +---------------------+
             | Python plot script  |
             |                     |
             | Creates daily plot  |
             +---------------------+

## Setup

### 1. Clone the repository
```
git clone https://github.com/AxelDegrande/humiBox.git
cd humiBox
```
### 2. Install Python dependencies

Install the required Python packages:
```
pip install -r dependancies.txt
```


## Data format
The measurement.csv contains following data:
```
time,temperature,humidity,status
2026-10-05 15:44:07,23.4,56.7,running
2026-10-05 15:49:07,23.6,55.7,running
```
