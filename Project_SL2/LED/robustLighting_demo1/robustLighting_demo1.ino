#include <FastLED.h>

#define LED_PIN     12
#define NUM_LEDS    144
#define LOW_BRIGHTNESS    5
#define MID_BRIGHTNESS    55
#define HIG_BRIGHTNESS    115

CRGB leds[NUM_LEDS];
int ledPin = 2;
int pirPin = 4;
int pirVal = 0;
bool ledOn = false;
int currBrightness = 0;
int delayDuration = 30000;
unsigned long delayTime = 0;
// bool delayRunning = false;

void setup() {

  Serial.begin(115200);
  FastLED.addLeds<WS2812, LED_PIN, GRB>(leds, NUM_LEDS);
  pinMode(ledPin, OUTPUT);
  pinMode(pirPin, INPUT);

}

void loop() {

  pirVal = digitalRead(pirPin);
  
  if (pirVal == HIGH) {

    blinkOnboardLED();

    // delayRunning = true;
    delayTime = millis();

    while ((millis() - delayTime) < delayDuration) {

      graduallyOn(currBrightness, MID_BRIGHTNESS);

      Serial.println(delayTime);
      Serial.println((millis() - delayTime));
      Serial.print(" ");
      Serial.print(((millis() - delayTime) < delayDuration));

      if (digitalRead(pirPin) == HIGH) {
        delayTime = millis();
      }

    }

  } 
  else {

    graduallyOff(currBrightness);

  }
  
}

void blinkOnboardLED() {

  digitalWrite(ledPin, HIGH);
  delay(2000);
  digitalWrite(ledPin, LOW);

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
