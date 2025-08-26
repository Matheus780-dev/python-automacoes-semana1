"""Organizador Automático de Arquivos"""

import shutil
from pathlib import Path
from datetime import datetime

MAPEAMENTO = {
    ".pdf": "PDFs",
    ".jpg": "Imagens",
    ".jpeg": "Imagens",
    ".png": "Imagens",
    ".mp3": "Musicas",
    ".mp4": "Videos",
    ".docx": "Documentos",
    ".xlsx": "Planilhas",
    ".txt": "Textos"
}

def registrar_log(log_file: Path, mensagem: str) -> None:
    with open(log_file, "a", encoding="utf-8") as f:
        f.write(mensagem + "\n")

def organizar_arquivos() -> None:
    downloads = Path.home() / "Downloads"
    log_file = downloads / "organizador_log.txt"

    for arquivo in downloads.iterdir():
        if arquivo.is_file():
            extensao = arquivo.suffix.lower()
            if extensao in MAPEAMENTO:
                pasta_destino = downloads / MAPEAMENTO[extensao]
                pasta_destino.mkdir(exist_ok=True)

                novo_caminho = pasta_destino / arquivo.name
                shutil.move(str(arquivo), str(novo_caminho))

                mensagem = f"[{datetime.now().strftime('%d/%m/%Y %H:%M:%S')}] {arquivo.name} → {novo_caminho}"
                print(mensagem)
                registrar_log(log_file, mensagem)

if __name__ == "__main__":
    organizar_arquivos()
