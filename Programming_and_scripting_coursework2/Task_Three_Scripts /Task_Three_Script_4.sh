#!/bin/bash

#Append a list of all available WMI classes to local file
powershell -Command "Get-WmiObject -List | Out-File 'C:\Users\50103233\OneDrive - Belfast Metropolitan College\CW Scripts\jamies_local_file.txt' -Append"