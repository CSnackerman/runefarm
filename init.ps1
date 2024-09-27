write-host "creating virtual environment..."
python.exe -m venv venv

write-host "activating virtual environment..."
& '.\venv\Scripts\Activate.ps1'

write-host "installing dependencies..."
pip install -r requirements.txt