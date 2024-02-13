# from dotenv import load_dotenv
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
    # load_dotenv()
    # token = os.getenv('TOKEN')
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    key = ServiceAccountCredentials.from_json_keyfile_name('keys.json', scope)
    increment_row = 'B2'
    night_timer = 0
    while (True):

        client = gspread.authorize(key)

        sheet = client.open_by_url("https://docs.google.com/spreadsheets/d/1r2mdOmDZoPaOy3IUqUx6AvLdaVhSBVzyEhObbHEUnac")

        worksheet = sheet.get_worksheet(0)
        data_sheet = sheet.get_worksheet(1)
        token = str(data_sheet.acell("D2").value)
        curr = int(data_sheet.acell(increment_row).value)
        sleep_timer = int(data_sheet.acell("C2").value)

        if  worksheet.acell("B" + str(curr + 1)).value:
            data = {
                # "content": "insert something here idk",
                "embeds": [
                    {
                        "title": "#" + str(curr),
                        "description": worksheet.acell("B" + str(curr + 1)).value,
                        "color": 14918853,
                        # "author": {
                        #     "name": "AUNSW LOVE LETTERS 2024"
                        # },
                        "image": {
                            # "url": worksheet.col_values(3)[curr]
                            "url": getImage(worksheet.acell("C" + str(curr + 1)).value)
                        }
                    }
                ],
                "attachments": []
            }
            response = requests.post(token, json=data)

            if response.status_code == 204:
                print(f"Love letter #{curr} successfully posted!")
            else:
                print(f"Love letter #{curr} got lost :(")
            data_sheet.update_acell(increment_row, curr + 1)
        night_timer += sleep_timer
        print(f"sleeping for {sleep_timer}")
        sleep(sleep_timer)
        # if night_timer >= 100:
        if night_timer >= 100: # 15 hours
            night_timer = 0
            # sleep(50)
            print("Goodnight Bois!")
            sleep(100) #9 hours


if __name__ == "__main__":
    main()
