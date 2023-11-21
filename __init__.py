from flask import Flask, jsonify, request

app = Flask(__name__)

# Cuando recibamos las peticioness


@app.route('/webhook/', methods=['GET', 'POST'])
def webhook_whatsapp():
    # Datos recibidos via GET
    if request.method == 'GET':
        # Si el token es igual al que recibimos
        if request.args.get('hub.verify_token') == 'mi_token':
            # Retornamos el valor de hub.challenge
            return request.args.get('hub.challenge')
        else:
            return 'Token invalido, no tienes permisos'

    # Datos recibidos via JSON
    data = request.get_json()

    # Obtenemos el número del cliente y su mensaje
    telefono_cliente = data['entry'][0]['changes'][0]['value']['messages'][0]['from']
    # Extraemos el mensaje
    mensaje_cliente = data['entry'][0]['changes'][0]['value']['messages'][0]['text']['body']
    # Extraemos el Id de WhatsApp
    id_whatsapp = data['entry'][0]['changes'][0]['value']['messages'][0]['id']
    # Obtenemos la fecha y hora del mensaje
    timestamp = data['entry'][0]['changes'][0]['value']['messages'][0]['timestamp']

    # Escribimos el numero de telefono y el mensaje enel archivo de texto
    if mensaje_cliente is not None:
        from rivescript import RiveScript
        # Inicializamos RiveScript
        bot = RiveScript()
        bot.load_file("chatia.rive")
        bot.sort_replies()
        
        # Obtenemos la respuesta del bot
        respuesta = bot.reply('localuser', mensaje_cliente)
        respuesta = respuesta.replace('\\n', '\\\n')
        respuesta = respuesta.replace('\\', '')
        
        enviar_mensaje(telefono_cliente, respuesta)
        
        # Retornamos status
        return jsonify({'status': 'success'}, 200)
    
def enviar_mensaje(telefono_cliente, respuesta):
    from heyoo import WhatsApp
    # Token
    token = '[TOKEN]'
    
    #Identificador del numero de telefono dado por Facebook
    id_num_whatsapp = '[numero de telefono]]'
    
    # Inicializamos envio de mensajes
    mensaje_whatsapp = WhatsApp(token, id_num_whatsapp)
    telefono_cliente = telefono_cliente.replace('521','52')
    
    # Enviamos el mensaje
    mensaje_whatsapp.send_message(respuesta, telefono_cliente)
        


if __name__ == "__main__":
    app.run(debug=True)
