
int irPin = 4;
int ledPin = 2;
int irVal = 0;

void setup() {
  // put your setup code here, to run once:

  Serial.begin(115200);

  pinMode(ledPin, OUTPUT);
  pinMode(irPin, INPUT);

}

void loop() {
  // put your main code here, to run repeatedly:

  irVal = digitalRead(irPin);  // Read sensor data
  Serial.println(irVal);

  if (irVal == HIGH) {
    Serial.println("Motion detected!");
    digitalWrite(ledPin, HIGH);  // Turn on LED if sensor detects any reflected ray
  } 
  else {
    Serial.println("Motion stopped!");
    digitalWrite(ledPin, LOW);  // Turn off LED if no reflection detected
  }

}
