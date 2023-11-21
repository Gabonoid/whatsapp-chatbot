# WhatsApp Chatbot con Flask y RiveScript
Este proyecto implementa un chatbot de WhatsApp utilizando Flask como framework web y RiveScript para la lógica de conversación.

## Configuración

1. **Instalación de dependencias:**
   ```bash
   pip install Flask rivescript heyoo
   ```
## Configuración del entorno:
Asegúrate de tener tu archivo chatia.rive con las reglas de respuesta de RiveScript.
Reemplaza ```[TOKEN]``` con tu token de WhatsApp en el archivo ```__init__.py```.
Reemplaza ```[numero de telefono]``` con el identificador de tu número de teléfono dado por Facebook.
### Ejecutar la aplicación:
```bash
python __init__.py
```
### Uso
Ejecuta la aplicación utilizando el comando anterior.
Configura tu webhook de WhatsApp para que apunte a la URL de tu aplicación en /webhook/.
Envía mensajes a tu número de WhatsApp configurado y observa las respuestas generadas por el chatbot.
#### Archivos Importantes
- ```__init__.py```: Contiene la lógica principal de la aplicación Flask y la integración con RiveScript.
- ```chatia.rive```: Archivo RiveScript que define las reglas de conversación del chatbot.
#### Personalización del Chatbot
El archivo chatia.rive contiene las respuestas predefinidas del chatbot. Puedes personalizar estas respuestas para adaptarlas a las necesidades específicas de tu servicio de atención al cliente.
