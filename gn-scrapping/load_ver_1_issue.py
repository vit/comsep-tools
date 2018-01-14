import sys
import os
import subprocess
from urllib.request import urlopen, Request, urlretrieve
import re
import xml.etree.ElementTree as ET
import shutil

from common_func import *


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


if len(sys.argv) < 4:
    print ("""
        Use with 3 args: year isuue_number secret_suffix
        For example: 2017 3 kld
        """)
    sys.exit(2)

year = int(sys.argv[1])
issue_n = int(sys.argv[2])
suffix = str(sys.argv[3])
file_path = '{0:04d}_gn_{1:02d}{2:s}'.format(year, issue_n, suffix)


# Read and Parse HTML Pages
issues={}
pack = {}
year_id = '{0:04d}'.format(year)
issue_id = '{0:04d}_{1:02d}'.format(year, issue_n)
for paper_n in range(1, 21):
#for paper_n in range(1, 3):
    html = read_html_for(year, issue_n, paper_n)
    if html != None:
        paper_id = '{0:04d}_{1:02d}_{2:02d}'.format(year, issue_n, paper_n)
        paper_dict = parse_html(html_parser_re, html)
        if paper_dict:
            paper_dict['file_url'] = FILES_URL_BASE+"/"+ file_path + '/{0:04d}_{1:02d}_{2:02d}.pdf'.format(year, issue_n, paper_n)
            paper_dict['paper_num'] = paper_n
            print('+', end='', flush=True)
        else:
            print('-', end='', flush=True)
        pack[paper_id] = paper_dict
issues[issue_id] = pack

print()

#from ruamel.yaml import YAML

#yaml=YAML()
#yaml.default_flow_style = False
#issues_y = yaml.dump(issues, sys.stdout)

#print(issues_y)

'''
META_TAGS_MAP = {
    'title': ('title', 'none'),
    'year': ('date', 'issued'),
    'title': ('title', 'none'),
    'title': ('title', 'none'),
    'title': ('title', 'none'),
    'title': ('title', 'none'),
    'title': ('title', 'none'),
    'title': ('title', 'none'),
}
'''

def get_dc_tags(p_data):
    rez = []
    rez.append( ('title', 'none', p_data['title']) )
    rez.append( ('description', 'abstract', p_data['abstract']) )
    rez.append( ('date', 'issued', p_data['year']) )
    try:
        for author in p_data['authors']:
            rez.append( ('creator', 'none', author) )
    except:
        pass
    try:
        for keyword in p_data['keywords']:
            rez.append( ('subject', 'none', keyword) )
    except:
        pass
    return rez

def make_item_files(p_data, f_path, f_name):
    with open(f_path+"/contents", "w", encoding="utf-8") as f:
        f.write(f_name)

    root = ET.Element('dublin_core')
    for a1, a2, v in get_dc_tags(p_data):
        elm = ET.SubElement( root, 'dcvalue', attrib={'element': a1, 'qualifier': a2} )
        elm.text = v
    tree = ET.ElementTree(root)
    tree.write(f_path+"/dublin_core.xml", encoding="utf-8", xml_declaration=True)




arch_path = "archives"

# Download Files
for i_id, i_data in issues.items():
    issue_path = year_id + "/" + i_id + "/"
    for p_id, p_data in i_data.items():
        paper_path = issue_path + p_id
        if p_data and p_data['file_url']:
            os.makedirs(paper_path)
            f_name = '{0:04d}_{1:02d}_{2:02d}.pdf'.format( int(p_data['year']), int(p_data['issue_num']), int(p_data['paper_num']) )
            make_item_files(p_data, paper_path, f_name)
            ff_name = paper_path + "/" + f_name
            urlretrieve(p_data['file_url'], ff_name)
            print('.', end='', flush=True)
    os.makedirs(arch_path, exist_ok=True)
    arch_file_name = arch_path+"/"+i_id
    shutil.make_archive(arch_file_name, 'zip', issue_path)

print()


import xml.etree.ElementTree as ET

