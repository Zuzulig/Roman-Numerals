priradenie = { 1: 'I', 4: 'IV', 5: 'V', 9: 'IX', 10: 'X', 40: 'XL',
              50: 'L', 90: 'XC', 100: 'C', 400: 'XD', 500: 'D', 900: 'CM', 1000: 'M'}
cislo=int(input("Enter a number: "))
nummer=[1000,900,500,400,100,90,50,40,10,9,5,4,1]

for i in nummer:
    if cislo != 0:
       kvocient=cislo//i

       if kvocient != 0:
            for y in range(kvocient):
                print(priradenie[i], end="")


       cislo=cislo%i



