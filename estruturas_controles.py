
idade = int(input("Digite sua idade: "))

if idade < 18:
    print(" Você é menor de idade!")
elif 18 <= idade <= 25:
    print("Você é maior de idade e jovem!") 
elif 26 <= idade <= 56:
    print("Você um adulto!")
else:
    print("Você é idoso!")      