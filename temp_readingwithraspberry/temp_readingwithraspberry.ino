float t=0;

void setup() {
  // put your setup code here, to run once:
pinMode(A0,INPUT);
Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
t = analogRead(A0);
t = t/1024.0 * 5.0;
t= t*100;
Serial.println(t);
delay(100);
}
