#coding:utf-8
import MySQLdb

class MySQLEngine(object):

    def __init__(self):
        self.conn=None
        self.cur=None

        '''
        打开数据库
        '''
    def open(self,dbHost,dbPort,dbUser,dbPasswd,dbName):
        self.conn = MySQLdb.connect(host=dbHost,port=dbPort,user=dbUser,passwd=dbPasswd,db=dbName)
        self.cur = self.conn.cursor()   #拿到游标，sql语句需要游标执行
        '''
           查询一条
        '''
    def searchOne(self,sql):
        affRows = self.cur.execute(sql) #通过游标执行查询操作,返回影响行数
        res = self.cur.fetchone()
        return res,affRows
        '''
           查询指定条数
        '''
    def searchMany(self,sql,size):
        affRows = self.cur.execute(sql) #通过游标执行查询操作,返回影响行数
        res = self.cur.fetchmany(size)  #每条结果都是一个tuple,所有tuple最终组成一个tuple
        return res,affRows
        '''
           查询所有
        '''
    def searchAll(self,sql):
        affRows = self.cur.execute(sql) #通过游标执行查询操作,返回影响行数
        res = self.cur.fetchall()
        return res,affRows
        '''
           该改记录，包括：增、删、改
        '''
    def modify(self,sql,params):
        affRows = self.cur.execute(sql,params)
        self.conn.commit()  #不commit不会修改到数据库中
        return affRows
        '''
          关闭数据库
        '''
    def close(self):
        self.cur.close()
        self.conn.close()
