#!/bin/bash

#Identify what account the spooler is running as (hint: use wmi)
wmic service where "name='Spooler'" get StartName >> "C:\Users\50103233\OneDrive - Belfast Metropolitan College\CW Scripts\spooler_account.txt"
