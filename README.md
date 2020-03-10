# Pokemon USUM Texture Mirror and Waifu2x Upscaler

The first python script iterates through a directory and finds every .png with a particular pattern and mirrors it accordingly, while the second python script applies TWO waifu-2x transformations, upscaling the USUM textures to 1080p quality.

WARNING: These directly replace the .png files rather than making copies.  Please make sure you have a backup of your extracted directory before using this script incase you change your mind!

- Support for Sw/Sh will be included shortly!

These transformations were used on the exported USUM models and textures as part of the fan game Pokemon Infinite.  

--------------

# transform.py

- You will need to create a `venv` and install the `CHAINER` & `PILLOW` module in your virtual environment in order for `transform.py` script to function properly.  This can be done with `pip install chainer` and `pip install pillow`.

- If you are on Windows and Linux and wish to utilize GPU, you should also install CuPy here: https://docs-cupy.chainer.org/en/stable/install.html#install-cupy.  Trust me on this, it's a lot faster and will take much less time!

- Lastly, clone waifu2x-chainer using `git clone https://github.com/tsurumeso/waifu2x-chainer.git`

- PLACE THIS SCRIPT INSIDE THE WAIFU2X-CHAINER FOLDER (after making appropriate adjustments, of course)!

- On line 7, where it says `for subdir, dirs, files in os.walk(os.path.expanduser('~danieljsottile/Desktop/TEST')):`, replace the directory with YOUR full pathname for your extracted directory.  This python script does NOT need to be in the same folder as your files.  In this particular example, my directory was named `TEST`, but it will likely be called `SMD` if you use the pyautogui script to extract the models.

- If you are using this on Mac OSX, then on lines 38, 43, 78, and 83, you will need to take out `-g 0`.  It'll also annoy you and go much slower.
