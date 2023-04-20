#functions.py
from PIL import Image, ImageFilter, ImageDraw, ImageFont

'''
    Load an image file from disk
    :param filename: The file to load
    :return the image object
'''
def load_image( filename ) :
    try:
        myimage = Image.open(filename)
        myimage.load()
    except:
        # It's not good to print here. The UI might be messed up
        # print("Unable to open", filename)
        #"Raise an exception" instead
        raise Exception("Unable to open", filename)
        return None #not much else to do
    return myimage
