import pyqrcode
from pyqrcode import QRCode


s ='https://www.youtube.com/watch?v=rfKiTGj-zeQ'

# Generate QR
url = pyqrcode.create(s)

# 
url.svg('youtube.svg', scale = 8)


