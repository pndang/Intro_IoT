
int inPin = 4;

void setup() {
  // put your setup code here, to run once:

  Serial.begin(115200);

}

void loop() {
  // put your main code here, to run repeatedly:

  int sensorVal = analogRead(inPin);

  Serial.println(sensorVal);

  delay(50);

}
