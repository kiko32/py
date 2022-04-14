print("olá senhor.")
print("escreva o seu nome aqui em baixo")  
nome=input("qual é o seu nome:")
print("olá senhor", nome ,"seja bem vindo" )

resposta = "s"

while resposta == "s" :
    numero1 = input ("escreva um numero:")
    numero2 = input ("escreva outro numero:")
    numero3 = print ("a soma entre os dois numeros que escolheu é:" , int(numero2) + int(numero1) )
    resposta = input("queres fazer outra conta?")
 
print("adeus!")