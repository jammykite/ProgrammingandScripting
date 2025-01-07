# Get the last 20 error events from the system log
$errorEvents = Get-WinEvent -LogName System -Level Error | Select-Object -First 20

# Append the errors to the file
$errorEvents | Out-File -FilePath "C:\Scripts\print_commands.txt" -Append
