from secureheaderscanner.scan import *

class RunScan:
	objScanUrlsInFile =  scan("secureheaderscanner/url_list.txt")
	result = objScanUrlsInFile.scanUrlsInFile()
	for info in result:
		print("{0}: {1}".format(info,result[info]))


