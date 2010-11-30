import os
import sys
import site

PROJECT_NAME = 'guckstdu'
PROJECT_ROOT = os.path.dirname(__file__)
CODE_ROOT = os.path.join(PROJECT_ROOT,PROJECT_NAME)
site_packages = os.path.join(PROJECT_ROOT, 'env/lib/python2.5/site-packages')
site.addsitedir(os.path.abspath(site_packages))
sys.path.insert(0, PROJECT_ROOT)
sys.path.insert(0, CODE_ROOT)
os.environ['DJANGO_SETTINGS_MODULE'] = PROJECT_NAME + '.settings'

# needed because feincms can't handle models.py not loaded prior to feincms
# from django.core.management.validation import get_validation_errors
# try:
#     from cStringIO import StringIO
# except ImportError:
#     from StringIO import StringIO
# s = StringIO()
# num_errors = get_validation_errors(s, None)
 
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()

