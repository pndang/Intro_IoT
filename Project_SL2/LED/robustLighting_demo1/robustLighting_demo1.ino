#include <FastLED.h>

#define LED_PIN     12
#define NUM_LEDS    20
#define LOW_BRIGHTNESS    5

CRGB leds[NUM_LEDS];
int ledPin = 2;
int pirPin = 4;
int pirVal = 0;

void setup() {

  FastLED.addLeds<WS2812, LED_PIN, GRB>(leds, NUM_LEDS);
  pinMode(ledPin, OUTPUT);
  pinMode(pirPin, INPUT);

}

void loop() {

  pirVal = digitalRead(pirPin);
  
  if (pirVal == HIGH) {

    blinkOnboardLED();
    delay(2000);
    turnOnFirstThree();

  } 
  else {

    turnOff();

  }
  
}

void blinkOnboardLED() {

  digitalWrite(ledPin, HIGH);
  delay(2000);
  digitalWrite(ledPin, LOW);

}

void turnOnFirstThree() {

  FastLED.setBrightness(LOW_BRIGHTNESS);
  leds[0] = CRGB(255, 0, 0);
  FastLED.show();
  delay(500);  
  leds[1] = CRGB(0, 255, 0);
  FastLED.show();
  delay(500);
  leds[2] = CRGB(0, 0, 255);
  FastLED.show();
  delay(500);

}

void turnOff() {

  FastLED.clear();
  FastLED.show();

}