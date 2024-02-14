# Discord Love Letters 
# DELETE JSON FILES AND KEYS BEFORE PUBLIC!!!
A Python3 script that utilises discord webhooks in order to send anonymous love letters to a discord server. Love letters are stored in a google sheet (which gets it's data from a google form in real time) and is fetched using the google sheets API.

## Installation
1. clone repo
2. Run: 
```bash
source env/bin/activate
```
3. Install dependencies with `pip install -r requirements.txt` (actually you can skip this haha cuz i accidently pushed to main)
4. Replace json file with your own google api key
5. Fill in empty cells with corresponding information
6. Run `python3 main.py`

## ~~TO-DO~~ Done
1. webhooks
2. sheets working
3. test working
4. anonymous working
5. deploy


# Credit where credit is due:
- [zfere](https://github.com/zfere/): helping out with embedding images from google-drive
- [MonkieeBoi](https://github.com/MonkieeBoi): Look over code


