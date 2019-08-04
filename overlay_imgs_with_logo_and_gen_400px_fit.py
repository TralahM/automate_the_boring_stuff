from argparse import ArgumentParser
from PIL import Image
import os


def resize(target, ft_size=400):
    t_wd, t_ht = target.size
    if t_wd > ft_size and t_ht > ft_size:
        if t_wd > t_ht:
            t_ht = int((ft_size/t_wd)*t_ht)
            t_wd = ft_size
        else:
            t_wd = int((ft_size/t_ht)*t_wd)
            t_ht = ft_size
        target = target.resize((t_wd, t_ht))
    return target, t_wd, t_ht


def overlay(target, logo, filename):
    print("Resizing %s..." % filename)
    target, width, height = resize(target)
    logo = logo.resize((75, 9))
    lw, lh = logo.size
    print("overlaying logo to %s..." % filename)
    target.paste(logo, (width-lw, height-lh), logo)
    target.save(os.path.join('with_logo', os.path.basename(filename)))


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('-l ', '--logo', action='store',
                        dest='logofn', help='logofilename')
    parser.add_argument('-t', '--target_dir',
                        action='store', dest='target_dir')
    parser.add_argument('-s', action='store_true',
                        help="Only one single Image file", dest='single')
    args = parser.parse_args()
    logo = Image.open(args.logofn)
    os.makedirs('with_logo', exist_ok=True)
    if args.single:
        target = Image.open(args.target_dir)
        overlay(target, logo, args.target_dir)
    else:
        for e in os.listdir(os.path.abspath(args.target_dir)):
            if e.lower().endswith(".png") or e.lower().endswith(".jpg"):
                target = Image.open(os.path.abspath(args.target_dir+e))
                overlay(target, logo, e)
    print("Done....")
