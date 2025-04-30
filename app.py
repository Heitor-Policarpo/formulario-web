from flask import Flask, render_template, request
from dotenv import load_dotenv
import os
import smtplib
from email.mime.text import MIMEText
import gspread
from oauth2client.service_account import ServiceAccountCredentials

load_dotenv()

remetente = os.getenv("EMAIL_USUARIO")
senha = os.getenv("EMAIL_SENHA")


app = Flask(__name__)

@app.route('/')
def form():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
    nome = request.form['nome']
    telefone = request.form['telefone']
    email = request.form['email']
    assunto = request.form['assunto']

    enviar_email(nome, telefone, email, assunto)
    salvar_em_planilha(nome, telefone, email, assunto)

    return "Formulário enviado com sucesso!"


def enviar_email(nome, telefone, email, assunto):
    remetente = os.getenv("EMAIL_USUARIO")
    senha = os.getenv("EMAIL_SENHA")
    destinatario = remetente  # Pode ser outro, se quiser

    corpo = f"Nome: {nome}\nTelefone: {telefone}\nEmail: {email}\nAssunto: {assunto}"
    msg = MIMEText(corpo)
    msg['Subject'] = "Novo contato do formulário"
    msg['From'] = remetente
    msg['To'] = destinatario

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as servidor:
        servidor.login(remetente, senha)
        servidor.send_message(msg)

def salvar_em_planilha(nome, telefone, email, assunto):
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
    client = gspread.authorize(creds)

    planilha = client.open("FormularioWeb").sheet1  # Nome da sua planilha
    planilha.append_row([nome, telefone, email, assunto])

if __name__ == '__main__':
    app.run(debug=True)