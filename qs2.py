from bottle import route, run, get, post, request, template, error
from sitecrypt_bottle import *
from captcha_bot import captcha

url = captcha() # How to get this random string used as the post URL???

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
    

    # Functions called from 'sitecrypt_bottle'
    # 'Message' passed as argument
    generate_otp(len(message))
    sheet = load_sheet("otp.txt")    
    ciphertext = encrypt(message, sheet)
    save_file("encrypted.txt", ciphertext)
    ciphertext = load_file("encrypted.txt")
    global ciphertext # this is apparently unadvisable

   
      
    return '''
        <table style="width:50%", border=1px solid black>
            <tr>
                <th>Encrypted message</th>
                <th>Sharable link</th>
            </tr>
            <tr>
                <td>{message}</td>
                <td><a href=localhost:8080/message/{url}>Link</a></td>
            </tr>
        </table>
    '''.format(message=ciphertext, url=url)




@route('/message/<url>')
def show_message(url=url):
    return ciphertext

    #return "localhost:8080/message/{url}".format(url=url)

    # Ciphertext variable is out of scope (except when cast as a global var)
    # This function can't reference it; furthermore it will need to be passed
    # in to the decryption function, which is what this decorated URL should
    # ultimately be calling and returning a value from

# Try maybe @post decorator after this @route decorator to have it load a new page
# that has the decrypted message?


# ///////////////////////////////////////////////////////////////////////
# ERROR
@error('500')
def error500(error):
    return 'ERROR 500: Dude, you fucked up. Go back and edit your code.'



# //////////////////////////////////////////
run(host="localhost", port=8080, debug=True)
