from kasa import SmartPlug as kasaSmartPlug
from time import sleep, time
import asyncio

class KasaClass:
    def __init__(self, ip):
        self.plug = kasaSmartPlug(ip)

    async def update(self):
        try:
            await self.plug.update()
        except:
            print("Error updating SmartPlug")
            sleep(10)
            await self.update()

    def is_off(self):
        return self.plug.is_off

    def is_on(self):
        return self.plug.is_on
    
    async def turn_on(self):
        try:
            await self.plug.turn_on()
        except:
            print("Error turning on SmartPlug")
            sleep(10)
            await self.turn_on()

    async def turn_off(self):
        try:
            await self.plug.turn_off()
        except:
            print("Error turning on SmartPlug")
            sleep(10)
            await self.turn_off()

SMARTPLUGIP = "192.168.0.1"
async def main():
    print("Looking for SmartPlug")
    plug = KasaClass(SMARTPLUGIP)
    await plug.update()
    if plug.is_off():
        print("Turning device on")
        await plug.turn_on()
    else:
        print("Turning device off")
        await plug.turn_off()

if __name__=="__main__":
    asyncio.run(main())
    
    
