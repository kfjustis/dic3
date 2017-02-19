import sys, getopt
import quantize
import numpy
import matplotlib.pyplot as plt

def main(argv):
  inputFile = ""
  outputFile = ""
  numLevels = ""

  # load file with command line args
  try:
    #opts, args = getopt.getopt(argv, "hi:o:", ["ifile=","ofile="])
    opts, args = getopt.getopt(argv, "hi:o:r:")
  except getopt.GetoptError:
    print("main.py -i <input file> -o <output file> -r <num levels>")
    sys.exit(2)

  for opt, arg in opts:
    if opt == "-h": # help
      print("main.py -i <input file> -o <output file> -r <num levels>")
      sys.exit()
    elif opt in ("-i"):
      inputFile = arg
    elif opt in ("-o"):
      outputFile = arg
    elif opt in ("-r"):
      numLevels = arg

  # load image as array
  imgArray = quantize.load_image_as_array(inputFile)
  print(imgArray)
  print(imgArray.shape)
  print()

  # reshape array
  imgArray = imgArray.flatten()
  print("New dimensions: ", imgArray.shape)
  print()

  # determine length
  imgLength = len(imgArray)
  print("length: ", imgLength)
  print()

  # create reconstruction level array
  '''
  this will just be done with integer elements since our picture
  shouldn't be any larger than an integer max size in pixel width
  '''

  recon = quantize.init_recon_array_random(imgLength, numLevels)
  #recon = quantize.init_recon_array_random(10, 5)
  if (recon == -1):
    print("Invalid args for reconstruction array\n")
    sys.exit()

  # plot reconstruction lines
  plt.hist(imgArray, 255, align='mid')

  i = 0
  while (i < len(recon)):
    if (recon[i] == 1):
      print("idx: ", i)
      print("  val: ", recon[i])
      plt.axhline(i/256, color='red')
      print(i/256)
    i += 1
    
  plt.show()

if __name__ == "__main__":
  main(sys.argv[1:])
