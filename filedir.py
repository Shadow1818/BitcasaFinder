# encoding: utf-8

import os
import re
import shutil

#path = "/Volumes/Bitcasa Infinite Drive"
out_list_html_name  = u"アップロードされているファイル一覧.html"
test_file_path = "/Users/shibatakeisuke/test.txt"
home_path = os.environ['HOME']
out_list_html_path = home_path + "/" + out_list_html_name
filelist = []

def directory_check():
	cd = os.getcwd()
	dire_name = cd[cd.rfind("/")+1:]
	if (dire_name.find("Bitcasa Infinite Drive") != 0):
		print """
		this directory is different directory
		this script is moveing Bitcasa Directory
		"""
		exit()
	else:
		return cd

def out_html(filelist):
	html = open(out_list_html_path , "w+" )
	#print filelist[0]
	for i in filelist:
		html.writelines(i)
	html.close()

def make_html(filelist):
	html_list = []
	head = """
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
        <title>アップロードされているファイル一覧</title>
    </head>

    <body>

	"""
	foot = """
    </body>
</html>
	"""
	html_list.append(head)

	for i in filelist:
		directory = i["directory"]
		html_list.append("\n<h1>" + directory[(directory.rfind("/")+1):] + "</h1>\n")
		html_list.append("<h3>" + directory + "</h3>")
		filename =  i["filename"]
		sort_nicely(filename)
		#print filename_sort[0]
		for f in filename:
			if re.match("^\.",f) == None:
				filepath = directory + "/" + f
				if (filepath.find("#") != -1):
					filepath = re.sub("#","%23",filepath)
				html_list.append("\n<a target=\"_blank\" href=\" " + filepath +" \" >" + f + "</a><br>\n")
	html_list.append(foot)
	out_html(html_list)

def sort_nicely( l ):
  """ Sort the given list in the way that humans expect.
  """
  convert = lambda text: int(text) if text.isdigit() else text
  alphanum_key = lambda key: [ convert(c) for c in re.split('([0-9]+)', key) ]
  l.sort( key=alphanum_key )
  return l
def cp_html():
	shutil.copy(out_list_html_path,path)
	os.remove(out_list_html_path)


path = directory_check()
o = os.walk(path)
for i in o:
	if (i[2] != [] ):
		#print i[2]
		if (not( len( i[2] ) == 1  and  re.match( "^\.",i[2][0] ) != None ) ):

			directory_and_name = { "directory": i[0] , "filename": i[2] }
			filelist.append(directory_and_name)

# out_html(out_list_html_path,filelist)
# out_html(test_file_path,filelist)

make_html(filelist)
cp_html()


