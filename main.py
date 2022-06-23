from flask import Flask, render_template, flash, request, redirect, url_for
import urllib.request
import os
from werkzeug.utils import secure_filename
from RedesNeuronales.Controller import Controller
import sys
sys.path.append("E:\\BilateralPneumoniaClassification\\RedesNeuronales\\Config")
sys.path.append("E:\\BilateralPneumoniaClassification\\RedesNeuronales")
sys.path.append("E:\\BilateralPneumoniaClassification\\RedesNeuronales\\Clasificacion")
sys.path.append("E:\\BilateralPneumoniaClassification\\RedesNeuronales\\Models")
sys.path.append("E:\\BilateralPneumoniaClassification\\RedesNeuronales\\Controller")
sys.path.append("E:\\BilateralPneumoniaClassification\\RedesNeuronales\\Utils")
sys.path.append("E:\\BilateralPneumoniaClassification\\RedesNeuronales\\temp")

app = Flask(__name__)

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])
UPLOAD_FOLDER = 'static/uploads/'

app.secret_key = "secret key"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
 
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def home():
    return render_template('home.html')



@app.route('/efficientnet')
def home2():
    return render_template('efficientnet.html')

@app.route('/efficientnet', methods=['POST'])
def upload_image():
    if 'uploadedfile' not in request.files:
        flash('No existe la imagen seleccionada')
        return redirect(request.url)
    file = request.files['uploadedfile']
    if file.filename == '':
        flash('No se ha seleccionado ninguna imagen')
        return redirect(request.url)
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        #print('upload_image filename: ' + filename)

        predCNN1,predCNN2,predEfficientnet,predDensenet, predResnet = Controller.visualizarClasificacion(app.config['UPLOAD_FOLDER'] + filename, False,False,True,False,False);
        pathPos, pathNeg = Controller.visualizarXAI(app.config['UPLOAD_FOLDER'] + filename, False,False,True,False,False)

        flash('Imagen correctamente procesada')
        return render_template('efficientnet.html', filename=filename, positivo=predEfficientnet[0][0]*100, negativo=predEfficientnet[0][1]*100, pathPositivo = pathPos, pathNegativo = pathNeg)
    else:
        flash('Extensiones permitidas - png, jpg, jpeg')
        return redirect(request.url)

@app.route('/efficientnet/display/<filename>')
def display_image(filename):
    #print('display_image filename: ' + filename)
    return redirect(url_for('static', filename='uploads/' + filename), code=301)

@app.route('/resnet')
def home3():
    return render_template('resnet.html')

@app.route('/resnet', methods=['POST'])
def upload_image2():
    if 'uploadedfile' not in request.files:
        flash('No existe la imagen seleccionada')
        return redirect(request.url)
    file = request.files['uploadedfile']
    if file.filename == '':
        flash('No se ha seleccionado ninguna imagen')
        return redirect(request.url)
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        #print('upload_image filename: ' + filename)

        predCNN1,predCNN2,predEfficientnet,predDensenet, predResnet = Controller.visualizarClasificacion(app.config['UPLOAD_FOLDER'] + filename, False,False,False,False,True);
        pathPos, pathNeg = Controller.visualizarXAI(app.config['UPLOAD_FOLDER'] + filename, False,False,False,False,True)

        flash('Imagen correctamente procesada')
        return render_template('resnet.html', filename=filename, positivo=predResnet[0][0]*100, negativo=predResnet[0][1]*100, pathPositivo = pathPos, pathNegativo = pathNeg)
    else:
        flash('Extensiones permitidas - png, jpg, jpeg')
        return redirect(request.url)

@app.route('/resnet/display/<filename>')
def display_image2(filename):
    #print('display_image filename: ' + filename)
    return redirect(url_for('static', filename='uploads/' + filename), code=301)


@app.route('/densenet')
def home4():
    return render_template('densenet.html')

@app.route('/densenet', methods=['POST'])
def upload_image3():
    if 'uploadedfile' not in request.files:
        flash('No existe la imagen seleccionada')
        return redirect(request.url)
    file = request.files['uploadedfile']
    if file.filename == '':
        flash('No se ha seleccionado ninguna imagen')
        return redirect(request.url)
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        #print('upload_image filename: ' + filename)

        predCNN1,predCNN2,predEfficientnet,predDensenet, predResnet = Controller.visualizarClasificacion(app.config['UPLOAD_FOLDER'] + filename, False,False,False,True,False);
        pathPos, pathNeg = Controller.visualizarXAI(app.config['UPLOAD_FOLDER'] + filename, False,False,False,True,False)

        flash('Imagen correctamente procesada')
        return render_template('densenet.html', filename=filename, positivo=predDensenet[0][0]*100, negativo=predDensenet[0][1]*100, pathPositivo = pathPos, pathNegativo = pathNeg)
    else:
        flash('Extensiones permitidas - png, jpg, jpeg')
        return redirect(request.url)

@app.route('/densenet/display/<filename>')
def display_image3(filename):
    #print('display_image filename: ' + filename)
    return redirect(url_for('static', filename='uploads/' + filename), code=301)

@app.route('/cnn1')
def home5():
    return render_template('cnn1.html')

@app.route('/cnn1', methods=['POST'])
def upload_image4():
    if 'uploadedfile' not in request.files:
        flash('No existe la imagen seleccionada')
        return redirect(request.url)
    file = request.files['uploadedfile']
    if file.filename == '':
        flash('No se ha seleccionado ninguna imagen')
        return redirect(request.url)
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        #print('upload_image filename: ' + filename)

        predCNN1,predCNN2,predEfficientnet,predDensenet, predResnet = Controller.visualizarClasificacion(app.config['UPLOAD_FOLDER'] + filename, True,False,False,False,False)
        pathPos, pathNeg = Controller.visualizarXAI(app.config['UPLOAD_FOLDER'] + filename, True,False,False,False,False)

        flash('Imagen correctamente procesada')
        return render_template('cnn1.html', filename=filename, positivo=predCNN1[0][0]*100, negativo=predCNN1[0][1]*100, pathPositivo = pathPos, pathNegativo = pathNeg)
    else:
        flash('Extensiones permitidas - png, jpg, jpeg')
        return redirect(request.url)

@app.route('/cnn1/display/<filename>')
def display_image4(filename):
    #print('display_image filename: ' + filename)
    return redirect(url_for('static', filename='uploads/' + filename), code=301)


@app.route('/cnn2')
def home6():
    return render_template('cnn2.html')

@app.route('/cnn2', methods=['POST'])
def upload_image5():
    if 'uploadedfile' not in request.files:
        flash('No existe la imagen seleccionada')
        return redirect(request.url)
    file = request.files['uploadedfile']
    if file.filename == '':
        flash('No se ha seleccionado ninguna imagen')
        return redirect(request.url)
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        #print('upload_image filename: ' + filename)

        predCNN1,predCNN2,predEfficientnet,predDensenet, predResnet = Controller.visualizarClasificacion(app.config['UPLOAD_FOLDER'] + filename, False,True,False,False,False);
        pathPos, pathNeg = Controller.visualizarXAI(app.config['UPLOAD_FOLDER'] + filename, False,True,False,False,False)

        flash('Imagen correctamente procesada')
        return render_template('cnn2.html', filename=filename, positivo=predCNN2[0][0]*100, negativo=predCNN2[0][1]*100, pathPositivo = pathPos, pathNegativo = pathNeg)
    else:
        flash('Extensiones permitidas - png, jpg, jpeg')
        return redirect(request.url)

@app.route('/cnn2/display/<filename>')
def display_image5(filename):
    #print('display_image filename: ' + filename)
    return redirect(url_for('static', filename='uploads/' + filename), code=301)

@app.route('/metricas')
def home7():
    return render_template('metricas.html')

@app.route('/cnn1Info')
def home8():
    return render_template('cnn1Info.html')

@app.route('/cnn2Info')
def home9():
    return render_template('cnn2Info.html')

@app.route('/efficientnetInfo')
def home10():
    return render_template('efficientnetInfo.html')

@app.route('/resnetInfo')
def home11():
    return render_template('resnetInfo.html')

@app.route('/densenetInfo')
def home12():
    return render_template('densenetInfo.html')

if __name__ == '__main__':
    app.run()
