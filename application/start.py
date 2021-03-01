from bottle import Bottle, TEMPLATE_PATH

app = Bottle()
TEMPLATE_PATH.insert(0,"application/views/")

from application.controllers import controller

