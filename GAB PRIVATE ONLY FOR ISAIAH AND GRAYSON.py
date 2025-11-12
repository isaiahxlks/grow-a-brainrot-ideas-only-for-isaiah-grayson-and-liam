$processName = "notepad"
$logFile = "$env:USERPROFILE\Desktop\ProcessMonitor.log"
$timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"

$process = Get-Process -Name $processName -ErrorAction SilentlyContinue

if ($process) {
    $message = "$timestamp - $processName is already running."
    Write-Host $message
    Add-Content -Path $logFile -Value $message
} else {
    $message = "$timestamp - $processName is not running. Attempting to start..."
    Write-Host $message
    Add-Content -Path $logFile -Value $message

    Start-Process $processName
    Start-Sleep -Seconds 2

    $checkAgain = Get-Process -Name $processName -ErrorAction SilentlyContinue
    if ($checkAgain) {
        $successMessage = "$timestamp - $processName started successfully."
        Write-Host $successMessage
        Add-Content -Path $logFile -Value $successMessage

        [Windows.UI.Notifications.ToastNotificationManager, Windows.UI.Notifications, ContentType = WindowsRuntime]
        $template = [Windows.UI.Notifications.ToastNotificationManager]::GetTemplateContent([Windows.UI.Notifications.ToastTemplateType]::ToastText01)
        $textNodes = $template.GetElementsByTagName("text")
        $textNodes.Item(0).AppendChild($template.CreateTextNode("$processName started successfully.")) | Out-Null
        $toast = [Windows.UI.Notifications.ToastNotification]::new($template)
        $notifier = [Windows.UI.Notifications.ToastNotificationManager]::CreateToastNotifier("ProcessMonitor")
        $notifier.Show($toast)
    } else {
        $failMessage = "$timestamp - Failed to start $processName."
        Write-Host $failMessage
        Add-Content -Path $logFile -Value $failMessage
    }
}
