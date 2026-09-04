import sys
import time
from demo_opts import get_device
from luma.core.render import canvas


def main():
    while True:
        with canvas(device) as draw:
            draw.rectangle(device.bounding_box, outline="white", fill="black")
            draw.text((30, 40), "Hello World", fill="white")


while True:
    try:
        device = get_device()
        main()
    except KeyboardInterrupt:
        pass