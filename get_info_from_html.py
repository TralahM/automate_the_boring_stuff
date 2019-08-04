#! python
from bs4 import  BeautifulSoup
from argparse import ArgumentParser
import re

def get_imgs_list(fp):
    fobj=open(fp,'r')
    soup=BeautifulSoup(fobj,features="html.parser")
    fobj.close()
    imgs=list(set(soup.find_all('img')))
    return imgs

def get_links_list(fp):
    fobj=open(fp,'r')
    soup=BeautifulSoup(fobj,features="html.parser")
    fobj.close()
    links=list(set(soup.find_all('a')))
    return links
def get_tables_list(fp):
    fobj=open(fp,'r')
    soup=BeautifulSoup(fobj,features="html.parser")
    fobj.close()
    tables=list(set(soup.find_all('table')))
    return tables
def get_meta_list(fp):
    fobj=open(fp,'r')
    soup=BeautifulSoup(fobj,features="html.parser")
    fobj.close()
    meta=list(set(soup.find_all('meta')))
    return meta
def get_text_repr(fp):
    fobj=open(fp,'r')
    soup=BeautifulSoup(fobj,features="html.parser")
    fobj.close()
    text=soup.find_all('html')
    return [h.text for h in text ]
def get_headers_list(fp):
    fobj=open(fp,'r')
    soup=BeautifulSoup(fobj,features="html.parser")
    fobj.close()
    headers=[]
    for  h in ['h1','h2','h3','h4','h5','h6']:
        headers.extend(list(set(soup.find_all(h))))
    return headers
def get_internal_links_list(fp):
    links=get_links_list(fp)
    internals=[]
    for link in links:
        if link['href'].startswith('/'):
            internals.append(link)
    return internals
def get_el_attribs(fp,el):
    fobj=open(fp,'r')
    soup=BeautifulSoup(fobj,features='html.parser')
    fobj.close()
    el=soup.find(el)
    return el.attrs
def get_els_list_attribs(fp,el):
    fobj=open(fp,'r')
    soup=BeautifulSoup(fobj,features="html.parser")
    fobj.close()
    elems=list(set(soup.find_all(el)))
    keys=[]
    for e in elems:
        keys.extend(list(e.attrs.keys()))
    return set( keys )


