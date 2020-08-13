# 作用

该文件主要用于labelx文件向voc和lmdb文件的格式转化
labelx的文件格式如下：

    l_json = {"url": “”,
			"type":"image",
			"label":[{"name": "general", "type": "detection", "version": "1",
			"data":[]}]}

# 姿势

      from factory import jsontoVoc，

      jsontoVoc(srcJson,exceptPath,imageSplitrate,isBucket)
    
* srcJson:标识labelx源文件路径
* exceptPath:表示输出的VOC格式路径
* imageSplitrate:表示0-1的浮点数，表示图片随机初始化为训练集的概率,默认为None
* isBucket:表示图片是否来源于远程地址
    
    
    
      from factory import
      
      jsontoLmdb(srcJson,outPath,isBucket)
        
* srcJson:标识labelx源文件路径
* outPath:表示输出lmdb格式路径
* isBucket:表示图片是否来源于远程地址
    
    
    
