/*
  Example from WiFi > WiFiScan
  Complete details at https://RandomNerdTutorials.com/esp32-useful-wi-fi-functions-arduino/
*/

#include "WiFi.h"

// Replace with your network credentials
const char* ssid = "Phu Dang";
const char* password = "dangphu9220";

void setup() {
  Serial.begin(115200);

  // Set WiFi to station mode and disconnect from an AP if it was previously connected
  WiFi.mode(WIFI_STA);
  WiFi.disconnect();
  delay(100);

  Serial.println("Setup done");
}

void loop() {
  Serial.println("scan start");

  // WiFi.scanNetworks will return the number of networks found
  int n = WiFi.scanNetworks();
  Serial.println("scan done");
  if (n == 0) {
      Serial.println("no networks found");
  } else {
    Serial.print(n);
    Serial.println(" networks found");
    for (int i = 0; i < n; ++i) {
      // Print SSID and RSSI for each network found
      Serial.print(i + 1);
      Serial.print(": ");
      Serial.print(WiFi.SSID(i));
      Serial.print(" (");
      Serial.print(WiFi.RSSI(i));
      Serial.print(")");
      Serial.println((WiFi.encryptionType(i) == WIFI_AUTH_OPEN)?" ":"*");

      if (WiFi.SSID(i) == "Phu Dang") {
        Serial.println("Attempting to connect to Phu's Phone");
        WiFi.mode(WIFI_STA);
        WiFi.begin(ssid, password);
        Serial.print("Connecting to WiFi ..");
        while (WiFi.status() != WL_CONNECTED) {
          Serial.print('.');
          delay(1000);
        }
        Serial.println(WiFi.localIP());
      } 

      delay(10);
    }
  }
  Serial.println("");

  // Wait a bit before scanning again
  delay(5000);
}


// #include <WiFi.h>

// #define CONNECTION_TIMEOUT 10

// const char* ssid = "brandt";
// const char* password = "botilde10";

// void setup(){
//     Serial.begin(115200);
//     delay(1000);

//     WiFi.mode(WIFI_STA); //Optional
//     WiFi.begin(ssid, password);
//     Serial.println("\nConnecting");
//     int timeout_counter = 0;

//     while(WiFi.status() != WL_CONNECTED){
//         Serial.print(".");
//         delay(200);
//         timeout_counter++;
//         if(timeout_counter >= CONNECTION_TIMEOUT*5){
//         ESP.restart();
//         }
//     }

//     Serial.println("\nConnected to the WiFi network");
//     Serial.print("Local ESP32 IP: ");
//     Serial.println(WiFi.localIP());
// }

// void loop(){}




// /* Wi-Fi STA Connect and Disconnect Example

//    This example code is in the Public Domain (or CC0 licensed, at your option.)

//    Unless required by applicable law or agreed to in writing, this
//    software is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR
//    CONDITIONS OF ANY KIND, either express or implied.
   
// */
// #include <WiFi.h>

// const char* ssid     = "brandt";
// const char* password = "botilde10";

// int btnGPIO = 0;
// int btnState = false;

// void setup()
// {
//     Serial.begin(115200);
//     delay(10);

//     // Set GPIO0 Boot button as input
//     pinMode(btnGPIO, INPUT);

//     // We start by connecting to a WiFi network
//     // To debug, please enable Core Debug Level to Verbose

//     Serial.println();
//     Serial.print("[WiFi] Connecting to ");
//     Serial.println(ssid);

//     WiFi.begin(ssid, password);
// // Auto reconnect is set true as default
// // To set auto connect off, use the following function
// //    WiFi.setAutoReconnect(false);

//     // Will try for about 10 seconds (20x 500ms)
//     int tryDelay = 500;
//     int numberOfTries = 31;

//     // Wait for the WiFi event
//     while (true) {
        
//         switch(WiFi.status()) {
//           case WL_NO_SSID_AVAIL:
//             Serial.println("[WiFi] SSID not found");
//             break;
//           case WL_CONNECT_FAILED:
//             Serial.print("[WiFi] Failed - WiFi not connected! Reason: ");
//             return;
//             break;
//           case WL_CONNECTION_LOST:
//             Serial.println("[WiFi] Connection was lost");
//             break;
//           case WL_SCAN_COMPLETED:
//             Serial.println("[WiFi] Scan is completed");
//             break;
//           case WL_DISCONNECTED:
//             Serial.println("[WiFi] WiFi is disconnected");
//             break;
//           case WL_CONNECTED:
//             Serial.println("[WiFi] WiFi is connected!");
//             Serial.print("[WiFi] IP address: ");
//             Serial.println(WiFi.localIP());
//             return;
//             break;
//           default:
//             Serial.print("[WiFi] WiFi Status: ");
//             Serial.println(WiFi.status());
//             break;
//         }
//         delay(tryDelay);
        
//         if(numberOfTries <= 0){
//           Serial.print("[WiFi] Failed to connect to WiFi!");
//           // Use disconnect function to force stop trying to connect
//           WiFi.disconnect();
//           return;
//         } else {
//           numberOfTries--;
//         }
//     }
// }

// void loop()
// {
//     // Read the button state
//     btnState = digitalRead(btnGPIO);
    
//     if (btnState == LOW) {
//       // Disconnect from WiFi
//       Serial.println("[WiFi] Disconnecting from WiFi!");
//       // This function will disconnect and turn off the WiFi (NVS WiFi data is kept)
//       if(WiFi.disconnect(true, false)){
//         Serial.println("[WiFi] Disconnected from WiFi!");
//       }
//       delay(1000);
//     }
// }
