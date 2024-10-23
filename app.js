async function searchRecipe() {
    const query = document.getElementById("searchQuery").value;
    const resultDiv = document.getElementById("result");

    // Limpa o resultado anterior
    resultDiv.innerHTML = '';

    if (query.trim() === '') {
        resultDiv.innerHTML = 'Por favor, insira o nome de um bolo.';
        return;
    }

    try {
        // Fazendo requisição para a API FastAPI que você criou
        const response = await fetch(`http://127.0.0.1:8000/recipes/?search_query=${query}`);
        const data = await response.json();

        if (response.ok) {
            // Exibindo a receita no div de resultado
            resultDiv.innerHTML = JSON.stringify(data.recipe, null, 2);
        } else {
            resultDiv.innerHTML = data.detail;
        }
    } catch (error) {
        resultDiv.innerHTML = 'Erro ao buscar receita. Verifique sua conexão ou tente novamente mais tarde.';
    }
}