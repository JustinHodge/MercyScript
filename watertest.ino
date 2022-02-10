#include "new_digiKeyboard.h"
void setup() {
	DigiKeyboard.sendKeyStroke (_R_, _WINDOWS_);
	DigiKeyboard.delay (500);
	DigiKeyboard.delay(1000);
	DigiKeyboard.print ("cmd");
	DigiKeyboard.delay (500);
	DigiKeyboard.delay(1000);
	DigiKeyboard.sendKeyStroke (_ENTER_);
	DigiKeyboard.delay (500);
	DigiKeyboard.print ("ipconfig");
	DigiKeyboard.delay (500);
	DigiKeyboard.sendKeyStroke (_ENTER_);
	DigiKeyboard.delay (500);
	DigiKeyboard.delay(2000);
	DigiKeyboard.print ("ping 8.8.8.8");
	DigiKeyboard.delay (500);
}
void loop() {
}
