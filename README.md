💀⚡ Ins4niTY.py — Advanced Offensive Validation & Attack Chaining
O Ins4niTY.py é uma plataforma de validação ofensiva de última geração, projetada para transpor a barreira entre a vulnerabilidade teórica e a Prova de Valor (PoC) irrefutável. Combinando a precisão de um motor híbrido com a agressividade de táticas APT (Advanced Persistent Threat), o sistema automatiza o ciclo completo de exploração em ambientes de alta complexidade e arquiteturas Cloud-native.

✨ Diferenciais Estratégicos e Técnicos
Motor de Mutação Reativa & Evasão: Payload tuning em tempo real para bypass de WAFs e IDSs, garantindo furtividade durante o Elite Fuzzing.

Exploração Ativa e Chaining: Automação de cadeias de ataque complexas, incluindo SSRF em nuvem, RCE via OOB (Out-of-Band), Race Conditions e Prototype Pollution.

Auditoria Inteligente e Looting: Sistema integrado de exfiltração que identifica e valida credenciais (AWS, GitHub, DBs) em tempo real, realizando o privilege checking imediato.

Inteligência Acionável: Centralização de evidências em dashboards técnicos, com monitoramento de interações externas e notificações via webhooks.

🛠️ Espectro Total de Auditoria (Módulos de Teste)
1. OPSEC, Evasão e Furtividade
Proxy Rotation: Pool rotativo para evitar bloqueios de IP.

Identity Spoofing: Headers realistas e User-Agents de navegadores modernos/bots legítimos.

Adaptive Payload Mutation: Bypass automático de erro 403 via Double Encoding, Unicode Obfuscation e Case Randomization.

WAF Fingerprinting: Identificação de assinaturas (Cloudflare, Akamai, Imperva, F5).

2. Exploração de Injeções e Execução (RCE)
SSTI (Server-Side Template Injection): Validação em engines como Jinja2 e Twig.

Blind RCE: Testes de execução cegos disparando comandos de callback via HTTP e DNS.

SQL Injection (Time-based): Confirmação via análise de latência de resposta.

Race Condition: Requisições assíncronas simultâneas para falhas de lógica e concorrência.

3. Infraestrutura e Cloud (AWS Focus)
SSRF Advanced: Bypass de IMDSv1 e IMDSv2 em instâncias EC2 (payloads Hex/Decimal).

Key Exterminator: Validação automática de chaves AWS, GitHub e Google Maps com verificação de privilégios "God-Mode".

S3 Bucket Scanner: Auditoria de exposição e listagem pública de arquivos em buckets.

4. Vazamento de Dados e Fuzzing de Elite
Elite Path Fuzzing: Foco nos caminhos estatisticamente mais críticos (ex: /.env, /.git/config).

JS Deep Scanner: Varredura de arquivos JavaScript em busca de segredos e endpoints ocultos.

Dependency Confusion: Análise de package.json contra sequestro de cadeia de suprimentos.

IDOR/BOLA: Validação de falhas de controle de acesso e manipulação de identificadores.



🚀 Instalação e Uso
Clone o repositório:

> git clone https://github.com/XMatheusCoelhoX/Ins4niTY-.git
> cd Ins4niTY-

Instale as dependências:

> pip install requests yara-python

Execução:

> python3 Ins4niTY.py -d alvo.com.br

📊 Core de Auditoria e Reporting
Dashboard HTML Dinâmico: Relatórios interativos com categorização de severidade (Critical/High).

Painel de Comando Real-time: Interface via terminal com métricas de velocidade e subfases do scan.

Data Persistence: Logs sincronizados em JSON para preservação total de evidências.

Why Ins4niTY? Projetado para operações onde a velocidade e a precisão da prova de conceito são mandatórias. Ele não apenas reporta falhas; ele demonstra o impacto real na integridade do negócio.



Desenvolvido por Matheus Coelho Disclaimer: Este software é para fins educacionais e auditorias autorizadas. O uso indevido é de total responsabilidade do operador.
