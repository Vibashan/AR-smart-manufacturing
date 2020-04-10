#include "ESP_MICRO.h"

#define LED 4

int inputVal  = 0; 

void setup(){
  Serial.begin(9600);
  start("One_plus7","lollollol"); // Wifi details connec to

  pinMode(D1,OUTPUT);
  pinMode(D2,OUTPUT);
  pinMode(D4,OUTPUT);
}

void loop(){
  waitUntilNewReq();  //Waits until a new request from python come

  if (getPath()=="/2"){
    digitalWrite(D1, LOW);
    digitalWrite(D2, HIGH);
    digitalWrite(D4, LOW);
  }

  if (getPath()=="/3"){
    digitalWrite(D1, LOW);
    digitalWrite(D2, LOW);
    digitalWrite(D4, HIGH);
  }
}
