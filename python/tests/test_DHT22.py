import time
import sys
import board
import adafruit_dht

# DHT22 connected to GPIO4
dht_sensor = adafruit_dht.DHT22(board.D4)

try:
    try:
        temperature = dht_sensor.temperature
        humidity = dht_sensor.humidity

        print(f"Temperature: {temperature:.1f} C")
        print(f"Humidity:    {humidity:.1f} %")
        print(" ")

    except RuntimeError as err:
        # DHT22 readings occasionally fail; simply try again.
        print(f"Reading failed: {err}")

        time.sleep(2)

except KeyboardInterrupt:
    sys.exit()