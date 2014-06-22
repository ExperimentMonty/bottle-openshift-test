from bottle import route, default_app, run
import jinja2

@route('/name/<name>')
def nameindex(name='Stranger'):
    return '<strong>Hello, %s!</strong>' % name
 
@route('/')
def index():
    return '<strong>Hello World!</strong>'

# This must be added in order to do correct path lookups for the views
import os
from bottle import TEMPLATE_PATH

# Don't try to run this while we're testing locally.
if __name__ != '__main__':
    TEMPLATE_PATH.append(os.path.join(os.environ['OPENSHIFT_HOMEDIR'],
        'runtime/repo/wsgi/views/'))

application=default_app()

# For local debugging purposes.
# After starting server, it will automatically reload when files are changed.
if __name__ == '__main__':
    run(host='localhost', port=8080, reloader=True)
