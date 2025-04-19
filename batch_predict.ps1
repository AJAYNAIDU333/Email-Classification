# batch_predict.ps1

# List of sample emails to classify
$emails = @(
  "Hi, my name is Alex and my card expires in 12/24.",
  "Dear Support, contact me at 9876543210 for help.",
  "Hello, I am Jane Doe and my email is jane.doe@example.com"
)

# Your API endpoint
$url = "http://localhost:7860/predict"

# Loop over each email and send a prediction request
foreach ($email in $emails) {
    $body = @{ email_body = $email } | ConvertTo-Json
    $response = Invoke-RestMethod -Uri $url -Method Post `
        -ContentType 'application/json' -Body $body
    Write-Host "Input: $email"
    Write-Host "Response:"
    $response | ConvertTo-Json -Depth 5
    Write-Host "`n---`n"
}
