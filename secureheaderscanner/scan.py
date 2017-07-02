import os
import urllib.request
from urllib.error import HTTPError
from urllib.request import urlcleanup

class scan:
	'''
	Two actions are preformed:
	1. Check that a file containing newline separated URLS exists - if not return an error 
	2. Set the headers to check
	'''
	def __init__(self, fname=None):		
		if fname is not None:
			if(os.path.isfile(fname)):
				print("INFO: URL file exists")
				self.fname = fname
			else:
				print("INFO: URL file does not exists")
				self.fname = None
		# List of header names to check
		'''self.listHeaders = {
						"content-security-policy",
						"x-frame-options", 
						"x-xss-protection", 
						"x-content-type-options", 
						"strict-transport-security", 
						"x-download-options", 
						"x-permitted-cross-domain-policies"}
						'''
		# #Create a dictionay to contain the count of headers detected
		# self.dictUrlToHeaderMap = dict([
		# 				("content-security-policy", 0),
		# 				("x-frame-options", 0), 
		# 				("x-xss-protection", 0), 
		# 				("x-content-type-options", 0), 
		# 				("strict-transport-security", 0), 
		# 				("x-download-options", 0), 
		# 				("x-permitted-cross-domain-policies", 0)
		# 				])
		self.finalResult = dict()
		#Create a valied url template expected
		self.validurlformat = "<scheme>://<address>:<port>"

	
	'''
	Prints the current list of urls to scan from the file url_list.txt into console, if such a file exists.
	'''			
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
			# Create a dictionay to contain the count of headers detected
			# ToDO: There must be a better way then to create it every time but 
			# making it global screws up the header counts
			dictUrlToHeaderMap = dict([
						("content-security-policy", 0),
						("x-frame-options", 0), 
						("x-xss-protection", 0), 
						("x-content-type-options", 0), 
						("strict-transport-security", 0), 
						("x-download-options", 0), 
						("x-permitted-cross-domain-policies", 0)
						])
			responseData = urllib.request.urlopen(urlstring).info()
			for entry in dictUrlToHeaderMap:
				getTheHeader = responseData.get(entry)
				if getTheHeader:
					dictUrlToHeaderMap[entry] += 1			
		except HTTPError as e:
			raise HTTPError("Error processing url: {0}. Error: {1}".format(urlstring, e ))
			return False
		except Exception as e:
			raise ValueError("Error processing {0} url. Check that the format is :{1}".format(urlstring, self.validurlformat))
			return False		
		# Create the final dictionaty object that maps the URL and the header count results
		self.finalResult[(urlstring.rstrip())] = dictUrlToHeaderMap
		return True
				
	'''
	1. Read one url at a time from the file, fname
	2. Call read_header with the url
	3. Repeat #2 and #3 till end of all Urls in scope
	4. Return a dictionary object that contains the response header and the number of responses that has this header in [header: #] format
	'''		
	def scanUrlsInFile(self):
		if self.fname is None:
			print("ERROR: File containing URLs is not available")
			return False
		try:
			print("INFO: Opening the URL file")
			file = open(self.fname)		
			for line in file:
				print("INFO: Checking for {0}".format(line.rstrip()))
				if(self.read_header(line)):
					continue
				else:
					raise ValueError("ERROR: Error processing '%s' url. Check that the format is :%s" % (line, self.validurlformat))
		except Exception as e:
			raise ValueError("ERROR: {0}".format(e))
		finally:
			file.close()
		return self.finalResult

	'''
	1. Read the url provided as input
	2. Call read_header with the url
	3. Return a dictionary object that contains the response header and the number of responses that has this header in [header: #] format
	'''		
	def scanUrl(self, strUrl):
		if self.read_header(strUrl):
			return self.dictHeaderCount
		return False

