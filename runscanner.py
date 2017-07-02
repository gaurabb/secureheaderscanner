from secureheaderscanner.scan import *

class RunScan:
	objScanUrlsInFile =  scan("secureheaderscanner/url_list.txt")
	result = objScanUrlsInFile.scanUrlsInFile()
	for info in result:
		print("{0}:".format(info))
		for count in result[info]:
			print("\t{0}: {1}".format(count, result[info][count]))


