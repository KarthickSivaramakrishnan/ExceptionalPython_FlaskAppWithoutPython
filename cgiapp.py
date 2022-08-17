import wfastcgi
import sys
import os
from flaskapp import * # just a dummy import to inform pyinstaller to include these modules in executable

if __name__ == '__main__':
    os.environ.update({
        'PYTHONPATH': sys._MEIPASS, 
        'WSGI_HANDLER': 'flaskapp.app' 
        # PYTHONPATH - sys._MEIPASS contains the directory path where this application is deployed as pyinstaller executable.
        # WSGI_HANDLER - modulefile.flaskAppObject - wfastcgi will check for this module and app Object in PYTHONPATH.
    })
    wfastcgi.main()

