#include <FastLED.h>

#define LED_PIN     12
#define NUM_LEDS    20

CRGB leds[NUM_LEDS];
int ledPin = 2;

void setup() {

  FastLED.addLeds<WS2812, LED_PIN, GRB>(leds, NUM_LEDS);
  pinMode(ledPin, OUTPUT);

}

void loop() {

  digitalWrite(ledPin, HIGH);
  delay(2000);
  digitalWrite(ledPin, LOW);
  
  leds[0] = CRGB(255, 0, 0);
  FastLED.show();
  delay(500);  
  leds[1] = CRGB(0, 255, 0);
  FastLED.show();
  delay(500);
  leds[2] = CRGB(0, 0, 255);
  FastLED.show();
  delay(500);
  // leds[5] = CRGB(150, 0, 255);
  // FastLED.show();
  // delay(500);
  // leds[9] = CRGB(255, 200, 20);
  // FastLED.show();
  // delay(500);
  // leds[14] = CRGB(85, 60, 180);
  // FastLED.show();
  // delay(500);
  // leds[19] = CRGB(50, 255, 20);
  // FastLED.show();
  // delay(500);
  // leds[24] = CRGB(255, 0, 255);
  // FastLED.show();
  // delay(500);
  // leds[29] = CRGB(51, 204, 204);
  // FastLED.show();
  // delay(500);
  // leds[34] = CRGB(150, 0, 255);
  // FastLED.show();
  // delay(500);
  // leds[39] = CRGB(255, 200, 20);
  // FastLED.show();
  // delay(500);
  // leds[44] = CRGB(85, 60, 180);
  // FastLED.show();
  // delay(500);
  // leds[49] = CRGB(50, 255, 20);
  // FastLED.show();
  // delay(500);
  // leds[54] = CRGB(255, 0, 255);
  // FastLED.show();
  // delay(500);
  // leds[59] = CRGB(51, 204, 204);
  // FastLED.show();
  // delay(500);
  // leds[64] = CRGB(150, 0, 255);
  // FastLED.show();
  // delay(500);
  // leds[69] = CRGB(255, 200, 20);
  // FastLED.show();
  // delay(500);
  // leds[74] = CRGB(85, 60, 180);
  // FastLED.show();
  // delay(500);
  // leds[79] = CRGB(50, 255, 20);
  // FastLED.show();
  // delay(500);
  // leds[84] = CRGB(255, 0, 255);
  // FastLED.show();
  // delay(500);
  // leds[89] = CRGB(51, 204, 204);
  // FastLED.show();
  // delay(500);
  // leds[94] = CRGB(50, 255, 20);
  // FastLED.show();
  // delay(500);
  // leds[99] = CRGB(255, 0, 255);
  // FastLED.show();
  // delay(500);
  // leds[104] = CRGB(51, 204, 204);
  // FastLED.show();
  // delay(500);
  // leds[109] = CRGB(51, 204, 204);
  // FastLED.show();
  // delay(500);
  // leds[114] = CRGB(50, 255, 20);
  // FastLED.show();
  // delay(500);
  // leds[119] = CRGB(255, 0, 255);
  // FastLED.show();
  // delay(500);
  // leds[124] = CRGB(51, 204, 204);
  // FastLED.show();
  // delay(500);
  // leds[129] = CRGB(51, 204, 204);
  // FastLED.show();
  // delay(500);
  // leds[134] = CRGB(50, 255, 20);
  // FastLED.show();
  // delay(500);
  // leds[139] = CRGB(255, 0, 255);
  // FastLED.show();
  // delay(500);
  // leds[144] = CRGB(51, 204, 204);
  // FastLED.show();
  // delay(500);
}