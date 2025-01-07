# Get the current date and time in long format
$currentDateTime = Get-Date -Format "F"

# Append to the file
$currentDateTime | Out-File -FilePath "C:\Scripts\print_commands.txt" -Append
