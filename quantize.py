from PIL import Image
import numpy

'''
Loads an image from given file path
and stores it as an array. Used for
grayscale only -- other images untested

// param: imgFile - the file path for a given
//        image to be loaded
// return: an array of numbers between 0-255
//         representing the given image file
'''
def load_image_as_array(imgFile):
	img = Image.open(imgFile)
	imgArray = numpy.asarray(img)

	return imgArray 
