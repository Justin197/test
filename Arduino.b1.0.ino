int flash = 6;

int analogPin = 0;

int ldrWert = 0;

int schalter = 7;

int buttonState = LOW;

int x = 0;

int led = 13;



void setup() {

  Serial.begin(9600);

  pinMode(flash, OUTPUT);

  pinMode(led, OUTPUT);

  pinMode(schalter, INPUT);


}

void loop() {

  digitalWrite(flash, HIGH);

  ldrWert = analogRead(analogPin);

  if (ldrWert < 300) {

    Serial.println("Post ist da!");

    delay(2000);

  }

  if (ldrWert > 300) {

    Serial.println("Leerer Karsten"); //leer

    delay(2000);

  }

  if (Serial.available() > 0) {

    x = Serial.read();

    if (x == '1') {

      digitalWrite(led, HIGH);
      //delay(5000);

      buttonState = digitalRead(schalter);

      while (buttonState == LOW) {
        buttonState = digitalRead(schalter);
        delay(1000);
      }

      digitalWrite(led, LOW);

      Serial.println("Briefkarsten wird geschlossen");
      delay(1000);
 
    }

    else if (x == '0') {

      digitalWrite(led, LOW);

    }
    else {

      Serial.println("invalid!");

    }

  }

}
