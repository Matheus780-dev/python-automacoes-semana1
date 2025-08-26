"""Backup + Envio Automático por E-mail"""

import os
import shutil
import smtplib
from pathlib import Path
from datetime import datetime
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from os.path import basename

EMAIL_USER = os.getenv("EMAIL_USER")
EMAIL_PASS = os.getenv("EMAIL_PASS")

PASTA_ORIGEM = Path.home() / "Downloads"
PASTA_BACKUP = Path("C:/Backups")
DESTINATARIOS = ["seu_email@gmail.com"]

def criar_backup() -> Path:
    PASTA_BACKUP.mkdir(parents=True, exist_ok=True)
    data_hora = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    nome_arquivo = f"backup_{data_hora}"
    caminho_zip = PASTA_BACKUP / nome_arquivo
    shutil.make_archive(str(caminho_zip), 'zip', PASTA_ORIGEM)
    return caminho_zip.with_suffix(".zip")

def enviar_email_com_anexo(destinatarios, assunto, mensagem, caminho_arquivo: Path) -> None:
    if not Path(caminho_arquivo).exists():
        raise FileNotFoundError(f"Arquivo não encontrado: {caminho_arquivo}")

    msg = MIMEMultipart()
    msg["From"] = EMAIL_USER
    msg["To"] = ",".join(destinatarios)
    msg["Subject"] = assunto

    msg.attach(MIMEText(mensagem, "plain", "utf-8"))

    with open(caminho_arquivo, "rb") as arquivo:
        parte = MIMEBase("application", "octet-stream")
        parte.set_payload(arquivo.read())
    encoders.encode_base64(parte)
    parte.add_header("Content-Disposition",
                     f"attachment; filename={basename(caminho_arquivo)}")
    msg.attach(parte)

    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as servidor:
            servidor.starttls()
            servidor.login(EMAIL_USER, EMAIL_PASS)
            servidor.send_message(msg)
        print(f"📧 E-mail enviado com sucesso para {destinatarios}")
    except Exception as e:
        print(f"❌ Erro ao enviar e-mail: {e}")

if __name__ == "__main__":
    print("📂 Criando backup...")
    arquivo_backup = criar_backup()
    print(f"✅ Backup criado: {arquivo_backup}")

    print("📧 Enviando e-mail...")
    enviar_email_com_anexo(
        DESTINATARIOS,
        "Backup Diário Automático",
        "Segue em anexo o backup gerado automaticamente.",
        arquivo_backup
    )
