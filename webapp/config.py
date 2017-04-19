class Config(object):
    SECRET_KEY = '736670cb10a600b695a55839ca3a5aa54a7d7356cdef815d2ad6e19a2031182b'
    RECAPTCHA_PUBLIC_KEY = "6LdKkQQTAAAAAEH0GFj7NLg5tGicaoOus7G9Q5Uw"
    RECAPTCHA_PRIVATE_KEY = '6LdKkQQTAAAAAMYroksPTJ7pWhobYb88fTAcxcYn'

class ProdConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'postgres://qyigqdyqriovxs:b04382028ab03ca11e33ac8f5170dd8d44bd2ca99a6199def37e0a6aaece98ef@ec2-23-23-237-68.compute-1.amazonaws.com:5432/d51cdtt24cutt'

class DevConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://btatum:P@rker101@localhost:5432/cyberSummit'

class HerokuConfig(ProdConfig):
    @classmethod
    def init_app(cls, app):
        ProdConfig.init_app(app)

        from werkzeug.contrib.fixers import ProxyFix
        app.wsgi_app = ProxyFix(app.wsgi_app)

        #log to stderr
        import logging
        from logging import StreamHandler
        file_handler = StreamHandler()
        file_handler.setLevel(logging.WARNING)
        app.logger.addHandler(file_handler)