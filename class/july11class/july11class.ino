
int ledPin = 2;
int inPin = 4;
int val = 0;

void setup() {
  // put your setup code here, to run once:

  Serial.begin(115200);
  
  pinMode(ledPin, OUTPUT);
  pinMode(inPin, INPUT);

}

void loop() {
  // put your main code here, to run repeatedly:

  val = analogRead(inPin);
  Serial.println(val, DEC);

  if (val > 2000) {
    digitalWrite(ledPin, HIGH);
  } else {
    digitalWrite(ledPin, LOW);
  }

  delay(val);
  
}
