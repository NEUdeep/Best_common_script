# 描述（该工具不定时持续更新）
factory暂时提供两种json文件向voc和lmdb两种数据集格式的转换：

* json_make_lmdb.py ：提供lmdb数据格式的转换
* json_make_voc.py  ：提供voc数据格式的转换

fileAPI提供多种labelx用到的函数成体，可以直接调用，具体可以参考内含文件说明。

# demo

* readlmdb_demo.py：

    是dataloader读取lmdb文件的demo，实现了具体lmdb文件数据的读取，可以直接整改到pytorch程序框架下。

* xml2labelx_demo.py：

    是利用fileAPI，通过图片描述的xml文件生成为labelx可用的json文件。