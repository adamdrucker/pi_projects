from bottle import route, run, get, post, request, template, error
from sitecrypt_bottle import *
from captcha_bot import captcha
import pyperclip as pc

url = captcha()

@route('/message')
def message_in():
    return '''
        <form action="/encrypted" method="post">
            Message: <input name="message" type="text" />
            <input value="Encrypt message" type="submit" />
        </form>
    '''

@post('/encrypted')
def do_encrypt():
    message = request.forms.get('message')
    url = captcha()
    global ciphertext
    
    # Functions called from 'sitecrypt_bottle'
    # 'Message' passed as argument
    generate_otp(len(message))
    sheet = load_sheet("otp.txt")    
    ciphertext = encrypt(message, sheet)
    save_file("encrypted.txt", ciphertext)
    ciphertext = load_file("encrypted.txt")

      
    return '''
        <table style="width:50%", border=1px solid black>
            <tr>
                <th>Encrypted message</th>
                <th>Sharable link</th>
            </tr>
            <tr>
                <td>{message}</td>
                <td><a href=localhost:8080/message/{url}>localhost:8080/message/{url}</a></td>
            </tr>
        </table>
    '''.format(message=ciphertext, url=url)




@route('/message/<url>')
def show_message(url=url):
    sheet = load_sheet("otp.txt")
    ciphertext = load_file("encrypted.txt")
    plaintext = decrypt(ciphertext, sheet)

    return '''
        <table style="width:50%", border=1px solid black>
            <tr>
                <th>Decrypted message</th>                
            </tr>
            <tr>
                <td>{message}</td>                
            </tr>
        </table>
    '''.format(message=plaintext)



# Try maybe @post decorator after this @route decorator to have it load a new page
# that has the decrypted message?

# Have the new page display the encrypted message, add a button to call decryption?

# Issue: the two text files (OTP and encrypted) generated are stored locally -- how would
# this work on a public website?

# Copy button failed, unable to find out how to copy the link generated in the <a href> tag


# ///////////////////////////////////////////////////////////////////////
# ERROR
@error('500')
def error500(error):
    return 'ERROR 500: Dude, you fucked up. Go back and edit your code.'



# //////////////////////////////////////////
run(host="localhost", port=8080, debug=True)
