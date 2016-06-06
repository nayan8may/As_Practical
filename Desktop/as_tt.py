#!/usr/bin/python3

import sys
import urllib.request
import re


def find_source(src):
	mails = []
	reg_ex = re.compile(r'[-a-z0-9._]+@([-a-z0-9]+)(\.[-a-z0-9]+)+',re.IGNORECASE)
	for m in reg_ex.finditer(src):
		print(m.group())
	
	
def main(args):
	#url = "http://old.gtu.ac.in/Administration.asp"
	
	#try:	
	#	src = urllib.request.urlopen(url).read()
	#except:
	#	print("URL can't Load")
	#	exit(420)
	f = open("gtu_admin.html","r")
	src = f.read()
	find_source(str(src))
	
	
if __name__ == "__main__":
	main(sys.argv[1:])
