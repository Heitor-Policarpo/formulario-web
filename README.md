Esse projeto é formulário web simples que permite ao usuário preencher: Nome, telefone, email e assunto. As informações são enviadas por email para um destinatário configurado e registradas automaticamente em uma Google Sheet via API
Eu utilizei o Vs Code como editor de código e as tecnologias que utilizei para fazer esse programa  foram Python (Flask), HTML + CSS , google Sheets API, Email (via SMTP), gspread e python-dotenv.

Puxe o programa do github utilizando o comando "git clone https://github.com/seu-usuario/formulario-web.git" dentro do seu editor de código. 
É necessario criar um ambiente virtual:
Para windows o comando é:
"python -m venv venv
venv\Scripts\activate"

Para linux/mac o comando é:
"python3 -m venv venv
source venv/bin/activate"

Para baixar as bibliotecas o comando é "pip install -r requirements.txt", caso não dê certo esses são os comandos para baixar cada uma manualmente:

"pip install flask";
"pip install dotenv";
"pip install gspread";
"pip install oauth2client".

É necessário criar um google shets com o nome "FormularioWeb".
Troque os nomes do arquivo .env para o nome do seu email e uma senha temporária apenas para essa aplicação no site "https://myaccount.google.com/apppasswords", é necessario ter ativada a verificação de duas etapas na sua conta google.
É necessario criar o arquivo "credentials.json" da conta de serviço do Google na raiz do projeto. Aqui está como criar esse arquivo "https://docs.gspread.org/en/latest/oauth2.html#for-bots-using-service-account", nesse passo a passo ao final você recebera um arquivo json, troque o nome dele para ele ficar "credentials.json" e adicione ele na raiz do projeto.

Com esses passos feitos, é só compartilhar o google sheets com o e-mail que está no arquivo "credentials.json" e dê permisão de editor a esse e-mail.

Agora o código deve funcionar completamente, teste ele fazendo "python app.py" no terminal e depois acesse "http://localhost:5000" para fazer o formulario, depois do formulario enviado ele deve chegar no seu google shets.
