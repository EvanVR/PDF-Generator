import img2pdf
import os
from PIL import Image

def i2pconverter(files, folderName):

    for image in os.listdir(folderName):
        remove_transparency(folderName+"/"+image)

    try:
        print("i2pcon ",folderName)
        os.remove(folderName)
    except Exception as e:
        pass
    pdfname = folderName + ".pdf"
    with open(pdfname,'wb') as f:
        f.write(img2pdf.convert([folderName+"/"+i for i in os.listdir(folderName)]))
    


def remove_transparency(image, bg_colour=(255, 255, 255)):
    im = Image.open(image)
    
    # Only process if image has transparency (http://stackoverflow.com/a/1963146)
    if im.mode in ('RGBA', 'LA') or (im.mode == 'P' and 'transparency' in im.info):
        newimg = im.convert('RGB')
        newimg.save(image, 'PNG', quality=80)

    else:
        pass