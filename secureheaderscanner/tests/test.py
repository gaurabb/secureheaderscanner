import unittest
from scan import *

class TestSecureHeaderScanner(unittest.TestCase):
	
	'''
	UNIT TEST FOR listCurrentUrlList
	'''
	def test_listCurrentUrlList_pass(self):
		'''Test that the function lists all the Urls in the url_list.txt file in the root'''
		obj = Scan("url_list.txt")
		result = obj.listCurrentUrlList()
		self.assertEqual(result, True)
	
	def test_listCurrentUrlList_fail(self):
		'''Test that the function returns False when url_list.txt file is not present or empty'''
		obj = Scan("url_list1.txt")
		result = obj.listCurrentUrlList()
		self.assertEqual(result, False)
	'''
	UNIT TEST FOR read_header
	'''
	def test_read_header_pass(self):
		obj = Scan("url_list.txt")
		result = obj.read_header("http://bing.com")
		self.assertEqual(result, True)
	
	def test_read_header_fail(self):
		obj = Scan("url_list.txt")
		result = obj.read_header("")
		self.assertEqual(result, False)
		
	'''
	UNIT TEST FOR scan
	'''
	def test_scan_pass(self):
		obj = Scan("url_list.txt")
		result = obj.scan()
		self.assertEqual(isinstance(result,dict), True)
	
	def test_scan_fail(self):
		obj = Scan("url_list1.txt")
		result = obj.scan()
		self.assertEqual(result, False)

if __name__ == '__main__':
    unittest.main()
