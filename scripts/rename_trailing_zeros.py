#!/usr/bin/env python
import os
import shutil
from argparse import ArgumentParser


def rename_files(dest_dir, directory=os.getcwd()):
    """rename all files in directory and sub directories ending with 0 into a single folder on the current working dir. """
    directory = os.path.abspath(directory)
    # os.chdir(directory)
    print("\n\t\tSource Folder: \033[92m %s \033[90m" % (directory))
    if os.path.exists(os.path.abspath(dest_dir)):
        dest_dir = os.path.abspath(dest_dir)
        # print("\033[91mDestination Folder:\033[94m %s\033[0m" % (dest_dir))
    else:
        os.mkdir(os.path.abspath(dest_dir))
        # print("\033[93mCreating new Folder:\033[94m %s\033[0m" %
        # (os.path.abspath(dest_dir)))
    counter = 0
    for dird, subdirs, filenames in os.walk(directory):
        # loop over dird contents
        # print("Walking ...  \033[94m %s \033[0m" % (dird))
        for fl in filenames:
            lfl = fl.lower()
            if not lfl.endswith(".png") or not lfl.endswith(".jpg") or not lfl.endswith(".jpeg"):
                # print(fl,dest_dir)
                try:
                    if fl[-1] == 'p':
                        shutil.move(os.path.abspath(directory+'/'+fl),
                                    os.path.abspath(directory+'/'+fl+'ng'))
                    else:
                        shutil.move(os.path.abspath(directory+'/'+fl), os.path.abspath(
                            directory+'/'+fl+'pg'))
                    counter += 1
                except Exception as e:
                    pass
        for dir in subdirs:
            rename_files(dest_dir, os.path.abspath(directory+"/"+dir))
    print("\033[95m %d \033[0m files renamed.\n" % counter)


if __name__ == '__main__':
    # print(shutil.__name__)
    ps = ArgumentParser()
    ps.add_argument('-d', '--destination-dir', action='store',
                    dest="dest_dir", default="All_Photos")
    ps.add_argument('-s', '--source-dir', action='store',
                    dest='src_dir', default=os.getcwd())
    args = ps.parse_args()
    rename_files(args.dest_dir, args.src_dir)
