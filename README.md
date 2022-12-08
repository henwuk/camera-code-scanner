# Camera Code Scanner

This script scans barcodes via camera and helps to insert the records into a mongoDB database.

## Prerequisites
### MongoDB 

**1. Atlas**

See [Atlas](https://www.mongodb.com/atlas)

**2. pymongo**

See [this document](https://www.mongodb.com/languages/python)

### Others

**3. opencv-python**

	pip install opencv-python

**4. pyzbar**

	pip install pyzbar


## Usage
Run the following command

	python scanner.py
  
Book record example

	{
 	 '_id': '9780330508537', 
	 'title': "The Hitchhiker's Guide to the Galaxy", 
	 'author': 'Douglas Adams',
 	 'language': 'english',
	 'category': 'sci-fi'
  	}
