import pywifi
import time

#检测WiFi是否连接
def chakaiwuxianwangkashifoulianjie():
	wifi=pywifi.PyWiFi()
	ifaces=wifi.interfaces()[0]

	if ifaces.status() in [pywifi.const.IFACE_CONNECTED,pywifi.const.IFACE_CONNECTING]:
		return 1 #连接后返回值为1
	else:
		return 0 #连接后返回值为0


#扫描周围的WiFi
def saomiaowifi():
	wifi=pywifi.PyWiFi()
	iface=wifi.interfaces()[0]
	iface.scan()
	bsses=iface.scan_results()
	liebiao=[]
	for i in bsses:
		liebiao.append(i.ssid)
	shaichu=set(liebiao)
	return shaichu

#进行连接
def lianjie(wifi_mingzheng,wifi_mima):
	wffi=pywifi.PyWiFi()
	iface=wffi.interfaces()[0]
	iface.disconnect()
	time.sleep(3)
	profile_info= pywifi.profile
	profile_info.ssid=wifi_mingzheng
	profile_info.auth=pywifi.const.AUTH_ALG_OPEN
	profile_info.akm.append(pywifi.const.AKM_TYPE_WPA2PSK)
	profile_info.cipher=pywifi.const.CIPHER_TYPE_CCMP
	profile_info.key=wifi_mima
	iface.remove_all_network_profiles()
	tmp_profile=iface.add_network_profile(profile_info)
	iface.connect(tmp_profile)
	time.sleep(5)
	if iface.status()==pywifi.const.IFACE_CONNECTED:
		print("wifi:{}连接成功".format(wifi_mingzheng))
	else:
		print("wifi:{}连接失败".format(wifi_mingzheng))


def zong():
	zidian={}
	a=1
	for i in saomiaowifi():
		zidian[a]=i
		a+=1

	print("请输入WiFi对应的数字")
	for weizhi,wifi_name in zidian.items():
		print("{}-WiFi:{}".format(weizhi,wifi_name))

	#选择WiFi
	while True:
		try:
			shuzi=int(input("请输入:"))
			wifi_name_name=zidian[shuzi]
			break
		except:
			print("请重新输入")

	#输入密码
	while True:
		try:
			mima=input("请输入密码：")
			break
		except:
			print("错误，请重新输入")

	#wifi连接和检测
	lianjie(wifi_name_name,mima)

zong()