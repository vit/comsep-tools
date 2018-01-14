import subprocess
import os
#import urllib.request
from urllib.request import urlopen, Request
import re
#import bleach
from common_func import *
import sys

'''
html_parser_re = re.compile(r"""
        Гироскопия\sи\sнавигация.*?\n
    (?P<year>\d{4})             # Issued, year
        .*?;
    (?P<issue_num>\d)               # Issue #n (inside the year)
        .*?\(
    (?P<issue_num_abs>\d*)\)                # Issue #n absolute
        .*?\n\s*
    (?P<pages>\d+.*?\d+)            # Published on pages range
        .*?\n\s*УДК\s*\n\s*
    (?P<udk>[\d\.]*)            # UDK
        .*?DOI\s*\n\s*
    (?P<doi>[\d\.\/\-]*)            # DOI
        .*?Arial.*?>.*?\n
    (?P<authors_raw>.*?)\n          # Authors, needs extra parsing
        .*?Georgia.*?>\n\s*
    (?P<title>.*?)\s*\n<            # Paper title
        .*?Georgia.*?>\n\s*
    (?P<abstract>.*?)\s*\n<         # Paper abstract
        .*?Georgia.*?>\n\s*
    (?P<keywords_raw>.*?)\n         # Keywords, needs extra parsing
        .*?mainp.*?>\n\s*
    (?P<authors_affiliation_raw>.*?)            # Authors with affiliation, needs extra parsing
        \s*\n*\s*</p>
""", re.DOTALL | re.VERBOSE)

#dir_name = os.path.abspath(os.path.dirname(__file__))

#years = [2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017]
#years = [2014, 2017]
years = [2017]
'''

src_issues = [
    (2014, 4, 'rrh'),
    (2015, 1, 'ked'),
    (2015, 2, 'bwk'),
    (2015, 3, 'lqb'),
    (2015, 4, 'gre'),
    (2016, 1, 'pft'),
    (2016, 2, 'szr'),
    (2016, 3, 'bnd'),
    (2016, 4, 'jsi'),
    (2017, 1, 'kfc'),
    (2017, 2, 'hjd'),
    (2017, 3, 'kld')
]

for year, issue_n, suffix in src_issues:
    dir_name = os.path.abspath(os.path.dirname(__file__))
    print(year, issue_n)
    subprocess.run(["python3.6", dir_name+"/load_ver_1_issue.py", str(year), str(issue_n), suffix])

