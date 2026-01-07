// consts

  //ID of Micro Controler used to diffrentite when mutiple are used 
  const byte ID = 0x02;
  const byte START = 0x0f;
  const byte END = 0xf0;
  
  // insert data pins of where positve lead of button is can support max of 255 buttons
  const int BUTTONS[] = {53,51};
  const int BUTTONSCOUNT = sizeof(BUTTONS) / sizeof(BUTTONS[0]);

void setup() {
  Serial.begin(9600);
  for(int pin : BUTTONS){
    digitalWrite(pin,HIGH);
  }  
}

void loop() {
  for (int index = 0 ; index < BUTTONSCOUNT ; index++)
    
    if(!digitalRead(BUTTONS[index])) {
      Serial.write(START);
      Serial.write(ID);
      Serial.write(byte2int(index+1));
      Serial.write(END);
      delay(250);
    }
  
}

byte byte2int(int i){
  byte b;
  // remove the high byte
  b = (byte) (i & 0x00FF);

  // drop the high byte just like that, but 'i' might be negative.
  b = (byte) i;

  // clip
  if( i < 0)
    i = 0;
  else if( i > 255)
    i = 255;
  b = (byte) i;

  // constrain
  i = constrain( i, 0, 255);
  b = (byte) i;

  return b;
}