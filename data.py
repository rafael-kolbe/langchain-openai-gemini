from pathlib import Path
import pandas as pd

df = None
local_file_path = Path(f"parquets/712313b8-d370-41f5-a75f-b256d4080b2f.parquet")

if local_file_path.is_file():
    try:
        df = pd.read_parquet(path=local_file_path)
        df = df[df["data_safra"] >= "2024-01-01"]
        df = df[["vendedor", "volume_financeiro", "ganho"]]
        df.rename(columns={"volume_financeiro": "Volume Financeiro"}, inplace=True)

    except Exception as e:
        print(e)


else:
    data = {
        "Produto": ["Arroz", "Feijão", "Macarrão", "Açúcar", "Café"],
        "Quantidade": [50, 30, 150, 25, 40],
        "Preço": [20.5, 15.0, 10.0, 5.0, 18.0],
        "Vendedor": ["Ana", "Carlos", "Beatriz", "Daniel", "Eduardo"],
    }

    df = pd.DataFrame(data)

print(df)
