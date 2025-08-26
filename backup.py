"""Backup Automático da Pasta Downloads"""

import os
import shutil
import stat
from pathlib import Path
from datetime import datetime

def remover_forcado(func, path, exc_info):
    os.chmod(path, stat.S_IWRITE)
    func(path)

def executar_backup() -> None:
    origem = Path.home() / "Downloads"
    destino_base = Path("C:/Backups")
    destino_base.mkdir(exist_ok=True)

    nome = datetime.now().strftime("backup_%Y-%m-%d_%H-%M-%S")
    destino = destino_base / nome

    shutil.copytree(origem, destino)
    zip_path = shutil.make_archive(str(destino), "zip", destino)
    print(f"[{datetime.now().strftime('%H:%M:%S')}] ✅ Backup criado: {zip_path}")

    shutil.rmtree(destino, onerror=remover_forcado)

    backups = sorted(
        [b for b in destino_base.iterdir() if b.suffix == ".zip"],
        key=os.path.getmtime
    )

    for backup_antigo in backups[:-3]:
        os.remove(backup_antigo)
        print(f"🗑️ Backup antigo apagado: {backup_antigo}")

if __name__ == "__main__":
    executar_backup()
