const int buzzer = 9;
int anPin0 = A0, anPin1 = A1, anPin2 = A2, anPin3 = A3, anPin4 = A4, anPin5 = A5;
int val0=0,val1=0, val2 =0,val3 =0, val4 =0, val5 = 0;

void setup() 
{
  Serial.begin(9600);
  pinMode(buzzer, OUTPUT);
  
}


void loop() {
  
  val0 = analogRead(anPin0);
  val1 = analogRead(anPin1);
  val2 = analogRead(anPin2);
  val3 = analogRead(anPin3);
  val4 = analogRead(anPin4);
  val5 = analogRead(anPin5);

  Serial.println(val0);
  Serial.println(val1);
  Serial.println(val2);
  Serial.println(val3);
  Serial.println(val4);
  Serial.println(val5);
  
if (val0>350){
  tone(buzzer, 200);}
else if (val1>350){
  tone(buzzer, 400);}
else if (val2>350){
  tone(buzzer, 600);}
else if (val3>320){
  tone(buzzer, 800);}
else if (val4>350){
  tone(buzzer, 1000);}
else if (val5>350){
  tone(buzzer, 2000);}
else{        
    noTone(buzzer);}    
}
