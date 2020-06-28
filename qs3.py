from bottle import route, run, get, post, request


@route('/encrypt')
def encrypt():
    return '''
        <form action="/encrypt" method="post">
            Message: <input name="message" type="text" />
            <input value="Encrypt message" type="submit" />
        </form>
    '''

@post('/encrypt')
def do_encrypt():
    message = request.forms.get('message')
    return message






run(host="localhost", port=8080, debug=True)
