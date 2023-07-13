
int ledPin = 4;

void setup() {
  // put your setup code here, to run once:

  // Open the serial port
  Serial.begin(115200);

  pinMode (ledPin, OUTPUT);

}

void loop() {
  // put your main code here, to run repeatedly:

  for (int i = 0; i < 100000; i++) {

    digitalWrite(ledPin, !digitalRead(ledPin));

  }
}
