#include <FastLED.h>
#include <WiFi.h>
#include <WiFiClientSecure.h>
#include <HTTPClient.h>
#include <Wire.h>
#include "DHT.h"

// Network credentials
const char* ssid = "";
const char* password = "";

// Database info
const char* serverName = "https://UCSD-HDSI-IOT.com/post-esp-data.php";

#define LED_PIN     12
#define NUM_LEDS     31   // 144 - MAX
#define LOW_BRIGHTNESS    5s
#define MID_BRIGHTNESS    55
#define HIG_BRIGHTNESS    115
#define DHT_PIN     17
#define DHT_TYPE     DHT11

// Declare vars for DHT sensor 
DHT dht(DHT_PIN, DHT_TYPE);

// Declare vars for ambient light sensor
int temt6000Pin = 33;
int lightingCondition = 0;

// Declare vars for LED strip
CRGB leds[NUM_LEDS];
int onboardLEDPin = 2;
int pirPin = 4;
int pirVal = 0;
bool ledOn = false;
int currBrightness = 0;
int delayDuration = 30000;
unsigned long delayTime = 0;

void setup() {
  Serial.begin(115200);

  blinkOnboardLED(0);
  blinkOnboardLED(0);

  WiFi.begin(ssid, password);
  Serial.println("Connecting");
  while(WiFi.status() != WL_CONNECTED) { 
    delay(500);
    Serial.print(".");
  }
  Serial.println("");
  Serial.print("Connected to WiFi network with IP Address: ");
  Serial.println(WiFi.localIP());

  FastLED.addLeds<WS2812, LED_PIN, GRB>(leds, NUM_LEDS);
  pinMode(onboardLEDPin, OUTPUT);
  pinMode(pirPin, INPUT);
  dht.begin();


  Serial.print("read through function setup: ");
  Serial.print(analogRead(temt6000Pin));
  Serial.println("done reading");

}

void loop() {

  pirVal = digitalRead(pirPin);
  sendData();
  
  if (pirVal == HIGH) {

    delayTime = millis();

    while ((millis() - delayTime) < delayDuration) {

      int lightingCondition = analogRead(temt6000Pin);
      Serial.print("lighting condition: ");
      Serial.print(lightingCondition);
      Serial.println("");
      if (lightingCondition > 850) {
        Serial.println("OVER 850");
        graduallyOff(currBrightness);
        graduallyOn(currBrightness, 99);
      // } else if (lightingCondition <= 850 && lightCondition >= 5)
      } else {
        graduallyOff(currBrightness);
        graduallyOn(currBrightness, 5);
      }

      sendData();

      Serial.println(delayTime);
      Serial.println((millis() - delayTime));

      if (digitalRead(pirPin) == HIGH) {
        delayTime = millis();
      }

      delay(1500);

    }

  } 
  else {

    graduallyOff(currBrightness);

  }

  delay(1500);
  
}

void blinkOnboardLED(int delayLength) {

  digitalWrite(onboardLEDPin, HIGH);
  delay(delayLength);
  digitalWrite(onboardLEDPin, LOW);

}

void turnOn(int brightness) {

  FastLED.setBrightness(brightness);

  for (int i = 0; i <= NUM_LEDS; i++) {

    leds[i] = CRGB(255, 255, 255);

  }

  FastLED.show();
  currBrightness = brightness;
  ledOn = true;

}

void turnOff() {

  FastLED.clear();
  FastLED.show();
  currBrightness = 0;
  ledOn = false;

}

void graduallyOff(int currBrightness) {

  for (int i = currBrightness; i >= 0 ; i--) {
    FastLED.setBrightness(i);
    for (int j = 0; j <= NUM_LEDS; j++) {
      leds[j] = CRGB(255, 255, 255);
    }
    
    FastLED.show();
    delay(8);
  }
  
  ledOn = false;
  currBrightness = 0;
}

void graduallyOn(int currBrightness, int brightness) {

  if (ledOn == false) {
    for (int i = currBrightness+1; i <= brightness; i++) {
      FastLED.setBrightness(i);
      for (int j = 0; j <= NUM_LEDS; j++) {
        leds[j] = CRGB(255, 255, 255);
      }
      FastLED.show();
      delay(8);
    }
    ledOn = true;
  }

  currBrightness = brightness;
}

void sendData() {

  String apiKeyValue = "";
  String sensorName = "Team 3";
  String sensorLocation = "UC San Diego";

  //Check WiFi connection status
  if(WiFi.status()== WL_CONNECTED){
    WiFiClientSecure *client = new WiFiClientSecure;
    client->setInsecure(); //don't use SSL certificate
    HTTPClient https;
    
    // Your Domain name with URL path
    https.begin(*client, serverName);
    
    // Specify content-type header
    https.addHeader("Content-Type", "application/x-www-form-urlencoded");
    
    // Prepare HTTP POST request data
    String httpRequestData = "api_key=" + apiKeyValue + "&sensor=" + sensorName
                          + "&location=" + sensorLocation + "&value1=" + String(digitalRead(pirPin))
                          + "&value2=" + String(dht.readHumidity())+"%" + "&value3=" + String(dht.readTemperature(true))+"°F" + "";
    Serial.print("httpRequestData: ");
    Serial.println(httpRequestData);

    // Send HTTP POST request
    int httpResponseCode = https.POST(httpRequestData);
    
    if (httpResponseCode>0) {
      Serial.print("HTTP Response code: ");
      Serial.println(httpResponseCode);
      blinkOnboardLED(2000);
    }
    else {
      Serial.print("Error code: ");
      Serial.println(httpResponseCode);
      ESP.restart();
    }

    https.end();
  }
  else {
    Serial.println("WiFi Disconnected");
  }

}
