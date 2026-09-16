import sys
import board
import adafruit_dht
import json

# DHT22 connected to GPIO4
dht_sensor = adafruit_dht.DHT22(board.D4)

def main():
    try:
        temperature = dht_sensor.temperature
        humidity = dht_sensor.humidity

        # Send message in JSON format: msg.payload.<temp, hum, stat>
        print(json.dumps({
            "temperature": temperature,
            "humidity": humidity,
            "status": "running"
        }))

        
    except RuntimeError as err:
        # DHT22 readings occasionally fail; simply try again.
        print(json.dumps({
            "status": "error"
        }))


if __name__ == "__main__":
    try:
        main()    

    except KeyboardInterrupt:
        sys.exit()    