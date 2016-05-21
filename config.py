import os
basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

WTF_CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'

OAUTH_CREDENTIALS = {
    'facebook': {
        'id': '131150650254246',
        'secret': 'e44489e006c039a99996388e4cde5a46'
    },
    'twitter': {
        'id': 't724wQasNgcKWkmS4mYIjVs5G',
        'secret': 'hCRV8Q2xd7sQ3t6vMpziqOHOf3e4kovQN78tCmIPnMBsvMv8wK'
    }
}

OPENID_PROVIDERS = [
    {'name': 'Google', 'url': 'https://www.google.com/accounts/o8/id'},
    {'name': 'Yahoo', 'url': 'https://me.yahoo.com'},
    {'name': 'AOL', 'url': 'http://openid.aol.com/<username>'},
    {'name': 'Flickr', 'url': 'http://www.flickr.com/<username>'},
    {'name': 'MyOpenID', 'url': 'https://www.myopenid.com'}]

