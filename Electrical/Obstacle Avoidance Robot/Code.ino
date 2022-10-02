const int trigPin = D5;
const int echoPin2 = D7;
const int echoPin = D6;
const int echoPin3= D8;

//Both enable pins are connected to 5v to enable them
//For motor A

int in1 = D3;
int in2 = D4;

//For motor B

int in3 = D1;
int in4 = D2;

int centre_threshold=20;
int left_threshold=30;
int right_threshold=30;

String store_turn="none";
int store_cm2=centre_threshold;

int turn_time=1263;

//define sound velocity in cm/uS
#define SOUND_VELOCITY 0.034
#define CM_TO_INCH 0.393701

long duration;
float distanceCm1;
float distanceCm2;
float distanceCm3;
float distanceInch;

void setup() {
  Serial.begin(115200); // Starts the serial communication
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin2, INPUT);
//  pinMode(trigPin, OUTPUT); // Sets the trigPin as an Output
  pinMode(echoPin, INPUT); // Sets the echoPin as an Input
  pinMode(echoPin3, INPUT);

 
  pinMode(in1, OUTPUT);
  pinMode(in2, OUTPUT);
  pinMode(in3, OUTPUT);
  pinMode(in4, OUTPUT);
  
}

void loop() {
  // Sets the trigPin on HIGH state for 10 micro seconds
  // Clears the trigPin
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(15);
  digitalWrite(trigPin, LOW);
  unsigned long StartTime = millis();
  duration = pulseIn(echoPin, HIGH);
  // Calculate the distance
  distanceCm1 = duration * SOUND_VELOCITY/2;
  
  
  

  delayMicroseconds(10);

  duration = pulseIn(echoPin2, HIGH);

  int i=0;
  
  
  // Calculate the distance
  distanceCm2 = duration * SOUND_VELOCITY/2;
  
  
  
  duration = pulseIn(echoPin3, HIGH);
  // Calculate the distance
  distanceCm3 = duration * SOUND_VELOCITY/2;
  
  if(distanceCm2>30)
   {  
     if(store_turn=="left")
     {
       if(distanceCm3<=50 || distanceCm1<=50)
       {
          go_straight_after_turn();
       }
       else{
        delay(400);
        turn_right();
        store_turn = "none";
       }
     }
     else if(store_turn=="right")
     {
        if(distanceCm3<=50 || distanceCm1<=50)
       {
          go_straight_after_turn();
       }
       else{
        delay(400);
        turn_left();
        store_turn = "none";
       }
     }
     else
     {
       go_straight();
     }
    
   
   }
   else
   {
      store_cm2=distanceCm2;
  
      if(distanceCm1>distanceCm3) // && conditions
      {
        turn_left();
        store_turn="left";
      }
        else if(distanceCm3>=distanceCm1) // && conditions
        {
          turn_right();
          store_turn="right";  
        }
        
   }

}

void go_straight()
{
    //Right Motor

  digitalWrite(in1, HIGH);
  digitalWrite(in2, LOW);

  //Left Motor

  digitalWrite(in3, HIGH);
  digitalWrite(in4, LOW);  
}


void go_straight_after_turn()
{
    //Right Motor

  digitalWrite(in1, HIGH);
  digitalWrite(in2, LOW);

  //Left Motor

  digitalWrite(in3, HIGH);
  digitalWrite(in4, LOW);  
}


void turn_right()
{
  
   // Left Motor does not Works
  digitalWrite(in3, LOW);
  digitalWrite(in4, HIGH);  

 //Right Motor works

  digitalWrite(in1, HIGH);
  digitalWrite(in2, LOW);

  delay(1255);
  
}

void turn_left()
{
  // Left Motor Works
  digitalWrite(in3, HIGH);
  digitalWrite(in4, LOW);  
 //Right Motor Does not work

  digitalWrite(in1, LOW);
  digitalWrite(in2, HIGH);
   delay(1255);
  
  
  }

void go_back()
{
  //Right Motor back

  digitalWrite(in2, HIGH);
  digitalWrite(in1, LOW);

  //Left Motor back

  digitalWrite(in4, HIGH);
  digitalWrite(in3, LOW);  
  
}
