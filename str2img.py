import base64

from PIL import Image
from io import BytesIO

from picstr import img_str  # img_str is byte-string in picstr.py

byte_data = base64.b64decode(img_str)
image_data = BytesIO(byte_data)


byteImg = Image.open(image_data)
byteImg.save("./export.png", "PNG")
