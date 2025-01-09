#!/bin/bash 

# Find all commands related to 'print'
printCommands=$(compgen -c | grep print)

# Output the list to a file
echo "$printCommands" > "C:\Users\50103233\OneDrive - Belfast Metropolitan College\CW Scripts\jamies_local_file.txt"