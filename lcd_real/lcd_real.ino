#include <LiquidCrystal.h>

// initialize the library with the numbers of the interface pins
LiquidCrystal lcd(12, 11, 5, 4, 3, 2);

void setup(){
    // set up the LCD's number of columns and rows: 
  lcd.begin(20, 4);
  // initialize the serial communications:
  Serial.begin(9600);
  Serial.println("initialized");
  lcd.println("initilized....");
  delay(10);
  //9 & 8 dio
  pinMode(9, INPUT);
  pinMode(8, INPUT);
  pinMode(7, INPUT);
}
int line_1 = 1;
int line_2 = 2;
int line_3 = 3;
int line_4 = 4;
int arr[] = {line_1,line_2,line_3,line_4};
int i = 0;
int x = 0;  

int oldD1 = 0;
int oldD2 = 0;
int oldD3 = 0;
boolean forward = false;
boolean backward = false;
int lastPos = 0;
void loop(){
  int d1 = digitalRead(9);
  int d2 = digitalRead(8);
  int d3 = digitalRead(7);
  if(d2 != oldD2){
    oldD2 = d2;
    if(d2 == 1){
      forward = false;
      backward = true;
    }
    //    Serial.print("8:");
    // Serial.println(d2);
  }
  if(d3 != oldD3){
    oldD3 = d3;
    if(d3 == 1){
      forward = true;
      backward = false;

    }
    //    Serial.print("7:");
    //    Serial.println(d3);
  } 
  if(forward==true && backward==false){
    Serial.println(">");
    forward = false;
    backward = false;
    lastPos = 1;
  }
  if(backward==true && forward==false){
    Serial.println("<");
	forward = false;
	backward = false;
	lastPos = -1;
  }
 

 

  while (Serial.available() > 0){
    char k = Serial.read();
    if(k == '\0'){
      lcd.clear();
    }
    lcd.write(k);
      }
}

void loop_1(){
   while (Serial.available() > 0) {
      // display each character to the LCD
//      String inp =  Serial.read();
      char k = Serial.read();
      if( k == '\n' || k == '\r'){
        Serial.println("newline");
        
        x = 0;
        if(i>=4){
          lcd.clear();
          i = 0;
          
        }
        else{
          lcd.setCursor(x,arr[i]);
          i++;
        }
      }
      else{
        lcd.write(k);

        Serial.print(" - (");
      
        Serial.print(x);
        Serial.print(",");
        Serial.print(i);
        Serial.println(")");
      
        x++;
    }
   }
}



