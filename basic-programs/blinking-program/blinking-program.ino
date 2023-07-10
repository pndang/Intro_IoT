/*

Blinking program for ESP32 - blink LED every 300 ms
  - stop (stay off) when key '0' is pressed
  - turn on (stay on) when key '1' is pressed
  - resume blinking when key 'r' is pressed
  - stop blinking when key 's' is pressed.

*/


int ledOnBoard = 2;

void setup() {
  // put your setup code here, to run once:

  // Open serial port
  Serial.begin(115200);

  pinMode  (ledOnBoard, OUTPUT);

}

void loop() {
  // put your main code here, to run repeatedly:

  // Check for incoming serial data
  if (Serial.available()) {
    char inChar = Serial.read();
    bool stop = false;
    bool stayFixed = false;

    if (inChar == 's') {

      digitalWrite(ledOnBoard, LOW);
      stop = true;

    } else if (inChar == '1') {

      digitalWrite(ledOnBoard, HIGH);
      stayFixed = true;

    } else if (inChar == '0') {

      digitalWrite(ledOnBoard, LOW);
      stayFixed = true;

    }

    while (stop == true || stayFixed == true) {
  
      inChar = Serial.read();     // Read incoming key again

      // break if key r (resume) is received
      if (inChar == 'r') {

        break;

      } else if (inChar == '1') {

        digitalWrite(ledOnBoard, HIGH);

      } else if (inChar == '0') {

        digitalWrite(ledOnBoard, LOW);

      }
    }
  }

  digitalWrite(ledOnBoard, HIGH);
  delay(300);
  digitalWrite(ledOnBoard, LOW);
  delay(300);

}
