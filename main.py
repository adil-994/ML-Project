from sensor.exception import SensorException
import sys
import os
from sensor.logger import logging
def test_sensor_exception():
    try:
        logging.info("Testing SensorException")
        a=1/0
        # raise ValueError("This is a test exception")
    except Exception as e:
        raise SensorException(e, sys) from e



if __name__ == "__main__":
    try:
       test_sensor_exception()
    except Exception as e:
        print(e)