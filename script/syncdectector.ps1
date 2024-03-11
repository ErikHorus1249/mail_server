# Define desired NTP server
$desiredNTPServer = "10.0.14.11"  

# Get configured NTP server
# $NTPServer = (Get-ItemProperty -Path HKLM:\SYSTEM\CurrentControlSet\Control\TimeProviders\NtpClient).NtpServer
$NTPServer = "10.0.14.12" 
# Compare and send email if mismatch
if ($NTPServer -ne $desiredNTPServer) {
    $body = @{
			 "hostname"=$env:COMPUTERNAME
			 "ntp"=$NTPServer
			} | ConvertTo-Json

	$header = @{
	 "Accept"="application/json"
	 "Content-Type"="application/json"
	} 

	Invoke-RestMethod -Uri "http://10.15.7.177:8015/checker/" -Method 'Post' -Body $body -Headers $header | ConvertTo-HTML
}