// Source: https://www.upesy.com/blogs/tutorials/dht11-humidity-temperature-sensor-with-arduino-code-on-esp32-board

#include "DHT.h"

#define dhtPin 17
#define dhtType DHT11

DHT dht(dhtPin, dhtType);  // Declare the sensor

void setup() {
  // put your setup code here, to run once:

  Serial.begin(115200);
  dht.begin();

}

void loop() {
  // put your main code here, to run repeatedly:

  delay(1000);

  float h = dht.readHumidity();  // Read moisture content in %
  float t = dht.readTemperature();  // Read temperature in degrees Celsius
  float f = dht.readTemperature(true);  // Read temprature in Fahrenheit

  if (isnan(h) || isnan(t) || isnan(f)) {
    Serial.println("Failed reception");
    return;
  }

  Serial.print("Humidity: ");
  Serial.print(h);
  Serial.print("% Temperature: ");
  Serial.print(t);
  Serial.print("°C, ");
  Serial.print(f);
  Serial.println("°F");

}
