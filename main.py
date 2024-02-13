# from dotenv import load_dotenv
import requests
import gspread
from time import sleep
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime
import pytz


def getImage(image):
    if image:
        return image.replace('open', 'thumbnail', 1) + "&sz=w2000"
    return ""


def main():
    time_zone = pytz.timezone("Australia/Sydney")
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    key = ServiceAccountCredentials.from_json_keyfile_name('keys.json', scope)
    increment_row = 'A2'
    while (True):
        now = datetime.now(time_zone).strftime("%H%M%S")
        while int(now) < 90000:  # check if past midnight and before 9am
            now = datetime.now(time_zone).strftime("%H%M%S")
            print(f"No more Letters, it's too late ({now})")
            sleep(300)

        client = gspread.authorize(key)

        sheet = client.open_by_url("https://docs.google.com/spreadsheets/d/1r2mdOmDZoPaOy3IUqUx6AvLdaVhSBVzyEhObbHEUnac")

        worksheet = sheet.get_worksheet(0)
        data_sheet = sheet.get_worksheet(1)
        token = str(data_sheet.acell("D2").value)
        curr = int(data_sheet.acell(increment_row).value)
        sleep_timer = int(data_sheet.acell("C2").value)

        if worksheet.acell("B" + str(curr + 1)).value:
            data = {
                "embeds": [
                    {
                        "title": "#" + str(curr),
                        "description": worksheet.acell("B" + str(curr + 1)).value,
                        "color": 14918853,
                        "image": {
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
        print(f"sleeping for {sleep_timer}")
        sleep(sleep_timer)


if __name__ == "__main__":
    main()
