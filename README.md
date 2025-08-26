# 📂 Projetos de Automação em Python – Semana 1

Este repositório contém os projetos desenvolvidos na **Semana 1** do plano de estudos de **Automação com Python + UiPath**.  
O foco desta semana foi manipulação de arquivos, criação de backups, envio automático de arquivos e agendamento de tarefas com Python.

---

## 📑 Projetos

### 1️⃣ Organizador de Arquivos (`organizador.py`)
- Move automaticamente arquivos da pasta **Downloads** para subpastas organizadas por tipo.
- Tipos suportados:
  - `.pdf` → **PDFs**
  - `.jpg`, `.jpeg`, `.png` → **Imagens**
  - `.mp3` → **Músicas**
  - `.mp4` → **Vídeos**
  - `.docx` → **Documentos**
  - `.xlsx` → **Planilhas**
  - `.txt` → **Textos**
- Mantém um arquivo de **log (`organizador_log.txt`)** registrando todas as ações realizadas.

---

### 2️⃣ Backup Automático (`backup.py`)
- Cria um backup completo da pasta **Downloads**.
- Compacta cada backup em um arquivo `.zip`.
- Nomeia os backups com **data e hora** (ex.: `backup_2025-08-22_11-50-00.zip`).
- Mantém apenas os **3 últimos backups**, apagando automaticamente os mais antigos.
- Pode ser agendado com a biblioteca `schedule` para rodar em horários definidos.

---

### 3️⃣ Backup + Envio Automático por E-mail (`backup_email.py`)
- Cria um backup **zipado** da pasta **Downloads**.
- Envia o arquivo automaticamente por **e-mail** para um ou mais destinatários.
- Usa variáveis de ambiente já configuradas no **PowerShell**:
  - `EMAIL_USER` → seu e-mail de envio (ex.: Gmail)
  - `EMAIL_PASS` → senha de aplicativo (não a senha normal)
- Ideal para enviar **relatórios diários automáticos** ou manter cópias de segurança na nuvem (via caixa de e-mail).

---

## 🚀 Como Executar

### Pré-requisitos
- **Python 3.10+**
- Bibliotecas utilizadas:
  ```bash
  pip install schedule
  ```

### Configurar credenciais (no PowerShell do Windows)
Antes de rodar o script de e-mail, configure as variáveis de ambiente:
```powershell
$env:EMAIL_USER="seu_email@gmail.com"
$env:EMAIL_PASS="sua_senha_de_app"
```

### Rodando os scripts
1. Clone o repositório:
   ```bash
   git clone https://github.com/SEU_USUARIO/python-automacoes-semana1.git
   ```
2. Entre na pasta do projeto.
3. Execute o script desejado:

   **Organizador de Arquivos**
   ```bash
   python organizador.py
   ```

   **Backup Automático**
   ```bash
   python backup.py
   ```

   **Backup + E-mail Automático**
   ```bash
   python backup_email.py
   ```

---

## 🛠️ Tecnologias utilizadas
- Python (`pathlib`, `shutil`, `datetime`, `os`, `smtplib`, `email`, `schedule`)
- Git + GitHub

---

## 📌 Autor
Projeto desenvolvido por **Matheus** como parte do plano intensivo de **Automação com Python + UiPath (4 semanas)**.
