from bottle import route, run, get, post, request, template, error
from sitecrypt_bottle import *
from captcha_bot import captcha

url = captcha() # How to get this random string used as the post URL???

@route('/message')
def message_in():
    return '''
        <form action="/<url>" method="post">
            Message: <input name="message" type="text" />
            <input value="Encrypt message" type="submit" />
        </form>
    '''


@post('/<url>')
def do_encrypt():
    message = request.forms.get('message')

    # Functions called from 'sitecrypt_bottle'
    # 'Message' passed as argument
    generate_otp(len(message))
    sheet = load_sheet("otp.txt")    
    ciphertext = encrypt(message, sheet)
    save_file("encrypted.txt", ciphertext)
    ciphertext = load_file("encrypted.txt")

        
    # Bottle template returning encrypted message
    # tpl = template("Encrypted message: {{message}}", message=ciphertext)
    
      
    return '''
        <table style="width:50%", border=1px solid black>
            <tr>
                <th>Encrypted message</th>
            </tr>
            <tr>
                <td>{message}</td>
            </tr>
        </table>
    '''.format(message=ciphertext)


@error('500')
def error500(error):
    return 'ERROR 500: Dude, you fucked up. Go back and edit your code.'


run(host="localhost", port=8080, debug=True)
