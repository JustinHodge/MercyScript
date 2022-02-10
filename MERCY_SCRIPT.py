#v1.1 adds the ability to use a multiple digit loop_counter
#v1.2 handles error_case in a better more reliable way

#includes and variable declarations
import pathlib
from os import remove as remove
import re
line_number = 0;
index_of_declaration = 0;
loop_counter = 1;


#file locations and setup
file_location = input("Where is the file. Please include the file extension if one exists.\n");
file_destination = input("Where should the file be created? DO NOT ADD A FILE EXTENSION.\n");
normalized_file_location = file_location.replace("\\", "/");
normalized_file_destination = file_destination.replace("\\", "/") + ".ino";
start_file = open(pathlib.Path(normalized_file_location), "r");
list_of_commands = start_file.readlines();
new_script = open(pathlib.Path(normalized_file_destination), "w");
new_script.write('#include "new_digiKeyboard.h"\n')
new_script.write('void setup() {\n')

def error_case(line_number):
	new_script.close()
	print('Error occured on line number ' + line_number + '\n')
	input("Press Enter to exit program.\n");
	remove(pathlib.Path(normalized_file_destination));
	exit();

#main loop

for raw_command_from_list in list_of_commands :
	index_of_declaration = 0
	line_number = line_number + 1;
	loop_counter = 1;

#this will check for repetition of command
	while raw_command_from_list[index_of_declaration].isnumeric():
			index_of_declaration = index_of_declaration + 1;
			loop_counter = int(raw_command_from_list[:index_of_declaration]);

	#this sets which branch is executed
	command_declaration = raw_command_from_list[index_of_declaration];

	#this block sets current_command srtripping off the ending newline and the command declare and repeater
	if raw_command_from_list[-1] == "\n":
		current_command = raw_command_from_list [ index_of_declaration + 1 : len(raw_command_from_list) - 1];

	else:
		current_command = raw_command_from_list [ index_of_declaration + 1: ];

	#this checks if the command declaration points to a valid branch
	#if command_declaration == "!" or command_declaration == "@" or command_declaration == "#":
	if command_declaration in ["!", "@", "#", "$"]:
		#this is for keystroke commands
			if command_declaration == "!":
				current_command_list = current_command.split("+");
				num_modifiers = len(current_command_list) - 1;
				index_of_list = -1;
				current_command_mods = [];

				for i in current_command_list:
					index_of_list = index_of_list + 1;
					if i.upper() == "_SHIFT_" or i.upper() == "_GUI_" or i.upper() == "_WINDOWS_" or i.upper() == "_CTRL_" or i.upper() == "_ALT_":
						current_command_mods.append(i);
					elif re.match('_*_', i):
						current_command_send = i;
					else:
						print('\nThere was an error in command format.\n')
						error_case(str(line_number));

				while loop_counter > 0:
					new_script.write('	DigiKeyboard.sendKeyStroke (' + current_command_send.upper() );
					if len(current_command_mods) > 0:
						new_script.write(", " + current_command_mods[0].upper());
						for i in current_command_mods[1:]:
							new_script.write(" | " + i.upper());
					new_script.write(');' + '\n' );
					new_script.write('	DigiKeyboard.delay (500);\n');
					loop_counter = loop_counter - 1;

			#This is for delays
			elif command_declaration == "@":
				while loop_counter > 0:
					if current_command.isnumeric():
						new_script.write('	DigiKeyboard.delay(' + current_command + ');\n');
						loop_counter = loop_counter - 1;
					else:
						print ("There was an error. Only numerical delays are allowed. Delays are in milliseconds. Error occured on line " + str(line_number) + '\n');
						error_case(str(line_number));
			#this is the branch for string inputs
			elif command_declaration == "#":
				while loop_counter > 0:
					loop_counter = loop_counter - 1;
					new_script.write('	DigiKeyboard.print ("' + current_command + '");\n');
					new_script.write('	DigiKeyboard.delay (500);\n');
			elif command_declaration == "$":
				pass
			else:
				print("Unknown error\n");
				error_case('*unknown line*');
	#this is default error if no appropriate declaration was made
	else:
		print('No command type was declared\n');
		error_case(str(line_number));


#close txt files and cleanup
new_script.write('}\n');
new_script.write('void loop() {\n');
new_script.write('}\n');
new_script.close();
start_file.close();
exit();
