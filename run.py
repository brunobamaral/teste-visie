from application.start import app

if __name__ == "__main__":
	host = "localhost"
	port = 8080
	app.run(host=host,port=port,debug=True,reloader=True)