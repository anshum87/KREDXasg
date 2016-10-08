from MyApp import app

import logging
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

#from werkzeug.contrib.profiler import ProfilerMiddleware
#app.wsgi_app = ProfilerMiddleware(app.wsgi_app, restrictions=[30])

app.run(debug=False)
