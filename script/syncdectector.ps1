# Define desired NTP server
$desiredNTPServer = "10.0.14.1"  

# Get configured NTP server
$NTPServer = (Get-ItemProperty -Path HKLM:\SYSTEM\CurrentControlSet\Control\TimeProviders\NtpClient).NtpServer

# Gateway Connection Testing
$targetGateway = "10.88.99.2"
$conn_Result = Test-Connection $targetGateway -Count 4 -Quiet

if ($conn_Result -eq $True) {
	if ($NTPServer -ne $desiredNTPServer) {
		$body = @{
				"hostname"=$env:COMPUTERNAME
				"username"=$env:USERNAME
				"ntp"=$NTPServer
				} | ConvertTo-Json

		$header = @{
		"Accept"="application/json"
		"Content-Type"="application/json"
		} 
		Invoke-RestMethod -Uri "http://10.15.7.177:8015/checker/" -Method 'Post' -Body $body -Headers $header | ConvertTo-HTML
	}
}
