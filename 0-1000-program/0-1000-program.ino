void setup() {
  // put your setup code here, to run once:

  // Open the serial port
  Serial.begin(115200);

}

void loop() {
  // put your main code here, to run repeatedly:

  Serial.println("Counting start");

  for (int i = 0; i < 1000; ++i) {

    // Check for incoming serial data
    if (Serial.available()) {
      char inChar = Serial.read();
      bool stop = false;

      if (inChar == 's') {
        Serial.println("Counting stopped");
        stop = true;  
      }

      // Check if key s is received (stop)
      while (stop == true) {
        inChar = Serial.read();     // Read incoming key again

        // Break if key r is received (resume)
        if (inChar == 'r') {
          Serial.println("Counting resume");
          break;
        }
      }
    }

    Serial.println(i+1);
    delay(200);
  }

  // Wait 5 seconds before counting again
  delay(5000);

}
