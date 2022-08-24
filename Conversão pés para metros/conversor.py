menu = {1: "Pés para metros", 2: "Metros para pés"}

def feet_to_meters(value):
  return "{0:.2f}m".format(value * 0.3048)

def meters_to_feet(value):
  return "{0:.2f}ft".format(value * 3.281)

def printMenu():
  print('Escolha uma opção para converter')
  for chave, valor in menu.items():
    print("{0} - {1}".format(chave, valor))

def convert(option, value):
  if(option == 1):
    return feet_to_meters(value)
  else:
    return meters_to_feet(value)

def opcaoValida(value):
  for op in menu.keys():
    if value == op:
      return True

  return False

