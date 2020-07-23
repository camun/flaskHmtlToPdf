from flask import Flask, render_template
import pdfkit
import os

#install wkhtmltopdf 

app = Flask(__name__)
app.config['PDF_FOLDER'] = 'static/pdf/'
app.config['TEMPLATE_FOLDER'] = 'templates/'


dataAlert = [
	["Alerta","amg_puentenegro",97.4, 178.0, 0],
	["Alerta","amg_puentenegro",97.4, 178.0, 0]
]

dataDeficit = [
	["Deficit","amg_puentenegro",97.4, 178.0, 0],
	["Deficit","amg_puentenegro",97.4, 178.0, 0]
]

@app.route('/')
def index():
	result = os.system("phantomjs generateImage.js")
	print(result)
	return render_template('index.html',dataAlert=dataAlert,dataDeficit=dataDeficit)


@app.route('/leaft')
def leaft():
	return render_template('leaft.html')



@app.route('/convert')
def konversi():
	#result = os.system("phantomjs generateImage.js")
	#print(result)
	htmlfile = app.config['TEMPLATE_FOLDER'] + 'index.html'
	pdffile = app.config['PDF_FOLDER'] + 'demo.pdf'
	

	pdfkit.from_file(htmlfile, pdffile)
	return '''Click here to open the
	<a href="http://localhost:5000/static/pdf/demo.pdf">pdf</a>.'''


if __name__ == '__main__':
	app.run(debug=True)