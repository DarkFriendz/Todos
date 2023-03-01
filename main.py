#Assets
from website import web

#Config
from config import config

#Run
if __name__ == '__main__':
    #Config = Uses settings from config.py
    web(config).run(debug=True)