from fastapi import FastAPI, Query, HTTPException
import requests
from urllib.parse import unquote

app = FastAPI()

# Função para chamar a API do Gemini
def get_gemini_recipe(query: str):
    url = "https://api.gemini.com/v1/recipes"  # URL fictícia da API do Gemini (ajuste conforme a documentação)
    headers = {
        "Authorization": "Bearer AIzaSyCSZNStF-i9lys4sVX55vgX0q3gG2CHYBo"  # Coloque sua chave da API do Gemini aqui
    }
    params = {"search": query}  # Parâmetro de pesquisa enviado à API do Gemini
    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        return response.json()  # Retorna os dados da API se a requisição for bem-sucedida
    else:
        raise HTTPException(status_code=response.status_code, detail="Erro ao buscar receita na API do Gemini")

@app.get("/recipes/")
async def get_recipe(search_query: str = Query(..., description="Digite o nome da receita")):
    # Decodifica a URL (para lidar com espaços e outros caracteres codificados)
    search_query = unquote(search_query)

    # Faz a busca pela receita diretamente na API do Gemini
    recipe_data = get_gemini_recipe(search_query)

    # Verifica se a resposta contém a receita
    if recipe_data and 'recipe' in recipe_data:
        return {"recipe": recipe_data['recipe']}
    else:
        # Caso a receita não seja encontrada
        raise HTTPException(status_code=404, detail="Receita não encontrada na API do Gemini")
