import os
import time
import random

#密码设置
def mima_shezhi(yuanxian=None):
	if yuanxian!=None:
		while True:
			yuanxian_mima=input("请输入原先的密码：")
			os.system("cls")
			if yuanxian==yuanxian_mima:
				xin_mima=input("请重新输入新的密码：")
				os.system("cls")
				while True:
					print("输入数字1可以返回上一步")
					xin_mima_1=input("请第二次输入新的密码：")
					if xin_mima_1==str(1):
						break
					if xin_mima_1==xin_mima:
						print("修改密码成功")
						os.system("cls")
						return xin_mima
			else:
				print("原先的密码错误，请重新输入")
				continue
	else:
		while True:
			xin_mima=input("请输入新密码：")
			os.system("cls")
			while True:
				print("输入数字1可以返回上一步")
				xin_mima_1=input("请输入第二遍密码：")
				print("*"*50)
				print("设置成功")
				time.sleep(2)
				os.system("cls")
				if xin_mima_1==str(1):
					break
				elif xin_mima==xin_mima_1:
					return xin_mima_1
				else:
					print("第二次和第一次不符合")
					print("请重新输入")
					os.system("cls")

#定时模块
def timing():
	xian_shijian = time.strftime("%Y-%m-%d", time.localtime())
	xian_shijian_1=time.strftime("%H:%M:%S", time.localtime())
	while True:
		print("现在的时间为：{} {}",xian_shijian,xian_shijian_1)
		print("1.修改年月")
		print("2.修改时分")
		print("3.修改年月时分")
		print("4.返回")
		xuanze_1=input()
		os.system("cls")
		if xuanze_1==1:
			print("现在的年月为：{}",xian_shijian)


		elif xuanze_1==2:
			pass
		elif xuanze_1==3:
			pass
		elif xuanze_1==4:
			return
		else:
			print("输入错误，请输入对应的数字")
			time.sleep(1)
			os.system("cls")




lujina=r'./lock_data'  #开锁记录文件路径
def rizhishengcheng(shuzhi1='kai',shuzhi2='guanbi',moshi=False):
	if shuzhi1=='kai':
		pass
	else:
		shijian = time.strftime("%Y-%m-%d", time.localtime())
		wenjian=os.listdir(lujina)
		for i in wenjian:
			if i==shijian:
				if moshi==False:
					continue
				else:
					wenjian_txt=open('{}\\{}.txt'.format(lujina,shijian),'a')
					wenjian_txt.write("时间：{}-模式：{}-状态：开锁\n".format(time.strftime("%H:%M:%S", time.localtime()),moshi))
					wenjian_txt.close()
			else:
				wenjian_txt = open('{}\\{}.txt'.format(lujina, shijian), 'a')
				wenjian_txt.write("时间：{}-模式：{}-状态：开锁\n".format(time.strftime("%H:%M:%S", time.localtime()), moshi))
				wenjian_txt.close()

	if shuzhi2=='guanbi':
		pass
	else:
		shijian = time.strftime("%Y-%m-%d", time.localtime())
		wenjian = os.listdir(lujina)
		for i in wenjian:
			if i == shijian:
				if moshi == False:
					continue
				else:
					wenjian_txt = open('{}\\{}.txt'.format(lujina, shijian), 'a')
					wenjian_txt.write("时间：{}-模式：{}-状态：关锁\n".format(time.strftime("%H:%M:%S", time.localtime()), moshi))
					wenjian_txt.close()
			else:
				wenjian_txt = open('{}\\{}.txt'.format(lujina, shijian), 'a')
				wenjian_txt.write("时间：{}-模式：{}-状态：关锁\n".format(time.strftime("%H:%M:%S", time.localtime()), moshi))
				wenjian_txt.close()

#动态密码
def mimashengcheng():
	a=['`', '~', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+', '-', '=', 'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', '[', ']', '{', '}', '|', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', ';', ':', '"', 'z', 'x', 'c', 'v', 'b', 'n', 'm', ',', '.', '/', '<', '>', '?']
	b=[]
	for i in range(8):
		b.append(random.choice(a))

	zidian={}
	for ii in b:
		zidian[ii]=random.randint(0,9)

	mima=''
	yuanmima=''
	for mimma,iii in zidian.items():
		mima+=str(iii)
		yuanmima+=mimma
	return mima
