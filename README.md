# Pokemon USUM Texture Mirror and Waifu2x Upscaler

This python script iterates through a directory and finds every .png with a particular pattern and mirrors it accordingly.

WARNING: This directly replaces the .png files rather than making copies.  Please make sure you have a backup of your extracted directory before using this script!  Also it does not currently work on all the edge-cases that actually are not doubled, so you'll need the originals in order to fix these later.

- This will probably work for Sw/Sh as well but you might need to change some things in the if statements.

These transformations were used on the exported USUM models and textures as part of the fan game Pokemon Infinite.  

--------------

# transform.py

- You will need to create a `venv` and install the `CHAINER` & `PILLOW` module in your virtual environment in order for `transform.py` script to function properly.  This can be done with `pip install chainer` and `pip install pillow`.

- On line 7, where it says `for subdir, dirs, files in os.walk(os.path.expanduser('~danieljsottile/Desktop/TEST')):`, replace the directory with YOUR full pathname for your extracted directory.  This python script does NOT need to be in the same folder as your files.  In this particular example, my directory was named `TEST`, but it will likely be called `SMD` if you use the pyautogui script to extract the models.
