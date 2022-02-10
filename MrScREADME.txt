
MERCYSCRIPT is a python3 (it is not compatible with python2. advised to use 3.5+ for built in access to necessary libraries) based interpretter for a 
simplified language that will take a simple text file in an ultra simplified format and output a text file in arduino native c++. The file output of this 
script will be a complete *.ino file available for immediate upload to a digispark device.

In this folder there is a file named "new_digiKeyboard.h" move this file to the libraries folder for your digispark installation 
(likely at "C:\Users\USERNAME\AppData\Local\Arduino15\packages\digistump\hardware\avr\1.6.7\libraries\DigisparkKeyboard" or similar depending on your digispark version). 
This header file includes some missing definitions in the base header and adds some simplified terminology for keystroke inputs.

When the script is started it will ask for locations of the text file. Simply use the entire filepath exactly as it is *including* filetype extension. 
Then it will ask for the location you wish to create the file. Again simply type an entire filepath but this time *without* a file extension, the script 
will automatically make this a *.ino file to be opened in an Arduino IDE directly.

The text files to be input into this script should be of a particular format. each line of the text file is interpreted as a new command. the commands are 
declared at the start of a line with an optional numerical representation if one wishes the command to be repeated that many times. If no numerical is found 
the script will default to executing the command a single time. 

There are 4 command types available. The script requires that each line is defined using one of these commands. All commands have an attached half second 
delay for compatibility with slower systems.  

[repeatnum]!_(key)_[+_(key)_] - this command is for a single keystroke output. Key names are not case sensitive but caps is advised. The optional "+_(key)_" 
can be repeated for additional modification keys such as SHIFT or WINDOWS. The order the keys are written is of no consequence. All keys are of the format "_(key)_" 

EXAMPLE CASE : 3!_DEL_+_CTRL_+_ALT_ will input control, alt, delete 3 times. 
EXAMPLE CASE2: !_A_ will strike the A key once.

[repeatnum]@(timeofdelay) - This command allows additional custom delays (for instance to wait for a network connection before proceeding). All delays 
must be numerical digits and are interpreted as milliseconds (1 second = 1000 milliseconds). 

EXAMPLE CASE : 2@30000 will delay any further keyboard inputs for 30 seconds twice.

[repeatnum]#(string) - This command types the string given any number of times declared. If new lines are required between strings one must follow a string input with a 
!_ENTER_ command

EXAMPLE CASE : 4#Hello World will type the phrase "Hello WorldHello WorldHello WorldHello World"

-------------------------V1.2 Added another command ------------------
$COMMENTTEXTHERE - this command will be completely ignored and used primarily for commenting and debugging payloads.
------------------------------------------------------------------