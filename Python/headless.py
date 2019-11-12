import time

import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306
import Adafruit_LSM303

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
#@sudo python "/location/of the/ program/ callled/gg.py"
RST = 24

DC = 23
SPI_PORT = 0
SPI_DEVICE = 0
datalist = []

disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST, i2c_address=0x3D)
lsm303 = Adafruit_LSM303.LSM303()

disp.begin()

disp.clear()
disp.display()

width = disp.width
height = disp.height
image = Image.new('1', (width, height))


draw = ImageDraw.Draw(image)


draw.rectangle((0,0,width,height), outline=0, fill=0)


padding = 2
shape_width = 20
top = padding
bottom = height-padding

x = padding


font = ImageFont.load_default()


disp.image(image)
disp.display()
print('Printing accelerometer & magnetometer X, Y, Z axis values, press Ctrl-C to quit...')
collecting = True
KYLE = 1
draw = ImageDraw.Draw(image)
data = []
lastpoint = 10
X=  "a(m/s^2)"
Y=  "Time"
while True:
    accel, mag = lsm303.read()
    accel_x, accel_y, accel_z = accel
    accel_x *= KYLE
    accel_y *= KYLE
    accel_z *= KYLE

        #draw.text()
    if collecting:
        datalist.append(accel_z)
        if len(datalist) == 10:
            average = sum(datalist) / 10
            KYLE = 9.8 / average
            collecting = False 
    else:
        print('Accel X={0}, Accel Y={1}, Accel Z={2}'.format(
              accel_x, accel_y, accel_z))
        # Wait half a second and repeat.
        time.sleep(0.0001)
        if(len(data)>20):
            data.pop(0)
        data.append(accel_z)
        xpos = 18
        
        draw = ImageDraw.Draw(image)
        draw.rectangle((0,0,width,height), outline=0, fill=0)
        for i in data:
            draw.line(((xpos,2*int(i)+8),(xpos - 3, lastpoint)),fill=255)
            xpos += 3
            lastpoint = 2*int(i)+8
        draw.line(((15,5),(15,60)), fill = 255)
        draw.text((15,3),X,font=font,fill=255)
        draw.line(((15,60),(78,60)), fill = 255)
        draw.text((80,55),Y,font=font,fill=255)
        
        #draw.text((x, top),"accel z" + str(round(accel_z,3)) ,  font=font, fill=255)
        #draw.text((x, top+20),"accel x" + str(round(accel_x,3)), font=font, fill=255)
        #draw.text((x, top+40),"accel y" + str(round(accel_y,3)), font=font, fill=255)
        disp.image(image)
        disp.display()

