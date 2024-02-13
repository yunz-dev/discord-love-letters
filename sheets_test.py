import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']

key = ServiceAccountCredentials.from_json_keyfile_name('keys.json', scope)
client = gspread.authorize(key)

sheet = client.open_by_url("https://docs.google.com/spreadsheets/d/1r2mdOmDZoPaOy3IUqUx6AvLdaVhSBVzyEhObbHEUnac")

worksheet = sheet.get_worksheet(0)
data_sheet = sheet.get_worksheet(1)

print(worksheet.col_values(2)[1]) # description
print(worksheet.col_values(3)[1]) # image link ()
print(int(data_sheet.acell('A2').value) + 3)
data_sheet.update_acell('A2', 2)
