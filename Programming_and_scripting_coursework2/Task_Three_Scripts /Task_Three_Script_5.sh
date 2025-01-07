# Get all available WMI classes
$wmiClasses = Get-WmiObject -List

# Append the WMI class list to the file
$wmiClasses | Out-File -FilePath "C:\Scripts\print_commands.txt" -Append
