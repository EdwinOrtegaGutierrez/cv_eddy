from flask import Flask, render_template as html, url_for
from json import load, loads
from requests import get

app = Flask(__name__, template_folder="templates")

app.config.update(
    TESTING=True,
    SECRET_KEY='192b9bdd22ab9ed4d12e236c78afcb9a393ec15f71bbf5dc987d54727823bcbf'
)

@app.route('/')
def index():
    with open('static/json/index.json') as f:
        data = load(f)
    presentation = data['presentation']
    information = {
        "work experience": data['WE'][0],
        "general objective": data['GO'][0],
        "strengths and weaknesses": data['SW'][0],
        "motivations": data['motivations'][0]
    }
    
    extra = data['extra']
    hobbies = data['hobbies']
    
    return html('home/index.html', presentation=presentation, information=information, extra=extra, hobbies=hobbies)

@app.route('/about-me')
def aboutMe():
    with open('static/json/aboutMe.json') as f:
        data = load(f)
    about_me = data['aboutMe'][0]
    education = data['education']
    return html('home/aboutMe.html', about_me=about_me, education=education)

@app.route('/work')
def work():    
    # La URL de la API para obtener la información de los repositorios de un usuario
    url = 'https://api.github.com/users/EdwinOrtegaGutierrez/repos'

    # Crea una solicitud GET a la API con el token de acceso en la cabecera
    response = get(url, headers={'Authorization': 'token your_acces_token'})

    # Obtiene la lista de repositorios de la respuesta JSON utilizando la biblioteca "json"
    repos = loads(response.content)

    # Crea el diccionario de repositorios utilizando una comprensión de diccionario
    repositories = {repo['name']: {'description': repo['description'], 'url': repo['html_url']} for repo in repos}

	# Renderiza la plantilla HTML y pasa el diccionario "repositories" como argumento
    return html('home/work.html', repositories=repositories)

@app.route('/contacts')
def contacts():
    return html('home/contacts.html')


@app.route('/skills')
def skills():
    with open('static/json/skills.json') as f:
        data = load(f)
    skills = data["skills"]
    db = data["db"]
    pl = data["pl"]
    frameworks = data["frameworks"]
    lenguages = data["lenguages"]
    return html('home/skills.html', skills=skills, db=db, pl=pl, frameworks=frameworks, lenguages=lenguages)

if __name__ == "__main__":
    #app.secret_key = 'super secret key' #NECESARIO PARA MANDAR MENSAJES PRIVADOS
    app.run(host = '0.0.0.0', port=80, debug=True)