# Import Module
Import-Module Terminal-Icons

# the fuck
$env:PYTHONIOENCODING="utf-8"
function fuck {
    $history = (Get-History -Count 1).CommandLine;
    if (-not [string]::IsNullOrWhiteSpace($history)) {
        $fuck = $(thefuck $args $history);
        if (-not [string]::IsNullOrWhiteSpace($fuck)) {
            if ($fuck.StartsWith("echo")) { $fuck = $fuck.Substring(5); }
            else { Invoke-Expression "$fuck"; }
        }
    }
    [Console]::ResetColor()
}


# Alias
Set-Alias vim nvim
Set-Alias ll ls
Set-Alias g git

# Settings
Set-PSReadLineOption -PredictionSource History
Set-PSReadLineOption -PredictionViewStyle ListView












