# coding=utf-8
# python2.7

dict = {'Google': 'www.google.com', 'Runoob': 'www.runoob.com', 'taobao': 'www.taobao.com'}

print("字典值 : %s" % dict.items())
a=dict.items() # or: a = zip(dict.iterkeys(),dict.itervalues())
print type(a)
for i in range(len(a)):
    k = a[i]
    j=i
    if k[0] == 'Google':
        continue
    elif k[0] == 'taobao':
        j=j+1
        s = a[j]
        if s[0] =='Runoob' and s[1] == 'www.runoob.com':
            box = k[1]
            print box