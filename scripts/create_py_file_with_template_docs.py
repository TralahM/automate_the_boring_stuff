#!/usr/bin/env python

import sys
import os
from datetime import datetime
from argparse import ArgumentParser

template="""#!/usr/bin/env python

'''
File: {0}
Author: Tralah M Brian <musyoki.tralah@students.jkuat.ac.ke>
Org: TralahTek LLC  <https://github.com/TralahTek>
Date: {1}
'''
""".format(sys.argv[1],datetime.now().date())

if __name__=='__main__':
    parser=ArgumentParser(epilog=template)
    parser.add_argument(action='store',dest='filename',help='python filename to create.')
    args=parser.parse_args()
    with open(args.filename,'w') as py:
        py.write(template)
    print(args.filename,"  written.")
    os.system('vim '+args.filename)
    os.sys.exit(0)
