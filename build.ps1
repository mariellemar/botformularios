$exclude = @("venv", "botformularios.zip")
$files = Get-ChildItem -Path . -Exclude $exclude
Compress-Archive -Path $files -DestinationPath "botformularios.zip" -Force