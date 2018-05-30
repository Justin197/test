int flash = 6;
int analogPin = 0;
int ldrWert = 0;

int x = 0;
int led = 13;

void setup() {
  Serial.begin(9600);
  pinMode(flash, OUTPUT);
  pinMode(led, OUTPUT);

}

void loop() {


  //char ard_sends = '1';
  //Serial.print (ldrWert);
  digitalWrite(flash, HIGH);
  ldrWert = analogRead(analogPin);
  if (ldrWert < 900) {
    Serial.println(9);
    delay(2000);
  }
  if (ldrWert > 900) {
    Serial.println(10); //leer
    delay(2000);
  }
  if (Serial.available() > 0) {



    x = Serial.read();

    if (x == '1') {
      digitalWrite(led, HIGH);
    }
    else if (x == '0') {
      digitalWrite(led, LOW);
    }
    else {
      Serial.println("invalid!");

    }
  }
}
