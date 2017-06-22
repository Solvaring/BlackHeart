try:
    import Image
except ImportError:
    from PIL import Image
import pytesseract

img = Image.open(r'D:\Myscripts\BlackHeart\testimages\screenshot001.png')
img.load()
i = pytesseract.image_to_string(img)
print i