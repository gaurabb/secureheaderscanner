import unittest
import os

class SecureHeaderScannerTest(unittest.TestCase):
	def check_file_with_urls_exists(self):
		self.assertEqual(os.path.isfile('url_list.txt'), True, 'File does not exists.')

	def check_file_with_urls_not_empty(self):
		self.assertEqual(os.path.getsize('url_list.txt')>0, True, 'File is empty.')
			
	def test_run_scan_read_report_header(self):
		# The file containing a list of websites to check is made available in the root scan folder
		self.check_file_with_urls_exists()
		# The file is not empty - contains one website url per line
		self.check_file_with_urls_not_empty()
		#self.fail('Finish the test') ##self.fail just fails no matter what, producing the error message given.  
		# The scan reads one url at a time and sends out a http GET request to the website
		# The scanner reads all the response headers and reports the ones listed in the config file in a dictionary format. Check This.
		pass

if __name__=='__main__':
	unittest.main(warnings='ignore')
