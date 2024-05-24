import pandas as pd

# Dados dos produtos e vendedores
data = {
    "Produto": ["Arroz", "Feijão", "Macarrão", "Açúcar", "Café"],
    "Quantidade": [50, 30, 20, 25, 40],
    "Preço": [20.5, 15.0, 10.0, 5.0, 18.0],
    "Vendedor": ["Ana", "Carlos", "Beatriz", "Daniel", "Eduardo"],
}

df = pd.DataFrame(data)
