
$requirements = ".\requirements.txt"
$requirements_dev = ".\requirements-dev.txt"

python -m venv env

$env_active = "env"

Write-Host "Activate Env... 🐳"

Get-ChildItem -Recurse ".\env\Scripts\Activate.ps1" | Unblock-File

if (Test-Path $env_active -PathType Container) {
    Write-Host "Install dependecies... 🚀"
    python -m pip install --upgrade pip

    pip install -r $requirements
    pip install -r $requirements_dev
    <# Action to perform if the condition is true #>
} else {
    Write-Host "Denied... folder env no exits ❌"
}