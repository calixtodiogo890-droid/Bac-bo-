from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

class GraficoInput(BaseModel):
    olho_grande: str
    barata: str
    pequeno: str
    caminho_grande: List[str]

@app.post("/analisar")
def analisar_padroes(dados: GraficoInput):
    vermelhos = [g for g in [dados.olho_grande, dados.barata, dados.pequeno] if g == "vermelho"]
    azuis = [g for g in [dados.olho_grande, dados.barata, dados.pequeno] if g == "azul"]

    sequencia = dados.caminho_grande[-4:]
    tendencia = sequencia.count(sequencia[-1]) >= 3

    if len(vermelhos) == 3 and tendência:
        return {
            "entrada_sugerida": sequencia[-1],
            "grau_de_confianca": "Alta",
            "justificativa": "Gráficos derivados indicam padrão repetido e Caminho Grande confirma sequência."
        }
    elif len(vermelhos) >= 2:
        return {
            "entrada_sugerida": sequencia[-1],
            "grau_de_confianca": "Média",
            "justificativa": "Padrão ainda está presente, mas há sinais de instabilidade."
        }
    elif len(azuis) >= 2:
        return {
            "entrada_sugerida": "aguardar",
            "grau_de_confianca": "Baixa",
            "justificativa": "Gráficos indicam quebra de padrão, melhor não entrar agora."
        }
    else:
        return {
            "entrada_sugerida": "tie",
            "grau_de_confianca": "Neutra",
            "justificativa": "Sem padrão claro, possível empate ou rodada instável."
        }
      fastapi
uvicorn
pydantic

web: uvicorn main:app --host=0.0.0.0 --port=8000

# Bac Bo Pattern Analysis API

API para análise de padrões do Bac Bo Evolution usando FastAPI.

## Como rodar localmente

```bash
pip install -r requirements.txt
uvicorn main:app --reload

