#Made by @hui2007
#Twitter @hui2007a
#QQ:1404498096
#Copyright
import time
import os
import json
def switch_to_pc():
	sav = open("undertale.sav","r")
	sav_cont = sav.read()
	dict_sav = json.loads(sav_cont)
	file9_cont = dict_sav['file9']
	file9 = open('file9','w')
	file9.write(file9_cont)
	file9.close()
	file0_cont = dict_sav['file0']
	file0 = open('file0','w')
	file0.write(file0_cont)
	file0.close()
	ini_cont = dict_sav['undertale.ini']
	ini = open('undertale.ini','w')
	ini.write(ini_cont)
	ini.close()
	if 'file8' in dict_sav:
		file8 = open('file8','w')
		file8_cont = dict_sav['file8']
		file8.write(file8_cont)
		file8.close()
	if 'system_information_962' in dict_sav:
		si962 = open('system_information_962','w')
		si962_cont = dict_sav['system_information_962']
		si962.write(si962_cont)
		si962.close()
	if 'system_information_963' in dict_sav:
		si963 = open('system_information_963','w')
		si963_cont = dict_sav['system_information_963']
		si963.write(si963_cont)
		si963.close()
	sav.close()
def pc_to_switch():
	dict_sav = {"default":""}
	dict_sav['default'] = ''
	file9 = open('file9','r')
	file9_cont = file9.read()
	dict_sav['file9'] = file9_cont
	file9.close()
	ini = open('undertale.ini','r')
	ini_cont = ini.read()
	dict_sav['undertale.ini'] = ini_cont
	ini.close()
	file0 = open('file0','r')
	file0_cont = file0.read()
	dict_sav['file0'] = file0_cont
	file0.close()
	if os.path.exists('file8'):
		file8 = open('file8','r')
		file8_cont = file8.read()
		dict_sav['file8'] = file8_cont
	if os.path.exists('system_information_962'):
		si962 = open('system_information_962','r')
		si962_cont = si962.read()
		dict_sav['system_information_962'] = si962_cont
	if os.path.exists('system_information_963'):
		si963 = open('system_information_963','r')
		si963_cont = si963.read()
		dict_sav['system_information_963'] = si963_cont
	sav_cont = json.dumps(dict_sav)
	sav = open('undertale.sav','w')
	sav.write(sav_cont)
	sav.close()
def ch():
	print('欢迎来到UNDERTALE存档转换器！')
	print('本工具由hui2007制作')
	print('有任何疑问请联系QQ:1404498096 备注:UT存档转换器')
	print('或在Github提出Issue!')
	print('')
	print('转换模式:')
	print('1.PC转Switch')
	print('2.Switch转PC')
	choose = input('>')
	if choose == "1":
		print('请确定您已将file0,file9,undertale.ini放至当前目录下')
		print('如果存在file8/system_information_962/963也请一并放置')
		print('转换中...')
		time.sleep(3)
		pc_to_switch()
		print('转换完成!')
	elif choose == '2':
		print('请确定您已将undertale.sav放至当前目录下')
		print('转换中...')
		time.sleep(3)
		switch_to_pc()
		print('转换完成!')
def en():
	print('Welcome to UNDERTALE Save Converter！')
	print('This tool is made by Hui2007')
	print('Any question please contact Twitter @hui2007a or create an Issue on Github!')
	print('')
	print('Convert mode:')
	print('1.PC to Switch')
	print('2.Switch to PC')
	choose = input('>')
	if choose == "1":
		print('Please make sure you have put \'file0\',\'file9\' and \'undertale.ini\' to current directory.')
		print('If \'file8\' ,\'system_information_962\' or \'system_information_963\' exists, please place it together')
		print('Converting...')
		time.sleep(3)
		pc_to_switch()
		print('Conversion completed!')
	elif choose == '2':
		print('Please make sure you have put \'undertale.sav\' to current directory.')
		print('Converting...')
		time.sleep(3)
		switch_to_pc()
		print('Conversion completed!')
print('Language/语言:')
print('1.English')
print('2.简体中文')
choose = input('>')
if choose == "1":
	en()
elif choose == "2":
	ch()

