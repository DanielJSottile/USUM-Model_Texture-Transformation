from PIL import Image
import os
import fnmatch
import shutil
import subprocess

# So this will mirror all textures.  However, some textures are not meant to be mirrored.
# This is why I have the original folder of unmirrored as a backup so I can
# manually replace those as needed.

def mainFlip(path, imOrig, filename):
    width, height = imOrig.size
    mode = imOrig.mode
    # make a copy of this image, mirror the copy,
    imCopy = imOrig.copy()
    imFlip = imCopy.transpose(Image.FLIP_LEFT_RIGHT)
    # make a new image 2x the width, then paste them into the new
    imFinal = Image.new(mode, (width * 2, height))
    imFinal.paste(imOrig)
    imFinal.paste(imFlip, (width, 0))
    # image...save it as the OLD image name!
    print(filename + ' mirrored!')
    return imFinal.save(path)

def eyeFlip(path, imOrig, filename):
    w, h = imOrig.size
    m = imOrig.mode
    # Make a new image
    imFinal = Image.new(m, (w * 2, h))
    # crop and make 2 copies of the original
    left = imOrig.crop((0, 0, w / 2, h))
    right = imOrig.crop((w / 2, 0, w, h))
    # flip each one facing outwards
    imFlipLeft = left.transpose(Image.FLIP_LEFT_RIGHT)
    imFlipRight = right.transpose(Image.FLIP_LEFT_RIGHT)
    # paste the left one, then original, then right
    imFinal.paste(imFlipLeft)
    imFinal.paste(imOrig, (round(w / 2), 0))
    imFinal.paste(imFlipRight, (round(w + (w / 2)), 0))
    # image....save it as the OLD image name!
    return imFinal.save(path)
    print(filename + ' mirrored!')

def main():
    for subdir, dirs, files in os.walk(os.path.expanduser('F:/FBX')): # noqa
        for filename in files:
            if (
                fnmatch.fnmatch(filename, "*Body?.tga.png") or
                fnmatch.fnmatch(filename, "*Body??.tga.png") or
                fnmatch.fnmatch(filename, "*Body*Inc.tga.png") or
                fnmatch.fnmatch(filename, "*Body?Mask.tga.png") or
                fnmatch.fnmatch(filename, "*SaCap???.tga.png") or
                fnmatch.fnmatch(filename, "*Pokabu*Inc.tga.png") or
                fnmatch.fnmatch(filename, "*ChonchieInc.tga.png") or
                fnmatch.fnmatch(filename, "*Iris?.tga.png") or
                fnmatch.fnmatch(filename, "*Eff*.tga.png")
            ):
                # ALL the file endings we need for generic mirroring
                path = os.path.join(subdir, filename)
                imOrig = Image.open(path)
                mainFlip(path, imOrig, filename)
                continue
            elif (
                    fnmatch.fnmatch(filename, "*Eye?.tga.png") or
                    fnmatch.fnmatch(filename, "*EyeInc.tga.png") or
                    fnmatch.fnmatch(filename, "*EyeAlpha?.tga.png") or
                    fnmatch.fnmatch(filename, "*Mouth?.tga.png")
            ):
                # open like normal
                path = os.path.join(subdir, filename)
                imOrig = Image.open(path)
                eyeFlip(path, imOrig, filename)
                continue

if __name__ == "__main__":
    main()