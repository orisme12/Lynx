Write-Host "Hola Mundo"

$folder_app = "app" 

if (Test-Path $folder_app -PathType Container) {
    <# Action to perform if the condition is true #>
    Write-Host "Run server... 🚀"
    uvicorn app.main:app --port 8888 --reload
} else {
    Write-Host "Denied folder no exits...❌"
}

