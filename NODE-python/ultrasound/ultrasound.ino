#include "ESP_MICRO.h"

#define LED 4

int inputVal  = 0; 
float  duration;
int distance;

const int trigP = D4; 
const int echoP = D3;

void setup(){
  Serial.begin(9600);
  //start("One_plus7","lollollol"); // Wifi details connec to

  pinMode(trigP, OUTPUT);  
  pinMode(echoP, INPUT);
}

void loop(){
  //waitUntilNewReq();  //Waits until a new request from python come

  digitalWrite(trigP, LOW);   
  delayMicroseconds(2);       
  digitalWrite(trigP, HIGH);  
  delayMicroseconds(10);      
  digitalWrite(trigP, LOW);   
  //duration = pulseIn(echoP, HIGH);
  distance=(duration*330)/20000;
  Serial.println(distance);
  Serial.println("lol");
  //returnThisInt(distance);
  delay(1000);
}
