import os
import fnmatch

# I used this to clean up the .smd files from copying over the textures from the SMD folder.
# I don't care if it's tacky or dangerous.

for subdir, dirs, files in os.walk(os.path.expanduser('F:/FBX')): # noqa
    for filename in files:
        if (fnmatch.fnmatch(filename, "*.smd")):
            path = os.path.join(subdir, filename)
            os.remove(path)
            continue