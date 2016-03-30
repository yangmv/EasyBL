#!/usr/bin/env python
#encoding: utf-8
import MySQLdb
def db(host,username):
    conn = MySQLdb.connect(host='10.10.50.30',user='root',passwd='123456',db='yangmv')
    cur = conn.cursor()
    sql = "select * from user where hostname=%s and user=%s"
    args = (host,username)
    recount = cur.execute(sql,args)
    data = cur.fetchall()
    cur.close()
    conn.close()
    if data:
        return data[0][3]
    else:
        return False


def dbgroup():
    conn = MySQLdb.connect(host='10.10.50.30',user='root',passwd='123456',db='yangmv')
    cur = conn.cursor(cursorclass = MySQLdb.cursors.DictCursor)
    sql = "select groups from dev"
    recount = cur.execute(sql)
    data = cur.fetchall()
    cur.close()
    conn.close()
    if data:
        return data
    else:
        return False

def dblist(s_group):
    conn = MySQLdb.connect(host='10.10.50.30',user='root',passwd='123456',db='yangmv')
    cur = conn.cursor(cursorclass = MySQLdb.cursors.DictCursor)
    sql = "select hostname from dev where groups='%s'"%s_group
    recount = cur.execute(sql)
    data = cur.fetchall()
    cur.close()
    conn.close()
    if data:
        return data
    else:
        return False

def dbpwd(s_user):
    conn = MySQLdb.connect(host='10.10.50.30',user='root',passwd='123456',db='yangmv')
    #cur = conn.cursor(cursorclass = MySQLdb.cursors.DictCursor)
    cur = conn.cursor()
    sql = "select pwd from dev where hostname='%s'"%s_user
    recount = cur.execute(sql)
    data = cur.fetchall()
    cur.close()
    conn.close()
    if data:
        return data[0][0]
    else:
        return False


def list(host,username):
    dic = {
        'root':{'10.10.50.31':'123456',
                'www.website1.com':'URE9ZjjbT57qfms',
				'www.website2.com':'inau3Eej6the',
                'www.website3.com':'I5C%8P[OTX,X',
                'www.website4.com':'MThM2E5Y',
                'www.website5.com':'2NFT5NhT',
		},
        'yangmv':{'10.10.50.31':'456789',
                'www.fb1.com':'123456'},
        'bob':[],
    }
    data = dic[username][host]
    if data:
        return data
    else:
        return False
