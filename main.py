#import model
#import lock
import os
import Additional_function


yuanxian_mima=None  #全局密码

while True:
	print("1.密码解锁")
	print("2.人脸识别解锁")
	print("3.动态密码解锁")
	print("4.设置")
	xuanze=int(input())
	os.system("cls")
	while True:
		if xuanze==4:
			print("1.密码设置")
			print("返回")
			si=int(input())
			os.system("cls")
			if si==1:
				yuanxian_mima=mima_shezhi(yuanxian_mima)

		else:
			break











