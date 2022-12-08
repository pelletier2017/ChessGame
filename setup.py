from setuptools import setup

setup(
    name="ChessGame",
    version="0.01",
    description="Chess Library",
    license="MIT",
    author="Andrew Pelletier",
    py_modules=["chess"],

    install_requires=[
        "Babel==2.4.0",
        "bcrypt==3.1.3",
        "blinker==1.4",
        "certifi==2022.12.7",
        "cffi==1.10.0",
        "chardet==3.0.4",
        "click==6.7",
        "coverage==4.0.3",
        "Flask==0.12.2",
        "Flask-BabelEx==0.9.3",
        "Flask-Login==0.4.0",
        "Flask-Mail==0.9.1",
        "Flask-Principal==0.4.0",
        "Flask-Security==3.0.0",
        "Flask-SQLAlchemy==2.2",
        "Flask-WTF==0.14.2",
        "idna==2.6",
        "itsdangerous==0.24",
        "Jinja2==2.9.6",
        "MarkupSafe==1.0",
        "passlib==1.7.1",
        "pluggy==0.5.1",
        "psycopg2==2.7.3",
        "py==1.4.34",
        "pycparser==2.18",
        "python-coveralls==2.9.1",
        "pytz==2017.2",
        "PyYAML==3.12",
        "requests==2.18.4",
        "six==1.10.0",
        "speaklater==1.3",
        "SQLAlchemy==1.1.13",
        "tox==2.8.0",
        "urllib3==1.22",
        "virtualenv==15.1.0",
        "Werkzeug==0.12.2",
        "WTForms==2.1"
    ]


)