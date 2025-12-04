## Real State App

🚀 1. Criar e ativar ambiente virtual

Cria o ambiente isolado para o projeto:

```bash
python -m venv venv
```

Ativa o ambiente virtual:

```bash
venv\Scripts\activate
```

🗄️ 2. Configurar o Prisma
🔹 Rodar a primeira migração (cria o banco)
```bash
prisma migrate dev --name init
```

🗄️ 3. Aplicar o Prisma
🔹 Criar uma nova migração
```bash
prisma migrate dev --name add_new_model
```

🔹 Regenerar o cliente Prisma
```bash
prisma generate
```

▶️ 4. Executar o servidor FastAPI

Inicia a API em modo de recarga automática:

```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000
```
