from PIL import Image
import numpy as np

import sys, getopt

def main(argv):
    ratio = 8
    inputfile = ""
    outputfile = "out"

    try:
        opts, args = getopt.getopt(argv[1:],"i:o:r:h",["input=","output=","ratio=","help"])
    except getopt.GetoptError:
        print(" -i <inputfile> -o <output_suffix> -r")
        sys.exit(2)
    for opt, arg in opts:
        if opt in ("-h", "--help"):
            print (argv[0] +  " -i <inputfile> -o <outputfile")
            sys.exit()
        elif opt in ("-i", "--input"):
            inputfile = arg
        elif opt in ("-o", "--output"):
            outputfile = arg
        elif opt in ("-r", "--ratio"):
            ratio = int(arg)

    if inputfile == "":
        print (argv[0] +  " -i <inputfile> -o <outputfile")
        sys.exit(2)

    i = Image.open(inputfile)
    cols = i.getcolors()
    pix = i.load()

    for c in cols:
        col_img = Image.new('RGB', i.size, (255,255,255,255))
        col_pix = col_img.load()
        col = c[1]
        for x in range(i.width):
            for y in range(i.height):
                if pix[x,y] == col:
                    col_pix[x,y] = (0,0,0,255)

        im_resize = col_img.resize((i.width*ratio, i.height*ratio), Image.NEAREST)
        name = outputfile + str(col)+".png"
        im_resize.save(name.replace(" ", ""))

if __name__ == "__main__":
   main(sys.argv)