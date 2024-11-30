Python 3.13.0 (tags/v3.13.0:60403a5, Oct  7 2024, 09:38:07) [MSC v.1941 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
def calcul_pgcd(a,b):
    while b != 0:
        a,b = b,a%b
        return a
    num1 = int(input("entrez le premier nombre :"))
    num2 = int(input("entrez le deuxieme nombre :"))
    pgcd = calcul_pgcd(num1,num2)
    print(f"le pgcd de (num1) et (num2) est :(pgcd)")
 except valueError:
     
SyntaxError: unindent does not match any outer indentation level
def calcul_pgcd(a,b):
    while b != 0:
...         a,b = b,a%b
...         return a
...     num1 = int(input("entrez le premier nombre :"))
...     num2 = int(input("entrez le deuxieme nombre :"))
...     pgcd = calcul_pgcd(num1,num2)
...     print(f"le pgcd de (num1) et (num2) est :(pgcd)")
...  except valueError :
...      
SyntaxError: unindent does not match any outer indentation level
>>> def calcul_pgcd(a,b):
...     while b != 0:
...         a,b = b,a%b
...         return a
...     num1 = int(input("entrez le premier nombre :"))
...     num2 = int(input("entrez le deuxieme nombre :"))
...     pgcd = calcul_pgcd(num1,num2)
...     print(f"le pgcd de (num1) et (num2) est :(pgcd)")
...  except valueError
...  
SyntaxError: unindent does not match any outer indentation level
>>> def calcul_pgcd(a,b):
...     while b != 0:
...         a,b = b,a%b
...         return a
...     num1 = int(input("entrez le premier nombre :"))
...     num2 = int(input("entrez le deuxieme nombre :"))
...     pgcd = calcul_pgcd(num1,num2)
...     print(f"le pgcd de (num1) et (num2) est :(pgcd)")
...  except valueError:
...      
SyntaxError: unindent does not match any outer indentation level
>>> def calcul_pgcd(a,b):
...     while b:
...         a, b = b, a%b
...         return a
...     num1 = int(input("entrez le premier nombre :"))
...     num2 = int(input("entrez le deuxieme nombre :"))
...     pgcd = calcul_pgcd(num1,num2)
...     print(f"le pgcd de {num1} et {num2} est {pgcd}")
