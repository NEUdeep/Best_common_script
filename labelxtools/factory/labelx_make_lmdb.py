"""
the file can make the format dataset of lmdb by the given json file.
"""

class jsontoLmdb(object):
    
    def __init__(self,srcJson,outPath,isBucket):
        '''
        the outPath is the path of lmdb excepted.
        '''
        env = lmdb.open(outPath, map_size=1099511627776)
        with open(srcJson,'r') as fjson:
            lines = fjson.readlines()
            write_lmdb(env,lines,isBucket)

        nSamples = len(lines)
        txn = env.begin(write=True,buffers=True)  
        if sys.version_info < (3, 0):
            txn.put(key = 'num-samples', value =str(nSamples)) 
        else:
            txn.put(key = 'num-samples'.encode(), value =str(nSamples).encode()) 
        txn.commit()

        
        
    def write_lmdb(env,lines,isBucket):
        cache = {}
        nSamples = len(lines)
        for indx,jsonline in enumerate(lines):
            dic = json.load(jsonline)
            image_path=dic['url']
            if(isBucket):
                resp = urllib.request.urlopen(quote(image_path,safe='/:'))
                image = np.asarray(bytearray(resp.read()), dtype="uint8")
            else:
                f = open(image_path,'rb')
                image = np.asarray(bytearray(f.read()), dtype="uint8")#转换成uint8数据
                f.close()
            if image is None:
                print("Imags is null")
                return -1
            
            imageKey = 'image-%09d' % idx
            labelKey = 'label-%09d' % idx
            
            if sys.version_info < (3, 0):
                cache[imageKey] = image.tostring()
                cache[labelKey] = jsonline
            else:
                #print(image.tostring().type)
                cache[imageKey.encode()] = image.tobytes()
                cache[labelKey.encode()] = jsonline.encode()
            
            if idx % 100 == 0 and idx !=0:
                writeCache(env, cache)
                cache = {}
                print('Written %d / %d' % (idx, nSamples))
                
        writeCache(env, cache)
        return 
    
    def writeCache(env, cache):
        with env.begin(write=True) as txn:
            if sys.version_info < (3, 0):
                for k, v in cache.iteritems():
                    txn.put(k, v)
            else:
                for k, v in cache.items(): 
                    txn.put(k, v)
            
        