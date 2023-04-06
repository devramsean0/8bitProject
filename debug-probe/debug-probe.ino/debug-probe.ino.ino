const char ADDR[] = {22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52};
#define CLOCK 2
void setup() {
  // Address Lines
  for (int n=0; n < 16; n+=1) {
    pinMode(ADDR[n], INPUT);
  }
  // Clock
  pinMode(CLOCK, INPUT);
  attachInterrupt(digitalPinToInterrupt(CLOCK), onClock, RISING);
  
  Serial.begin(57600);
}

void onClock() {
  // put your main code here, to run repeatedly:
  for (int n=0; n < 16; n+=1) {
    int bit = digitalRead(ADDR[n]) ? 1 : 0;
    Serial.print(bit);
  }
  Serial.println();
}

void loop() {
}
