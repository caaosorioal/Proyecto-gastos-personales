import eel

@eel.expose
def abrirPaginaDatos():
      try:
            eel.sleep(1)
            eel.start('paginaDatos.html',
                  chromeFlags = ["--start-fullscreen"],
                  port = 8000,
                  block = False)
      except:
            pass

      print("La prueba funciona")