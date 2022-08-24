import conversor

op = 0

while(not conversor.opcaoValida(op)):
  conversor.printMenu()
  op = int(input("Opção: "))

valor = float(input("Digite o valor a ser convertido: "))

resultado = conversor.convert(op, valor)
print("Resultado: {0}".format(resultado));