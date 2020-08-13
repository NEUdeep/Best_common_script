import torch
import MFNET_3D

model = MFNET_3D(num_classes=101)
params = sum(p.numel() for p in model.parameters())
print(params)
# outputs a same result 7996368 as shown in the paper: 8.0 M





#使用下面模块也可以
###   模型定义
# -------------
class MyModel(nn.Module):
    def __init__(self, feat_dim):   # input the dim of output fea-map of Resnet:
        super(MyModel, self).__init__()
        ...
    def forward(self, input):   # input is 2048!
        ...
        return x
 
net = MyModel()
 
######################################
params = list(net.parameters())
k = 0
for i in params:
    l = 1
    print("该层的结构：" + str(list(i.size())))
    for j in i.size():
        l *= j
    print("该层参数和：" + str(l))
    k = k + l
print("总参数数量和：" + str(k))
######################################