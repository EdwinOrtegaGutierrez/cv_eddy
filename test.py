from requests import get
from json import loads
# La URL de la API para obtener la información de los repositorios de un usuario
url = 'https://api.github.com/users/EdwinOrtegaGutierrez/repos'

# Crea una solicitud GET a la API con el token de acceso en la cabecera
response = get(url, headers={'Authorization': 'token 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'})

# Obtiene la lista de repositorios de la respuesta JSON utilizando la biblioteca "json"
repos = loads(response.content)

# Crea el diccionario de repositorios utilizando una comprensión de diccionario
repositories = {repo['name']: {'description': repo['description'], 'url': repo['html_url']} for repo in repos}

print(repositories)