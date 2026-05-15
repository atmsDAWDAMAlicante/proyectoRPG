# Validar

class Validaciones:
  @staticmethod
  def validar_menu_en_rango(opcion_menu, lim):
    try:
      menu_validado = int(opcion_menu)
    except ValueError:
      print(f'Introduce un número entero entre el 0 y el {lim}')
      return False
    else:
      if ((menu_validado < 0) or (menu_validado > lim)):
        print(f'Introduce un número entero dentro entre el 0 y el {lim}')
        return False
      else:
        return True