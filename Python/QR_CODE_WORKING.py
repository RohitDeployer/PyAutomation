#pip install pyqrcode

import pyqrcode 
from pyqrcode import QRCode 
  
# String which represent the QR code 
s = "https://www.linkedin.com/in/rohit-more-87a405295/"
  
# Generate QR code
url = pyqrcode.create(s)
  
# Create and save the png file naming "myqr.png" 
#Scalable Vector Graphics
url.svg("mylinkedin.svg", scale = 8) 