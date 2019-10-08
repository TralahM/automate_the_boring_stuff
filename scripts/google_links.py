from argparse import ArgumentParser
from googlesearch import search
import os

# try:
#     links=search("site:github.com scrapy",num=45)
#     for link in links:
#         print(link)
# except:
#     print("Search Error")

if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('-q', action='store', dest='q')
    parser.add_argument('-n', action='store', dest='n', type=int, default=13)
    args = parser.parse_args()
    try:
        links = search(args.q, num=args.n)
        for link in links:
            print(link)
            if link.endswith(".pdf") or link.endswith(".csv") or link.endswith(".json") or link.endswith(".xlsx"):
                os.system("wget  "+link)
    except:
        print("Search Error")
