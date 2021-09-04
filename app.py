from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

curl --location --request POST 'https://api.telegram.org/bot1980859217:AAEJiw0rhDJN4kcaRfV2ebcUSPZVcKKIyxA/setWebhook' \
--header 'Content-Type: application/json' \
--data-raw '{
    "url": "https://0c69-87-245-169-226.ngrok.io"
}'

curl\
     --socks5-hostname 127.0.0.1:9050\
     --header 'Content-Type: application/json'\
     --request 'POST'\
     --data '{"chat_id":"-347712505","text":"Проверка связи"}' \
     "https://api.telegram.org/bot1980859217:AAEJiw0rhDJN4kcaRfV2ebcUSPZVcKKIyxA/sendMessage"