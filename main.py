#Assets
from Website import web

#Config
from config import config

#Run
if __name__ == '__main__':
    web(config).run(debug=True)