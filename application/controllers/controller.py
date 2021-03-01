from application.start import app
from bottle import route, redirect, template, static_file
from application.models.database import Database
import json

@app.get("/<filename>")
def serve_static_files(filename):
	#print(filename)
	if filename[-4:] == ".css":
		return static_file(filename,root="application/static/style")
	elif filename[-4:] == ".png":
		return static_file(filename,root="application/static/image")
	elif filename[-3:] == ".js":
		return static_file(filename,root="application/static/script")

@app.route("/<id>",method="POST")
def del_id(id):
	database = Database()
	database.connect()
	res = database.get_status_conn()
	if res == True:
		condiction = "WHERE id_pessoa="+str(id)
		table="pessoas"
		database.delete(table,condiction)
		if database.get_state_delete() == True:
			print("Excluído com sucesso.")
		else:
			print("Erro na exclusão.")
	database.desconnect()
	return json.dumps(307)

@app.route("/<nome>/<dado>",method="POST")
def add_info(nome,dado):
	database = Database()
	database.connect()
	res = database.get_status_conn()
	if res == True:
		table = "pessoas"
		field = ['nome','data_admissao']
		data = [nome,dado]
		database.insert(table,field,data)
		if database.get_state_insert() == True:
			print("Adicionado com sucesso.")
		else:
			print("Erro na Adição.")
	database.desconnect()
	return json.dumps(307)

@app.route("/")
def home():
	user_id = []
	fname = []
	inc_date = []
	database = Database()
	database.connect()
	res = database.get_status_conn()
	if res == True:
		fields = ['*']
		table = "pessoas"
		database.select(fields,table)
		if database.get_state_select() == True:
			results = database.get_result()
			#print(results)
			siz = len(results)
			for row in results:
				dt = str(row[5]).split("-")
				if dt[0] != 'None':
					#print(dt)
					d = str(dt[2]) + "/" + str(dt[1]) + "/" + str(dt[0])
					inc_date.append(d)
					user_id.append(row[0])
					fnam = str(row[1]).split(" ")
					fname.append(fnam[0])
	database.desconnect()
	return template('home',fname=fname,inc_date=inc_date,user_id=user_id)