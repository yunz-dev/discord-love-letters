from dotenv import load_dotenv
import requests
import os
import gspread
from time import sleep
from oauth2client.service_account import ServiceAccountCredentials

def getImage(image):
    if image:
        return image.replace('open', 'thumbnail', 1) + "&sz=w2000"
    return ""

def main():
    load_dotenv()
    token = os.getenv('TOKEN')
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    key = ServiceAccountCredentials.from_json_keyfile_name('keys.json', scope)
    increment_row = 'B2'
    night_timer = 0
    while (True):

        client = gspread.authorize(key)

        sheet = client.open_by_url("https://docs.google.com/spreadsheets/d/1r2mdOmDZoPaOy3IUqUx6AvLdaVhSBVzyEhObbHEUnac")

        worksheet = sheet.get_worksheet(0)
        data_sheet = sheet.get_worksheet(1)
        curr = int(data_sheet.acell(increment_row).value)
        sleep_timer = int(data_sheet.acell("C2").value)

        if  worksheet.col_values(2)[curr]:
            data = {
                # "content": "insert something here idk",
                "embeds": [
                    {
                        "title": "#" + str(curr),
                        "description": worksheet.col_values(2)[curr],
                        "color": 14918853,
                        # "author": {
                        #     "name": "AUNSW LOVE LETTERS 2024"
                        # },
                        "image": {
                            # "url": worksheet.col_values(3)[curr]
                            "url": getImage(worksheet.col_values(3)[curr])
                        }
                    }
                ],
                "attachments": []
            }
            response = requests.post(token, json=data)

            if response.status_code == 204:
                print("Love letter successfully posted!")
            else:
                print("Love letter got lost :(")
            data_sheet.update_acell(increment_row, curr + 1)
        night_timer += sleep_timer
        sleep(sleep_timer)
        if night_timer >= 100:
        # if night_timer >= 54000:
            night_timer = 0
            sleep(50)
            # sleep(32400)


if __name__ == "__main__":
    main()
