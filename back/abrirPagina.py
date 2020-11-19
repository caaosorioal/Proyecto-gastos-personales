import eel

@eel.expose
def abrirPaginaDatos():
      try:
            eel.start('paginaDatos.html',
                  chromeFlags = ["--start-fullscreen"],
                  port = 8000)
      except:
            pass

      print("La prueba funciona")