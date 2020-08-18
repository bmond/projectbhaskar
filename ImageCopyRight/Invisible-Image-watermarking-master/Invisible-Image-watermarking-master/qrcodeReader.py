from PIL import Image
from pyzbar.pyzbar import decode
from pyzbar.pyzbar import ZBarSymbol
#image = Image.open('hello_qrcode.png')
data = decode(Image.open('D:\\POC\\ImageCopyRight\\NewMaster\\fragile-watermarking-master\\extracted_lsb_Leena_watermark_extracted.png'), symbols=[ZBarSymbol.QRCODE])
print data
