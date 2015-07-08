import os
import urllib.request
from urllib.error import HTTPError
from urllib.request import urlcleanup

class Scan:
	'''
	1. Check that a file contain newline separated URLS exists
	2. If not return error 
	3. Set the headers to check
	'''
	def __init__(self, fname=None):		
		if fname is not None:
			if(os.path.isfile(fname)):
				self.fname = fname
			else:
				self.fname = None
		# Create a list of headers to check
		self.listHeaders = {"content-security-policy",
						"x-frame-options", 
						"x-xss-protection", 
						"x-content-type-options", 
						"strict-transport-security", 
						"x-download-options", 
						"x-permitted-cross-domain-policies"}
		#Create a dictionay to contain the count of headers
		self.dictHeaderCount = dict()
		#Create a valied url template expected
		self.validurlformat = "<scheme>://<address>:<port>"

	
	#Prints the current list of urls to scan from the file url_list.txt into console, if such a file is provided.		
	def listCurrentUrlList(self):
		if self.fname is  None:
			return False
		file = open(self.fname)			
		try:
			for line in file:
				print(line)
		except:
			return False
		finally:
			file.close()

	'''
	1. Attempts to open the url provided as input
	2. Read the Response Headers 
	3. Iterate through the Headers of interest in the [listHeaders ]list
	4. Creates a dictionary for the detected headers from the [listHeaders] list.
	5. Returns a dictionary containing the header and the number of responses that has this header in [header: #] format
	'''			
	def read_header(self,urlstring):
		if urlstring is None or not urlstring:
			return False
		urllib.request.urlcleanup()		
		try:
			responseData = urllib.request.urlopen(urlstring).info()
			for header in self.listHeaders:
				if responseData.get(header):
					if header in self.dictHeaderCount:
						self.dictHeaderCount[header] += 1
					else:
						self.dictHeaderCount[header] =1
		except HTTPError as e:
			raise HTTPError("Error processing url: "+ urlstring + ". Error: " + e )
			return False
		except Exception as e:
			raise ValueError("Error processing '%s' url. Check that the format is :%s" % (urlstring, self.validurlformat))
			return False		
		return True
				
	'''
	1. Read one url at a time from the file, fname
	2. Call read_header with the url
	3. Repeat #2 and #3 till end of all Urls in scope
	4. Return a dictionary object that contains the response header and the number of responses that has this header in [header: #] format
	'''		
	def scanUrlsInFile(self):
		if self.fname is None:
			return False
		try:
			file = open(self.fname)		
			for line in file:
				if(self.read_header(line)):
					continue
				else:
					raise ValueError("Error processing '%s' url. Check that the format is :%s" % (line, self.validurlformat))
		except Exception as e:
			return False
		finally:
			file.close()
		return self.dictHeaderCount

	'''
	1. Read the url provided as input
	2. Call read_header with the url
	3. Return a dictionary object that contains the response header and the number of responses that has this header in [header: #] format
	'''		
	def scanUrl(self, strUrl):
		if self.read_header(strUrl):
			return self.dictHeaderCount
		return False

