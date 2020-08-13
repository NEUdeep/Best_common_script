'''
Description:
    the class is used to read file and return the results of exception.
    Every function is named as origin formate of file to except formate, for example: xmltoTree

'''

import os
import sys
import json
import pdb
import cv2
import numpy as np
from xml.etree.ElementTree import ElementTree, Element
import urllib
from urllib.parse import quote

    
def xml_to_tree(xmlFile):
    tree = ElementTree()
    try:
        tree.parse(xmlFile)
    except:
        print("The xml file is parsed failed.")
        return None
    finally:
        return tree
    
    
def json_to_strlists(josnFile):
    with open(jsonFile,'r') as f:
        lines = f.readlines()
        return lines
    return None
    
    
def url_to_image(bucketurl):
    resp = urllib.request.urlopen(quote(bucketurl,safe='/:'))
    image = np.asarray(bytearray(resp.read()), dtype="uint8")
    image = cv2.imdecode(image, cv2.IMREAD_COLOR)
    return image


def path_to_image(imagePath):
    image=cv2.imread(imagePath,cv2.IMREAD_COLOR)
    return image

def img_to_json(filename, bucketurl):
	l_json = {"url": os.path.join(bucketurl,filename),
			"type":"image",
			"label":[{"name": "general", "type": "detection", "version": "1",
			"data":[]}]}
	return json.dumps(l_json)

def xml_to_json(tree,filename, bucketurl):
	bbox_data_json =[]
	root = tree.getroot()
	for child in root:
		if child.tag == 'size':
			for subchild in child:
				if subchild.tag == 'width':
					width = subchild.text
				if subchild.tag == 'height':
					height = subchild.text
		if child.tag == 'object':
			for subchild in child:
				if subchild.tag == 'name':
					label = subchild.text
				if subchild.tag == 'bndbox':
					xmin = int(subchild[0].text)
					ymin = int(subchild[1].text)
					xmax = int(subchild[2].text)
					ymax = int(subchild[3].text)
					bbox_data_json.append({"bbox": [[xmin,ymin],[xmax,ymin],[xmax,ymax],[xmin,ymax]], "class": label})

	l_json = {"url": os.path.join(bucketurl,filename),
			"type":"image",
			"label":[{"name": "general", "type": "detection", "version": "1",
			"data":bbox_data_json}]}

	return json.dumps(l_json)


def file_name(file_dir):   
    L= list()  
    for root, dirs, files in os.walk(file_dir):
        for file in files:  
            if os.path.splitext(file)[1] == '.jpg':  
                L.append(file[0:-4])  
            if os.path.splitext(file)[1] == '.xml':
                L.append(file[0:-4])
            if os.path.splitext(file)[1] == '.png':
                L.append(file)
            if os.path.splitext(file)[1] == '.jpeg':
                L.append(file)
    return L 











    
    
    
    
    

    
    

    

    
    
def main():
    readFile.xmltoTree(xmlFile)
    
    
    
    
if __name__ == "__main__":
    main()
        