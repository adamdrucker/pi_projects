from bottle import route, run, get, post, request
from sitecrypt_bottle import *

@route('/message')
def message_in():
    return '''
        <form action="/encrypt" method="post">
            Message: <input name="message" type="text" />
            <input value="Encrypt message" type="submit" />
        </form>
    '''

@post('/encrypted')
def do_encrypt():
    message = request.forms.get('message')
    
    generate_otp(100)
    sheet = load_sheet("otp.txt")    
    ciphertext = encrypt(message, sheet)
    save_file("encrypted.txt", ciphertext)
    ciphertext = load_file("encrypted.txt")
    return ciphertext
    



run(host="localhost", port=8080, debug=True)
