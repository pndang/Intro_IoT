// Source: https://wiki.keyestudio.com/Ks0098_keyestudio_TEMT6000_Ambient_Light_Sensor

int temt6000Pin = 13;

void setup() {
  // put your setup code here, to run once:

  Serial.begin(115200);

}

void loop() {
  // put your main code here, to run repeatedly:

  int value = analogRead(temt6000Pin);
  Serial.print("Ambient light: ");
  Serial.println(value);
  delay(100);
}
