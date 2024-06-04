from luma.core.interface.serial import i2c
from luma.core.render import canvas
from time import sleep
from luma.oled.device import sh1106, ssd1306
from PIL import ImageFont, ImageDraw, Image

class OLEDCLass:
    def __init__(self,device,serial):
        self.device = device(serial)
        self.headerFont = ImageFont.truetype('FreeMono.ttf',12)
        self.textFont = ImageFont.truetype('FreeSans.ttf',22)
    
    def draw_text(self,text):
        with canvas(self.device) as draw:
            draw.text((5,35), text, font = self.textFont, fill = "white")
    
    def draw_text_with_header(self,header,text):
        with canvas(self.device) as draw:
            draw.text((5,5), header, font = self.headerFont, fill = "white")
            draw.text((5,35), text, font = self.textFont, fill = "white")

if __name__=="__main__":
    oled = OLEDCLass(sh1106,i2c(port=1, address=0x3c))
    oled.draw_text("Hello World!")
    sleep(10)