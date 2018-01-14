import sys

html = sys.stdin.read()

#print(html)


import re

#pattern=re.compile(these_regex)
#m = re.search('(?<=abc)def', 'abcdef')
#m.group(0)


#paragraphs = re.findall(r'Гироскопия и навигация(.*?)<br>', str(html))
#paragraphs = re.findall(r'Гироскопия и навигация(.*)<br>', str(html), re.MULTILINE)
#paragraphs = re.findall(r'Гироскопия и навигация(.*)<br>', html, re.MULTILINE)
#paragraphs = re.findall(r'<div(.*?)</div>', html, re.MULTILINE)
#paragraphs = re.findall(r'2017(.*?)96', html, re.MULTILINE|re.DOTALL)
#paragraphs = re.findall(r'Гироскопия и навигация.*\n(\d{4}).*?;(\d)\s*\n\s*([\d+.?\d+])', html, re.MULTILINE|re.DOTALL)
#paragraphs = re.findall(r'Гироскопия и навигация.*\n(\d{4}).*?;(\d).*\n\s*(\d+.*?\d+).*\n\s*УДК\s*\n\s*([\d\.]*).*DOI\s*\n\s*([\d\.\/\-]*)', html, re.MULTILINE|re.DOTALL)


#pat = re.compile(r'Гироскопия и навигация.*\n(\d{4}).*?;(\d).*\n\s*(\d+.*?\d+).*\n\s*УДК\s*\n\s*([\d\.]*).*DOI\s*\n\s*([\d\.\/\-]*)', re.MULTILINE|re.DOTALL)
#parts = pat.findall(html)

#pat = re.compile(r'Гироскопия и навигация.*\n(?P<year>\d{4}).*?;(\d).*\n\s*(\d+.*?\d+).*\n\s*УДК\s*\n\s*([\d\.]*).*DOI\s*\n\s*([\d\.\/\-]*)', re.MULTILINE|re.DOTALL)
#parts = pat.findall(html)
#print(parts)

#pat = re.match(r'Гироскопия и навигация.*\n(?P<year>\d{4}).*?;(\d).*\n\s*(\d+.*?\d+).*\n\s*УДК\s*\n\s*([\d\.]*).*DOI\s*\n\s*([\d\.\/\-]*)', html, re.MULTILINE|re.DOTALL)
#pat = re.search(r"""Гироскопия и навигация.*\n(?P<year>\d{4}).*?;(\d).*\n\s*(\d+.*?\d+).*\n\s*УДК\s*\n\s*([\d\.]*).*DOI\s*\n\s*([\d\.\/\-]*)""", html, re.DOTALL|re.DOTALL|re.VERBOSE)

'''
pat = re.search(r"""
	Гироскопия и навигация.*\n
	(?P<year>\d{4})
	.*?;
	(?P<num>\d)
	.*\n\s*
	(?P<pages>\d+.*?\d+)
	.*\n\s*УДК\s*\n\s*
	(?P<udk>[\d\.]*)
	.*DOI\s*\n\s*
	(?P<doi>[\d\.\/\-]*)
""", html, re.DOTALL|re.VERBOSE)
'''

#pat = re.search(r"""Гироскопия и навигация.*\n(?P<year>\d{4})""", html, re.MULTILINE|re.DOTALL|re.VERBOSE)
#pat = re.search(r"""Гироскопия и навигация.*\n(?P<year>\d{4})""", html, re.MULTILINE|re.DOTALL|re.VERBOSE)
#pat = re.search(r"""Гироскопия и навигация.*\n(?P<year>\d{4})""", html, re.DOTALL|re.VERBOSE)

#reg = re.compile(r"""Гироскопия и навигация.*\n(?P<year>\d{4})""", re.DOTALL|re.VERBOSE)
reg = re.compile(r"""
		Гироскопия\sи\sнавигация.*\n
	(?P<year>\d{4})				# Issued, year
  		.*?;
	(?P<num>\d)				# Journal #n (inside the year)
		.*\n\s*
	(?P<pages>\d+.*?\d+)			# Published on pages range
		.*\n\s*УДК\s*\n\s*
	(?P<udk>[\d\.]*)			# UDK
		.*DOI\s*\n\s*
	(?P<doi>[\d\.\/\-]*)			# DOI
		.*?Arial.*?>.*?\n
	(?P<authors_raw>.*?)\n			# Authors, needs extra parsing
		.*?Georgia.*?>\n\s*
	(?P<title>.*?)\s*\n<			# Paper title
		.*?Georgia.*?>\n\s*
	(?P<abstract>.*?)\s*\n<			# Paper abstract
		.*?Georgia.*?>\n\s*
	(?P<keywords_raw>.*?)\n			# Keywords, needs extra parsing
""", re.DOTALL|re.VERBOSE)
pat = reg.search(html)

rrr = pat.groupdict()
print(rrr)

#for eachP in paragraphs:
#    print(eachP)
