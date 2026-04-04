print("Operações:1(soma), 2(subtração), 3(multiplicação), 4(divisão), 5(potenciação), 6(raiz quadrada)")
operacao=int(input("Digite a operação que deseja: "))
if operacao==1:
    n1=float(input("Digite número 1: "))
    n2=float(input("Digite número 2: "))
    resultado=n1+n2
    print("O resultado é ",resultado)
elif operacao==2:
    n1=float(input("Digite número 1: "))
    n2=float(input("Digite número 2: "))
    resultado=n1-n2
    print("O resultado é ",resultado)
elif operacao==3:
    n1=float(input("Digite número 1: "))
    n2=float(input("Digite número 2: "))
    resultado=n1*n2
    print("O resultado é ",resultado)
elif operacao==4:
    n1=float(input("Digite número 1: "))
    n2=float(input("Digite número 2: "))
    resultado=n1/n2
    print("O resultado é ",resultado)
elif operacao==5:
    n1=float(input("Digite número 1: "))
    n2=float(input("Digite o número para qual vai se elevado: "))
    resultado=pow(n1,n2)
    print("o resultado é ",resultado)
else:
    if operacao==6:
        n1=float(input("Digite número 1: "))
        resultado=n1**0.5
        print("o resultado é ",resultado)
