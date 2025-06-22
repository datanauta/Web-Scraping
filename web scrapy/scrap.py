import requests
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0"
}

url = "https://www.marca.com"

try:
    response = requests.get(url, headers=headers)
    print("Código de respuesta:", response.status_code)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        word = 'gol'
        if word in soup.get_text().lower():
            print(f'✅ La palabra "{word}" aparece en la portada de Marca.')
        else:
            print(f'❌ La palabra "{word}" NO aparece en la portada de Marca.')
    else:
        print(f'🚫 No se pudo acceder a la página. Código: {response.status_code}')
except Exception as e:
    print(f'💥 Error durante la petición: {e}')
