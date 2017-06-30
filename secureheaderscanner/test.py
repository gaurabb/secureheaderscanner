import unittest
from scan import *

class TestSecureHeaderScanner(unittest.TestCase):
	
	def test_can_report_headers_for_single_url(self):
		objScanUrl = scan()
		result = objScanUrl.scanUrl("https://www.twitter.com")
		#self.assertEqual(result, True, "Failed to scan the single url supplied.")
		assert isinstance(result, dict), "Scan of the single url did not return a dictionary object as expected."

	def test_can_report_headers_for_urls_in_a_file(self):
		objScanUrlsInFile = scan("/root/secureheaderscanner/url_list.txt") # ToDo: The path is hardcoded and needs to be updated.
		result = objScanUrlsInFile.scanUrlsInFile()
		assert isinstance(result, dict), "Failed to scan the Urls in the file."

if __name__ == '__main__':
	unittest.main(warnings='ignore') # To prevent: "./usr/lib/python3.2/socket.py:350: ResourceWarning: unclosed <socket.socket object, fd=4, family=2, type=1, proto=6>  self._sock = None
	unittest.main()
