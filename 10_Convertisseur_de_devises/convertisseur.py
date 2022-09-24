# Convertisseur de devise avec Python

# Source = Revue Coding, n°18, p.27.
# Bibliothèque : forex-python (pip install forex-python)


from forex_python.converer import CurrencyRates 

c = CurrencyRates()

amount = int(input("Saisissez le montant à convertir : "))

from_currency = input("Devise source : ").upper()
to_currency = input("Devise cible : ").upper()

print(amount, "conversion de ", from_currency, "vers ", to_currency)

result = c.convert(from_currency, to_currency, amount)

print(result)