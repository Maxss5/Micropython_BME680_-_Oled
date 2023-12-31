# Micropython_BME680_-_Oled
Ficheros necesarios para obtener datos de temperatura, humedad, presión y gas y mostrar en una pantalla oled 128x32

---
__ESP32 Pages :)__

- __[BME680 sensor](https://randomnerdtutorials.com/micropython-bme680-esp32-esp8266/)__ - BME680 with ESP32 (Temperature, Humidity, Pressure, Gas).
- __[SSD1306 Oled](https://randomnerdtutorials.com/micropython-oled-display-esp32-esp8266/)__ - OLED Display with ESP32


---

## ESP8266 (Temperature, Humidity, Pressure, Gas) and SSD1306 (OLED Display 128x32)   8-)

---

**A continuación como deben ser las conexiones del sensor y pantalla oled con la placa ESP32**

### ESP32 vs BME680 Sensor

| Puerto ESP32 | Pin en el sensor |
| ------------ | ---------------- |
| P22    | Puerto SCL en el sensor BME680. |
| P21    | Puerto SDA en el sensor BME680. |
| 3.3V   | Positivo (VCC) en el sensor BME680. |
| GND    | Puerto tierra (GND) en el sensor BME680.  |

### ESP32 vs SSD1306 Oled

| Puerto ESP32 | Pin en el sensor |
| ------------ | ---------------- |
| P26    | Puerto SCK en la OLED SSD1306. |
| P27    | Puerto SDA en la OLED SSD1306. |
| 3.3V   | Positivo (VCC) en el sensor BME680. |
| GND    | Puerto tierra (GND) en el sensor BME680.  |


## Images

![ESP32 Placa](https://github.com/Maxss5/Micropython_BME680_-_Oled/blob/develop/images/ESP32Board.png "Placa ESP32")
![SSD1306 Oled Funcionando](https://github.com/Maxss5/Micropython_BME680_-_Oled/blob/develop/images/ssd1306_OLED.png "Oled SSD1306")
![bme680 Sensor](https://github.com/Maxss5/Micropython_BME680_-_Oled/blob/develop/images/bme680Sensor.png "Sensor BME6806")
