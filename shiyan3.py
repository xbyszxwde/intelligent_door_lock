import time
xian_shijian_1 = time.strftime("%H:%M:%S", time.localtime())
print(xian_shijian_1)
xiaoshi=xian_shijian_1[:2]
fenzhong=xian_shijian_1[3:5]
miao=xian_shijian_1[6:]
jisuan=((((24-int(xiaoshi))*60)-int(fenzhong))*60)-int(miao)


