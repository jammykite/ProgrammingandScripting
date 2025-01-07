# Find all print-related cmdlets
$printCommands = Get-Command *print*

# Output the list to a file
$printCommands | Out-File -FilePath "C:\Scripts\print_commands.txt"
