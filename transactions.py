from PIL import Image
from pytesseract import image_to_string
import urllib.request
import io
import datetime
import re


class Transaction:
    cost_p = r'СУММ[^\d]*([\d]{3})'
    date = datetime.date(2017, 11, 1).strftime('%d:%m:%Y')
    # date = datetime.date.today().strftime('%d:%m:%Y')

    def __init__(self, image):
        self.image = image
        self.card_number = -1
        self.cost = -1

    def reading_picture(self):
        request = image_to_string(Image.open(self.image), lang='rus')
        cost = re.search(self.cost_p, request).group(1)
        if (int(cost) >= int(self.cost)) & (self.date in request) & (str(self.card_number) in request):
            print('Транзакция прошла успеша')
            return int(cost)
        raise Exception('кто-то хочет меня обмануть')

    def make_transaction(self):
        with open('./sim_db', 'r+') as db:
            sumprice, self.card_number, self.cost = db.read().split()
            try:
                sumprice = int(sumprice) + self.reading_picture()
                db.seek(0)
                db.write('{} {} {}'.format(sumprice, self.card_number, self.cost))
            except Exception as ex:
                print(ex)


URL = 'https://pp.userapi.com/c639521/v639521220/6089d/pJfLB3iZoDo.jpg'

with urllib.request.urlopen(URL) as url:
    f = io.BytesIO(url.read())

Transaction(f).make_transaction()
