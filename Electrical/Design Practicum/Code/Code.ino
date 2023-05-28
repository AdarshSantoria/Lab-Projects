
const int StepX = 2;
const int DirX = 5;
const int StepY = 3;
const int DirY = 6;
const int E1 = 12;
const int E2 = 11;
char command; 

void setup() {
  pinMode(StepX,OUTPUT);
  pinMode(DirX,OUTPUT);
  pinMode(StepY,OUTPUT);
  pinMode(DirY,OUTPUT);
  pinMode(E1,OUTPUT);
  pinMode(E2,OUTPUT);
  Serial.begin(9600);  //Set the baud rate to your Bluetooth module.
}
//For horizontal Axis
void block_go_right(){
   digitalWrite(DirY, HIGH);
   digitalWrite(E1, LOW);
   digitalWrite(E2, HIGH);
   
   for(int x = 0; x<100; x++){ // loop for 200 steps
    digitalWrite(StepY,HIGH);
    delayMicroseconds(200);
    digitalWrite(StepY,LOW); 
    delayMicroseconds(200);
   }
}
void block_go_left(){
   digitalWrite(DirY, LOW);
   digitalWrite(E1, LOW);
   digitalWrite(E2, HIGH);
   
   for(int x = 0; x<100; x++){ // loop for 200 steps
    digitalWrite(StepY,HIGH);
    delayMicroseconds(200);
    digitalWrite(StepY,LOW); 
    delayMicroseconds(200);
   }
}
//--------------------------------------------------------------------------------------------
void axis_go_right(){
   digitalWrite(DirY, HIGH);
   digitalWrite(E1, HIGH);
   digitalWrite(E2, LOW);
   
   for(int x = 0; x<100; x++){ // loop for 200 steps
    digitalWrite(StepY,HIGH);
    delayMicroseconds(200);
    digitalWrite(StepY,LOW); 
    delayMicroseconds(200);
   }
}
void axis_go_left(){
   digitalWrite(DirY, LOW);
   digitalWrite(E1, HIGH);
   digitalWrite(E2, LOW);
   for(int x = 0; x<100; x++){ // loop for 200 steps
    digitalWrite(StepY,HIGH);
    delayMicroseconds(200);
    digitalWrite(StepY,LOW); 
    delayMicroseconds(200);
   }
}

/////////////////////////////////////////////////////////////////////
//For Vertical Axis
void block_go_up(){
   digitalWrite(DirX, HIGH);
   digitalWrite(E1, HIGH);
   digitalWrite(E2, LOW);
   
   for(int x = 0; x<100; x++){ // loop for 200 steps
    digitalWrite(StepX,HIGH);
    delayMicroseconds(150);
    digitalWrite(StepX,LOW); 
    delayMicroseconds(150);
   }
}
void block_go_down(){
   digitalWrite(DirX, LOW);
   digitalWrite(E1, HIGH);
   digitalWrite(E2, LOW);
   
   for(int x = 0; x<100; x++){ // loop for 200 steps
    digitalWrite(StepX,HIGH);
    delayMicroseconds(150);
    digitalWrite(StepX,LOW); 
    delayMicroseconds(150);
   }
}
//--------------------------------------------------------------------------------------------
void axis_go_up(){
   digitalWrite(DirX, LOW);
   digitalWrite(E1, LOW);
   digitalWrite(E2, HIGH);
   
   for(int x = 0; x<100; x++){ // loop for 200 steps
    digitalWrite(StepX,HIGH);
    delayMicroseconds(150);
    digitalWrite(StepX,LOW); 
    delayMicroseconds(150);
   }
}
void axis_go_down(){
   digitalWrite(DirX, HIGH);
   digitalWrite(E1, LOW);
   digitalWrite(E2, HIGH);
   
   for(int x = 0; x<100; x++){ // loop for 200 steps
    digitalWrite(StepX,HIGH);
    delayMicroseconds(150);
    digitalWrite(StepX,LOW); 
    delayMicroseconds(150);
   }
}
void loop() { 

  if(Serial.available() > 0){ 
    command = Serial.read(); 
    
    digitalWrite(E1, HIGH);
    digitalWrite(E2, HIGH);
    
    switch(command){
    case 'F':  
      block_go_up();
      break;
    case 'B':
       block_go_down();
      break;
    case 'L':  
      block_go_left();
      break;
    case 'R':
      block_go_right();
      break;
    case 'G':  
      axis_go_up();
      break;
    case 'J':  
      axis_go_down();
      break;
    case 'H':  
      axis_go_right();
      break;
    case 'I':  
      axis_go_left();
      break;
    }
  } 

}
