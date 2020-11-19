import eel
import os
from validarCredenciales import validarEntrada
from abrirPagina import abrirPaginaDatos

directorio = os.path.dirname(__file__)

eel.init(os.path.abspath(os.path.join(directorio, '..', 'front')))

eel.start('index.html',
          chromeFlags = ["--start-fullscreen"],
          port = 8080)