import os
import json
from xml.etree.ElementTree import ElementTree, Element
import urllib
from urllib.parse import quote

src_file = "/workspace/mnt/data/datasets/RaoCheng/train_960_noempty.txt"
src_voc = "/workspace/mnt/data/datasets/RaoCheng"
det_file = "./labelx.json"

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
					bbox_data_json.append({"bbox": [[xmin,ymin],[xmax,ymin],[xmax,ymax],[xmin,ymax]], "class": [label]})

	l_json = {"url": os.path.join(bucketurl,filename),
			"type":"image",
			"label":[{"name": "general", "type": "detection", "version": "1",
			"data":bbox_data_json}]}

	return json.dumps(l_json,)



def xml_to_tree(xmlFile):
    tree = ElementTree()
    try:
        tree.parse(xmlFile)
    except:
        print("The xml file is parsed failed.")
        return None
    finally:
        return tree
    


lines = open(src_file,'r')
for line in lines:
    
    xml_file = line.replace("JPEGImages","Annotations").replace(".jpg",".xml").strip('\n')
    file_name = line
    
    xml_tree = xml_to_tree(xml_file)
    json_str = xml_to_json(xml_tree,"",file_name.strip("\n"))
    with open(det_file,'w') as bw:
        bw.write(json_str+'\n')

