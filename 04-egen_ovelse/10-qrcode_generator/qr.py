# -*- coding: utf-8 -*-
# @Author: William Berge Groensberg
# @Date:   2025-12-05 17:58:47
# @Last Modified by:   William Berge Groensberg
# @Last Modified time: 2025-12-05 18:04:59



import pyqrcode
from PIL import Image
link = input("paste link here: ")
qr_code = pyqrcode.create(link)
qr_code.png("QRCode.png", scale=10)
Image.open("QRCode.png")