from flask import render_template

def get_signup(form):
    print('FORM IN GET: ', form)
    print('ALL KEYS IN FORM: ', vars(form))
    print('FIELDS KEY IN FORM: ', vars(form)['_fields'])
    print('FIELDS KEY IN FORM: ', vars(form)['_fields'])
    print('KEY OBJECT IN FORM: ', vars(form)['_fields']['key'])
    print('KEY VALUE IN FORM: ', vars(form)['_fields']['key'].data)
    return render_template(
        'pages/signup.html', 
        form = form
    ), 200