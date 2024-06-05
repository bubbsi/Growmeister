from time import sleep, time
from luma.core.interface.serial import i2c
from luma.oled.device import sh1106, ssd1306
from adafruit_dht import DHT22, DHT11
from os.path import dirname
import board
import asyncio
import logging

from kasa_class import KasaClass
from oled_class import OLEDCLass
from dht_class import DHTClass

# Config
SMARTPLUGIP = "192.168.0.5"
THRESTEMPERATUR = 27
THRESHUMIDITY = 70
FANEXECUTIONTIME = 1800

# returns the current timestamp
def get_timestamp():
	return int(time())

async def main():
    # initalize logging to file clima_controller.log in working directory
    logging.basicConfig(filename=f'{dirname(__file__)}/clima_controller.log', encoding='utf-8', level=logging.INFO, format='%(asctime)s %(levelname)s: %(message)s', datefmt='%d.%m.%Y %H:%M:%S')
    
    # try to initalize Smartplug
    try:
        plug = KasaClass(SMARTPLUGIP)
        await plug.update()
    except Exception as error:
        logging.error(f"Error initialize SmartPlug: {error}")
        raise error
    
    # initalize OLED display
    try:
        display = OLEDCLass(sh1106,i2c(port=1, address=0x3c))
    except Exception as error:
        logging.error(f"Error initialize OLED Display: {error}")
        raise error
    
    # try to initalize DHT Sensor
    try:
        sensor = DHTClass(DHT22,board.D4)
    except Exception as error:
        logging.error(f"Error initialize SmartPlug: {error}")
        raise error
    
    # if all devices up, print Ready on display
    message = "Ready"
    print(message)
    logging.info(message)
    display.draw_text(message)

    # get the current timestamp
    wait_until = get_timestamp()
    # start the main loop for controll the humidity and temperature
    try:
        while True:
            # get the current timestamp
            curr_timestamp = get_timestamp()
            await plug.update() 

            # get the temperature and humidity values, continue the main loop after 10 seconds by runtime exception, because sometimes there are errors while reading from DHT sensors
            try:
                (temperature, humidity, human_readable) = sensor.get_values()
            except RuntimeError as error:
                logging.error(f"DHT Runtime Exception: {error}")
                display.draw_text("DHTReadErr")
                sleep(10)
                continue
            
            # print out the current humidity and temperature values in human_readable format
            print(human_readable, end="\r")
            display.draw_text_with_header("Temp. Luft.",human_readable)

            # activate plug if needed for 30 minutes
            if temperature > THRESTEMPERATUR or humidity > THRESHUMIDITY:
                if curr_timestamp >= wait_until:
                    wait_until = get_timestamp() + FANEXECUTIONTIME
					
                if not plug.is_on():
                    await plug.turn_on()	

			# otherwise turn the plug off		
            elif plug.is_on():
                if curr_timestamp > wait_until:
                    await plug.turn_off()

            sleep(10)
    
    # catch exceptions
    # exits when you press CTRL+C  
    except KeyboardInterrupt:   
        print("\nStopping...")
        logging.info("Stopping...")
        
    # if something unexpectedly goes wrong
    except Exception as error:
        display.draw_text("unexpected error")
        logging.error(f"Exception: {error}")
        raise error

    finally:
        # finally cleaning up
        logging.info("Cleaning up...")
        print("Cleaning up...")
        sensor.exit()

#start the main function
if __name__=="__main__":
	asyncio.run(main())
