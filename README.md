# Nomad Teekron

## Installation
```
git clone https://github.com/yi1z/nomad_teekron.git
python -m venv venv
venv/Scripts/activate.bat
pip install -r reqirements.txt
playwright install
```

## How to use
Add the urls of pages of the products in `fetch_urls.py`, then edit and run `python src\main.py` in terminal from the root directory, the output will be stored in `src\results\`. Path to output file can be modified in `fetch_urls.py`.
