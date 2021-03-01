import pymysql.cursors

class Database:

	conn = None
	status_conn = None
	host = "db4free.net"
	user = "visie_user"
	password = "visie_pass"
	dbname = "visie_db"
	state_insert = None
	state_delete = None
	state_select = None
	result = None

	def __init__(self):
		if self.conn == None:
			self.connect()

	def connect(self):
		try:
			self.conn = pymysql.connect(host=self.host,user=self.user,password=self.password,database=self.dbname)
			self.status_conn = True
		except pymysql.Error as error:
			self.status = False
			print("Erro: ",error)

	def get_status_conn(self):
		return self.status_conn

	def desconnect(self):
		if self.conn != None:
			self.conn.close()

	def insert(self,table,fields,datas):
		cursor = self.conn.cursor()
		sql = "INSERT INTO "+table+" ("

		for x in range(0,len(fields)):
			if x == (len(fields) - 1):
				sql += fields[x]+") "
			else:
				sql += fields[x]+", "
		sql += "VALUES ("
		for x in range(0,len(datas)):
			if x == (len(datas) - 1):
				sql += "'"+datas[x]+"') "
			else:
				sql += "'"+datas[x]+"', "
		print(sql)
		try:
			cursor.execute(sql)
			self.conn.commit()
			self.state_insert = True
		except :
			self.state_insert = False
			self.conn.rollback()


	def get_state_insert(self):
		return self.state_insert

	def select(self,fields,table,condic=None):
		cursor = self.conn.cursor()
		sql = "SELECT "
		for x in range(0,len(fields)):
			if x == (len(fields) - 1):
				sql += fields[x]+" "
			else:
				sql += fields[x]+", "
		sql += "FROM "+table+" "
		if condic != None:
			sql += condic
		try:
			cursor.execute(sql)
			self.result = cursor.fetchall()
			self.state_select = True
		except:
			self.state_select = True

	def get_state_select(self):
		return self.state_select

	def get_result(self):
		return self.result

	def delete(self,table,condic):
		cursor = self.conn.cursor()
		sql = "DELETE FROM " + table + " "
		sql += condic
		print(sql)
		try:
			cursor.execute(sql)
			self.conn.commit()
			self.state_delete = True
		except:
			self.state_delete = False

	def get_state_delete(self):
		return self.state_delete
"""
#connect
db = Database()
db.connect()
res = db.get_status_conn()
if res == True:
	print("Conn succ")
else:
	print("Conn err")

#insert
field = ['nome','sobrenome']
data = ['Carlos','Almeida',None]
db.insert('pessoa',field,data)
res = db.get_state_insert()
if res == True:
	print("Insert")
else:
	print("No Insert")
#select all
field = ['*']
#condiction = "ORDER BY ASC"
db.select(field,'pessoas')
res = db.get_state_select()
if res == True:
	print(db.get_result())
	d = db.get_result()
	for row in d:
		print(row[1])
		print(row[5])
else:
	print("No Select")

#delete
condiction = "WHERE id=2"
db.delete('pessoa',condiction)
res = db.get_state_delete()
if res == True:
	print("Del Succ")
else:
	print("No Del")
"""