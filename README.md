# microblog
Restart on Miguel Grinberg's Flask tutorial.

For information see blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world.

To use this repository, be sure you have python 3 installed.
Initialize a git repository, pull this project to your local branch, then do the following.
I.Create a virtual environment for flask in the root folder of this project
  `$ python3 -m venv flask`

II. Run the following commands:
  (for Linux)
  A. `$ flask/bin/pip install flask`
  B. `$ flask/bin/pip install flask-login`
  C. `$ flask/bin/pip install flask-openid`
  D. `$ flask/bin/pip install flask-mail`
  E. `$ flask/bin/pip install flask-sqlalchemy`
  F. `$ flask/bin/pip install sqlalchemy-migrate`
  G. `$ flask/bin/pip install flask-whooshalchemy`
  H. `$ flask/bin/pip install flask-wtf`
  I. `$ flask/bin/pip install flask-babel`
  J. `$ flask/bin/pip install guess_language`
  K. `$ flask/bin/pip install flipflop`
  L. `$ flask/bin/pip install coverage`
  (for Windows, replace "flask/bin/pip" with "flask\Scripts\pip")

III. Change a few files to executables:
  `$ chmod a+x filename`
  run.py, db_create.py, db_migrate.py, db_upgrade.py, db_downgrade.py
  (or run these with `$ flask\Scripts\python filename`)
  
IV. run db_create.py & db_migrate.py

V. run run.py and then go to "localhost:5000" in your browser
