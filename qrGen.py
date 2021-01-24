import kivy
from kivy.app import App
from kivy.uix.label import Label

import datetime
import json
from PIL import Image
import qrcode

t = "some shit"

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
#qr.add_data("Time: " + str(t) + "\nLocation: GT Connector")
data =  '{ "day": 1, "month": 2, "year": 3, "site": "connector", "token": "vOEVroRAwn"}'

qr.add_data(json.loads(data))
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")
print("qr created")

#img.show()
img = img.save("asdasdasd.jpg")

from kivy.uix.image import Image

class MyApp(App):
    def build(self):
        return Image(source ='asdasdasd.jpg')

MyApp().run()
