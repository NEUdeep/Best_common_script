from fileAPI import xml_to_tree , xml_to_json

def xml2labelx(annopath,bucketurl):
	import os
	files = os.listdir(annopath)
	fout= open('instance.json','w')
	for file in files:
		tree = xml_to_tree(os.path.join(annopath,file))
		filename = file.replace('xml','jpg')
		jsonline = xml_to_json(tree,filename,bucketurl)
		fout.write(jsonline +'\n')
	fout.close()
    
if __name__ =="__main__":
    annodir="./Annotations"
    bucketurl="forexample.com"
    xml2labelx(annodir,bucketurl)