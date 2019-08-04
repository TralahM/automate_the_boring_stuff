#! python
from argparse import ArgumentParser
import PyPDF2
''' Read and Manipulate Pdf files Programmatically for Analysis.
Author: Tralah M Brian
Company: TralahTek LLC.
'''
import logging

logging.basicConfig(level=logging.DEBUG,
                    format="%(asctime)s - %(levelname)s - %(message)s")


def combine_pdfs(file1, file2, target_file):
    with open(file1, 'rb') as f1:
        Reader1 = PyPDF2.PdfFileReader(f1)
    with open(file2, 'rb') as f2:
        Reader2 = PyPDF2.PdfFileReader(f2)
    with open(target_file, 'wb') as tgtf:
        Writer = PyPDF2.PdfFileWriter()
        for i in range(Reader1.numPages):
            pobj = Reader1.getPage(i)
            Writer.addPage(pobj)
        for j in range(Reader2.numPages):
            pobj = Reader2.getPage(j)
            Writer.addPage(pobj)
        Writer.write(tgtf)


def read_pdf(pdf_fl):
    Pdf_Reader = PyPDF2.PdfFileReader(open(pdf_fl, 'rb'))
    print("\033[94m %s : \033[92m %d Pages.\033[0m" %
          (pdf_fl, Pdf_Reader.numPages))
    logging.info("Reading First Page ... of %s" % pdf_fl)
    pageobj = Pdf_Reader.getPage(0)
    print(pageobj.extractText())


if __name__ == '__main__':
    ps = ArgumentParser()
    ps.add_argument('-f', '--file', action='store', dest='fl',
                    help=" The Pdf File to open.")
    args = ps.parse_args()
    logging.info("Reading PDF file: " + args.fl)
    read_pdf(args.fl)
