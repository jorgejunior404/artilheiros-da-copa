# Artilheiros da Copa

Programa em Python (POO) para listar e atualizar automaticamente os artilheiros da Copa do Mundo.

## API utilizada

O projeto usa a [football-data.org](https://www.football-data.org) (plano free, gratuito pra sempre).

1. Crie uma conta grátis em https://www.football-data.org/client/register e pegue seu token.
2. Crie um arquivo `.env` na raiz do projeto com:
   ```
   API_KEY=seu_token_aqui
   ```
3. A Copa do Mundo tem o código `WC`. Outras competições disponíveis no free tier: `PL` (Premier League), `PD` (La Liga), `BL1` (Bundesliga), `SA` (Serie A), `FL1` (Ligue 1), `CL` (Champions League), entre outras.

**Limitação:** o endpoint de artilheiros (`/scorers`) devolve gols, assistências e pênaltis, mas não o número de jogos disputados — por isso o campo `jogos` fica zerado por enquanto.