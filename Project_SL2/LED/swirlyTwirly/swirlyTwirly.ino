// Source: https://lifemeetlightning.com/all-the-led-lights/fastled-tutorial-code/

#include <FastLED.h>
#define NUM_LEDS 144
#define DATA_PIN 12 //How boring and obvious!
#define COLOR_ORDER GRB //Green (G), Red (R), Blue (B)
#define CHIPSET WS2812B
#define BRIGHTNESS 60
#define VOLTS 5
#define MAX_AMPS 500 //value in milliamps

//ENOUGH NONSENSE!

CRGB leds[NUM_LEDS];

void setup() {

FastLED.addLeds<CHIPSET,DATA_PIN,COLOR_ORDER>(leds,NUM_LEDS);
FastLED.setMaxPowerInVoltsAndMilliamps(VOLTS,MAX_AMPS);
FastLED.setBrightness(BRIGHTNESS);
FastLED.clear();
FastLED.show(); 

//JONNY FIVE IS ALIVE!!!!!!!!!!!!!!!!!!!!

}

void loop() { //Swirly, twirly effect

  for (int i=0; i<NUM_LEDS; i++) {
    leds[i] = CRGB(0,255 - 4*i,4*i);
    FastLED.show();
    delay(10); //even shorter delay this time
  }

//decrements down from end of lights

  for (int i=NUM_LEDS - 1; i>=0; i--) {
    leds[i] = CRGB(4*i,0,255-4*i);
    FastLED.show();
    delay(10); //even shorter delay this time
  }

}