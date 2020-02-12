import pyqrcode
from pyqrcode import QRCode

site = "www.instagram.com/techhengine"
url = pyqrcode.create(site)

url.svg("techhengineqrcode.svg", scale = 8)
print("QR code generated succesfully!")
