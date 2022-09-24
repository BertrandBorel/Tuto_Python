# Convertir des nombres romains en nombres décimaux 

# Source = Revue Coding, n°18, p.28.

valeurs = {
    'I': 1,
    'V': 5,
    'X': 10, 
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}

def RomanNumeralToDecimal(romanNumeral):
    sum = 0
    for i in range(len(romanNumeral)-1):
        left = romanNumeral[i]
        right = romanNumeral[i + 1]
        if valeurs[left] < valeurs[right]:
            sum -= valeurs[left]
        else :
            sum += valeurs[left]
        sum += valeurs[romanNumeral[-1]]
        return sum

print(RomanNumeralToDecimal("XV")) 