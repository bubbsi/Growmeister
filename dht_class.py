import adafruit_dht
import board

class DHTClass:
        def __init__(self, type, pin):
            self.dhtDevice = type(pin)     
        
        def exit(self):
            self.dhtDevice.exit()
        
        def get_values(self):
            temperature = self.dhtDevice.temperature
            humidity = self.dhtDevice.humidity
            human_readable = ('{0:0.1f}*  {1:0.1f}%'.format(temperature, humidity))
            return (temperature,humidity,human_readable)
                

if __name__=="__main__":
        dht = DHTClass(adafruit_dht.DHT22,board.D4)
        print(dht.get_values()[2])
        dht.exit()
