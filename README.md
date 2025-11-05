# Scissor

O projeto propõe um sistema multiagente que modela debates polarizados com agentes que utilizam falácias e escalada retórica, evidenciando o papel de mecanismos de má-fé na amplificação de divisões e na ausência de convergência dialética.

## Motivação

Inspirado no ensaio ["Sort By Controversial"](https://slatestarcodex.com/2018/10/30/sort-by-controversial/) de Scott Alexander, que explora o conceito de **"Scissor Statements"** - declarações que dividem grupos de forma extremamente polarizada, onde cada lado acha sua posição tão obviamente correta que considera o outro irracional ou mal-intencionado.

**Objetivo:** Expor os mecanismos da polarização online de forma interativa.

## Como rodar

### 1. Instale as dependências

```bash
uv sync
```

### 2. Configure sua API key

Obtenha uma chave em: https://aistudio.google.com/app/api-keys

```bash
GOOGLE_GENAI_USE_VERTEXAI=0
GOOGLE_API_KEY=SUA_CHAVE
```

Se preferir, apenas renomeie o arquivo `.env.example` para `.env`.

### 3. Execute

Via ADK Web UI (recomendado):

```bash
adk web
```

Via CLI:

```bash
adk run scissor
```

### 4. Inicie um debate

Digite qualquer tópico divisivo, exemplo:

- "AI vai substituir programadores"
- "Trabalho remoto é mais produtivo"
- "Criptomoedas são seguras"

Assista os agentes debaterem em **6 posts** (3 rounds) com escalada progressiva de polarização.

## Customização

**Mudar número de rounds:**

```python
# scissor/agent.py
debate_loop = LoopAgent(
    max_iterations=5,  # Padrão: 3
)
```

**Ajustar temperatura (criatividade):**

```python
# scissor/sub_agents/ecomax/agent.py
generate_content_config=GenerateContentConfig(
    temperature=1.5,  # Padrão: 1.2 (0.0-2.0)
)
```

**Modificar táticas de debate:**
Edite os prompts em:

- `scissor/sub_agents/ecomax/prompt.py`
- `scissor/sub_agents/veritas/prompt.py`

## Suporte multilíngue

O sistema detecta automaticamente o idioma do input (Português, Inglês, Espanhol, etc.) e conduz o debate nesse idioma.

---

Este é um projeto experimental para fins educacionais
