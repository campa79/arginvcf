from django.http import HttpResponse
import datetime
from django.template import Template, Context
from django.template import loader
from django.template.loader import get_template
from django.shortcuts import render

class Persona(object):
	def __init__(self, nombre, apellido):
		self.nombre=nombre
		self.apellido=apellido

#Creo el link al INDEX con vista y CON LOADER
def index(request):
	#doc_externo=loader.get_template('index.html')
	#doc_externo=get_template('index.html') #Directo importando el método get_template
	#documento=doc_externo.render()
	return render(request, "index.html")

#Creo el link al INDEX con LOADER
def index3(request):
	return render(request, "index3.html")		

#Creo el link al INDEX2 con vista y SIN LOADER
def index2(request):
	doc_externo=open("C:/PP3Django/arginv/arginv/plantillas/index2.html")	
	plt=Template(doc_externo.read())
	doc_externo.close()
	ctx=Context()
	documento=plt.render(ctx)
	return HttpResponse(documento)	

#Creo el link al ERJ con vista
def erj(request):
	doc_externo=open("C:/PP3Django/arginv/arginv/plantillas/erj.html")	
	plt=Template(doc_externo.read())
	doc_externo.close()
	ctx=Context()
	documento=plt.render(ctx)
	return HttpResponse(documento)	

#Creo primera vista #Creo primera plantilla
def saludo(request):
	#return HttpResponse("Hola Proyecto Argentina Inversores!")
	p1=Persona("Ing. Juan", "Diaz")

	#nombre="Alberto"
	#apellido="Campagna"
	ahora=datetime.datetime.now()

	temasDelCurso=["Plantillas","Modelos","Formularios","Vistas","Despliegue App"]

	doc_externo=loader.get_template('miplantilla.html')
	#doc_externo=open("C:/PP3Django/arginv/arginv/plantillas/miplantilla.html")
	#plt=Template(doc_externo.read()) #Lo lee
	#doc_externo.close() #lo cierra
	#ctx=Context({"nombre_persona":p1.nombre,"apellido_persona":p1.apellido,"momento_actual":ahora,
		#"temas":temasDelCurso})

	documento=doc_externo.render({"nombre_persona":p1.nombre,"apellido_persona":p1.apellido,"momento_actual":ahora,
		"temas":temasDelCurso})
	#documento=plt.render(ctx)
	return HttpResponse(documento)	

def despedida(request):
	return HttpResponse("Hasta Luego!")

def damefecha(request):
	fecha_actual=datetime.datetime.now()

	documento="""
	<html>
		<body>
			<h1>Fecha y Hora: %s</h1>	
		</body>
	</html>
	""" % fecha_actual

	return HttpResponse(documento)

def calculaEdad(request, edad, anio): #Por parametro en la URL paso edad actual y año final
	periodo=anio-2021
	edadFutura=edad+periodo
	documento="""
	<html><body>
		<h2>En el año %s tendrás %s años.</h2>
	</body></html>""" %(anio, edadFutura)

	return HttpResponse(documento)

