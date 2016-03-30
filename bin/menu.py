#!/usr/bin/env python
#encoding: utf-8
import os,sys
import MySQLdb
Base_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(Base_DIR)
from modules import mydb
user_list = ['root','yangmv','bob']


msg = """
\033[31;1mXXserver管理平台\033[0m
"""
print msg
group_list = []
group_dic = mydb.dbgroup()
for i in group_dic:
    group_list.append(i.values()[0])
group_list = list(set(group_list))  #去重复项

while True:
    print '###################################游戏业务####################################'
    for index, groups in enumerate(group_list, 1):
        print index, groups
    s_group = raw_input('\033[31;1m请选择游戏业务:\033[0m')
    if len(s_group) == 0:continue
    if s_group == 'quit':
	print 'GoodBye!'
       	break
    try:
	s_group = int(s_group)
        host_group = group_list[s_group-1]  #选择对应的主机组
        host_dic = mydb.dblist(host_group)
        host_list = []   #主机中中的主机列表
        for i in host_dic:
            host_list.append(i.values()[0])
        while True:
            print '#################################机器列表################################'
            for index,hostname in enumerate(host_list,1):
                print '%s:    %s'%(index,hostname)
            show = raw_input('\033[31;1m请选择要登陆的机器:（返回上一层:quit) \033[0m') #选择要连接的主机
            if show == 'quit':
                print 'quit this host groups!'
                break
            if len(show) == 0:continue
            show = int(show)
            try:
                hostip = '10.10.50.30'
                username = host_list[show-1]  #获取选择的主机hostname
                pwd = mydb.dbpwd(username)
                print '\033[32;1mGoing to connect: %s@%s \033[0m'%(username,hostip)
		os.chdir("/home/dev/baolei/bin")
		os.system("python demo.py %s %s %s"%(hostip,username,pwd))
            except IndexError,e:
                print 'not found this number!,please again input'
            except Exception,e:
                print 'Error!!!',e
    except Exception,e:
        print 'Error!!!,please again input:',e
