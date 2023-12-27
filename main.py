# Complete project details at https://RandomNerdTutorials.com/micropython-bme680-esp32-esp8266/

from machine import Pin, I2C
from time import sleep
import ssd1306
from bme680 import *

# ESP32 - Pin assignment
i2c = I2C(scl=Pin(22), sda=Pin(21))
# ESP32 Pin assignment 
i2coled = I2C(scl=Pin(26), sda=Pin(27))
# ESP8266 - Pin assignment
#i2c = I2C(scl=Pin(5), sda=Pin(4))

bme = BME680_I2C(i2c=i2c)

oled_width = 128
oled_height = 32

oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2coled)

while True:
  try:
    temp = str(round(bme.temperature, 2)) + ' C'
    #temp = (bme.temperature) * (9/5) + 32
    #temp = str(round(temp, 2)) + 'F'
    
    hum = str(round(bme.humidity, 2)) + ' %'
    
    pres = str(round(bme.pressure, 2)) + ' hPa'
    
    gas = str(round(bme.gas/1000, 2)) + ' KOhms'

    print('Temperature:', temp)
    print('Humidity:', hum)
    print('Pressure:', pres)
    print('Gas:', gas)
    print('-------')
    
    oled.fill(0)
    oled.text('Temp:' + temp, 0, 0)
    oled.text('Hum:' + hum, 0, 12)
    oled.text('Pressr:' + pres, 0, 24)
    #oled.text('Gas:' + gas, 0, 36)
    oled.show()

  except OSError as e:
    print('Failed to read sensor.')
 
  sleep(5)
