1. README.md (Versão Ins4niTY)
Markdown
# Ins4niTY.py — Aggressive Secret Scanner 💀🔥

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE.md)
[![Status](https://img.shields.io/badge/status-Insane-red)](#)

O **Ins4niTY.py** é um scanner de segredos de ultra-performance, desenhado para ser a ferramenta definitiva em operações de Red Team e Bug Bounty. O seu objetivo é simples: encontrar o que deveria estar escondido, com uma velocidade e agressividade sem precedentes.

## ⚡ Porquê Ins4niTY?

- **Agressividade Pura**: Motor multi-threaded capaz de lidar com volumes massivos de dados sem perda de precisão.
- **Ecossistema de Recon**: Automatiza o uso de `subfinder`, `gau` e `Wayback Machine` para garantir que nenhum endpoint fique de fora.
- **Inteligência de Deteção**:
    - **YARA Core**: Regras avançadas para identificar chaves de cloud (AWS, Azure, GCP), tokens de comunicação (Slack, Telegram) e muito mais.
    - **Shannon Entropy**: Identifica segredos baseados na aleatoriedade dos dados, capturando chaves que não seguem padrões fixos.
    - **Base64 Deep Scan**: Decodificação inteligente para encontrar payloads escondidos.
- **Watchdog Anti-Kill**: Sistema de monitorização em tempo real que garante a continuidade da execução mesmo em ambientes instáveis.
- **Pronto para SOC/SIEM**: Integração nativa para exportar achados via API (FastAPI) e sistemas de alerta externos.

## 🛠️ Instalação

1. Clone o repositório:
```bash
> git clone [https://github.com/seu-usuario/Ins4niTY.git](https://github.com/seu-usuario/Ins4niTY.git)
> cd Ins4niTY

Instale as dependências:

> pip install requests yara-python

💻 Utilização

Para um varrimento agressivo completo:

> python3 Ins4niTY.py -d alvo.com.br

Comandos Principais:

-d, --domain: Define o domínio alvo para a fase de Recon.

-i, --input: Carrega uma lista personalizada de URLs.

-o, --output: Define o ficheiro de saída para os relatórios.

🛡️ Disclaimer

Esta ferramenta foi criada para profissionais de cibersegurança. O uso do Ins4niTY.py para atividades ilícitas é estritamente proibido. O autor não se responsabiliza por quaisquer danos ou uso indevido.

Desenvolvido por Matheus Coelho
# Ins4niTY-
