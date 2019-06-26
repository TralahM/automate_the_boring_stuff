#!/usr/bin/env python
'''
A script to be used as an English dictionary to quickly lookup words without consulting a \
    physical or online dictionary..
Automating the boring task of looking up the meaning of words.

Requirements:
    1. argparse --- for parsing command line arguments
    2. difflib --- for comparing similarities in words
    3. json  --- for reading json data

Usage: python lookup_meaning.py <English Word> [-h --help]

Author: Tralah M Brian <https://github.com/TralahM>
Org: TralahTek LLC.
Copyright: 2019 (All Rights Reserved)
Licence:  MIT.
'''
import json
from difflib import get_close_matches
from argparse import ArgumentParser

data = json.load(open("english_dict.json"))
# data = json.load(open("english_dict.json"))


def translate(w):
    w = w.lower()
    if w in data:
        result = data[w]
        if not isinstance(result, list):
            return list(result)
        return result
    elif len(get_close_matches(w, data.keys())) > 0:
        yn = input("Did you mean %s instead? Enter Y if yes, or N if no: " %
                   get_close_matches(w, data.keys())[0])
        if yn.upper() == "Y":
            result = data[get_close_matches(w, data.keys())[0]]
            if not isinstance(result, list):
                return list(result)
            return result
        elif yn.upper() == "N":
            return ["The word doesn't exist. Please double check it.", ]
        else:
            return ["We didn't understand your entry.", ]
    else:
        return ["The word doesn't exist. Please double check it.", ]


if __name__ == '__main__':
    parser = ArgumentParser(
        epilog="Author: Tralah M Brian <musyoki.tralah@students.jkuat.ac.ke>\nOrg: TralahTek LLC.\nCopyright: 2019 (All Rights Reserved.\n)")
    parser.add_argument('word', action='store',
                        help="The English word to lookup.")
    args = parser.parse_args()
    print("\t\033[93m %s Definition:\t\033[0m" % (args.word))
    print("\n".join(translate(args.word)))
