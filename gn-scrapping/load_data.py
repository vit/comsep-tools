#import urllib2
import sys, getopt

#try:
#  opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
#except getopt.GetoptError:
#  print 'error'
#  sys.exit(2)

#print(sys.argv)
paper_n = int(sys.argv[1])

url = 'http://elektropribor.spb.ru/gnnew/rn1_2017_annot?paper=%d' % (paper_n)

#response = urllib2.urlopen(url)
#html = response.read()



import urllib.request
#with urllib.request.urlopen(url) as response:
#   html = response.read()
html = urllib.request.urlopen(url).read()


import urllib.request
req = urllib.request.Request(url)
resp = urllib.request.urlopen(req)
html = resp.read().decode(resp.headers.get_content_charset())

#paragraphs = re.findall(r'<p>(.*?)</p>', str(respData))    #ищем все что между этими тэгами     
#for eachP in paragraphs:
#    print(eachP)



print(html)


