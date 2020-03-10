from PIL import Image
import os
import fnmatch
import shutil


for subdir, dirs, files in os.walk(os.path.expanduser('~danieljsottile/Desktop/TEST')): # noqa
    for filename in files:
        if (
            # List of Exceptions I need to add:
            # pm0047_00_BodyB1.png
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
            imFinal.save(path)
            print(filename + ' mirrored!')
            # now we're gonna do two transformations with waifu
            os.system(f"python waifu2x.py -m noise_scale -n 2 -i {path} -a 0 -g 0") # noqa
            # then we have to move it back before it does it again. . .
            waifuPath = os.path.expanduser(f'~danieljsottile/projects/model_image_transform/waifu2x-chainer/{filename}') # noqa
            shutil.move(waifuPath, path)
            print(filename + ' transformed and moved x1')
            os.system(f"python waifu2x.py -m noise_scale -n 2 -i {path} -a 0 -g 0") # noqa
            shutil.move(waifuPath, path)
            print(filename + ' transformed and moved x2!')
            continue
        elif (
                # List of Exceptions I need to add:
                # pm0491_00_Eye1.tga.png
                # pm0491_00_Eye2.tga.png
                # pm0884_00_EyeInc.tga.png
                fnmatch.fnmatch(filename, "*Eye?.tga.png") or
                fnmatch.fnmatch(filename, "*EyeInc.tga.png") or
                fnmatch.fnmatch(filename, "*EyeAlpha?.tga.png") or
                fnmatch.fnmatch(filename, "*Mouth?.tga.png")
        ):
            # open like normal
            pathTwo = os.path.join(subdir, filename)
            imOrigTwo = Image.open(pathTwo)
            w, h = imOrigTwo.size
            m = imOrigTwo.mode
            # Make a new image
            imFinalTwo = Image.new(m, (w * 2, h))
            # crop and make 2 copies of the original
            left = imOrigTwo.crop((0, 0, w / 2, h))
            right = imOrigTwo.crop((w / 2, 0, w, h))
            # flip each one facing outwards
            imFlipLeft = left.transpose(Image.FLIP_LEFT_RIGHT)
            imFlipRight = right.transpose(Image.FLIP_LEFT_RIGHT)
            # paste the left one, then original, then right
            imFinalTwo.paste(imFlipLeft)
            imFinalTwo.paste(imOrigTwo, (round(w / 2), 0))
            imFinalTwo.paste(imFlipRight, (round(w + (w / 2)), 0))
            # image....save it as the OLD image name!
            imFinalTwo.save(pathTwo)
            print(filename + ' mirrored!')
            # now we're gonna do two transformations with waifu
            os.system(f"python waifu2x.py -m noise_scale -n 2 -i {path} -a 0 -g 0") # noqa
            # then we have to move it back before it does it again. . .
            waifuPathTwo = os.path.expanduser(f'~danieljsottile/projects/model_image_transform/waifu2x-chainer/{filename}') # noqa
            shutil.move(waifuPathTwo, pathTwo)
            print(filename + ' transformed and moved x1')
            os.system(f"python waifu2x.py -m noise_scale -n 2 -i {path} -a 0 -g 0") # noqa
            shutil.move(waifuPathTwo, pathTwo)
            print(filename + ' transformed and moved x2!')
            continue
