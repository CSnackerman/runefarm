write-host 'building dist/rune_farm.exe ...'
& '.\clean.ps1'
pyinstaller.exe .\rune_farm.spec