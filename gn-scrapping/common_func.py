import subprocess
import os
from urllib.request import urlopen, Request
import re

import contextlib

url_base = "http://elektropribor.spb.ru/gnnew/"

FILES_URL_BASE = "http://elektropribor.spb.ru/gn/numbers/"


def read_html_for(year, issue_n, paper_n):
    html = None
    try:
        url = url_base + "rn%d_%d_annot?paper=%d" % (issue_n, year, paper_n)
        req = Request(url)
        with contextlib.closing(urlopen(req)) as resp:
            html = resp.read().decode(resp.headers.get_content_charset())
    except:
        html = None

    return html


def parse_html(parser_re, html):
    try:
        #print("parser_re.search:")
        pat = parser_re.search(html)
        #print("pat.groupdict:")
        p_dict = pat.groupdict()
        p_dict['authors'] = []
        #'''
        try:
            authors_raw = p_dict.get('authors_raw')
            authors_raw_list = authors_raw.split(',')
            p_dict['authors'] = list(
            map(
                ( lambda x: re.sub(r'<.*?></.*?>', '', x).strip() ),
                    authors_raw_list
                )
            )
            keywords_raw = p_dict.get('keywords_raw')
            keywords_raw_list = keywords_raw.split(',')
            p_dict['keywords'] = list(
            map(
                ( lambda x: x.strip() ),
                    keywords_raw_list
                )
            )
        except:
            None
        #'''
    except:
        p_dict = None
    return p_dict
