# Argparse_-_Click
A test task aimed at understanding the basic principles of work with the 
Argparse and Click.

# Details
The purpose of this task is to extract rows matching the conditions given in
arguments from a CSV file. CSV file containing the list of airports around the
world. There are three possible arguments: IATA code, Country name and Airport
name. 

IATA code should contain only three capital letters in format "AAA","BBB", etc. 

Country name should contain two capital letters (international format) 
in format "UA", "UK", "US", etc. Program will find and return all matches. 

Airport name should contain name (or part of the name) of airport. Program will 
find and return all matches. For example if Airport name argument will be 
"liman", program will return "Ilimanaq Heliport", "Sidi Slimane Airport", 
"Kilimanjaro International Airport", etc.

We should use only one of the three available arguments. To create 
arguments I used Argparse and Click (in the separate modules).

Also, custom errors were created to show IATACodeError if incorrect IATA code 
format will be entered, MultipleOptionsError if more than one argument 
received, etc.

This is the CLI script, so we can call this program using terminal.
To call script just enter python3 Click_test_task.py or 
python3 Argparse_test_task.py following by argument. 
For example: python3 Click_test_task.py -n Odessa, 
or python3 Argparse_test_task.py -ic ODS.

List available arguments we can check using "--help" option.
