Python 3.13.0 (tags/v3.13.0:60403a5, Oct  7 2024, 09:38:07) [MSC v.1941 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def dervee(a,b):
...     D = f"f' (x)={2 * a}x+{b}" if b !=0 else f"f' {2*a}x"
...     return D
...     def primitive(a,b,c):
...         P = f"F(x)={a/3}x^3 + {b/2}^2 + {c}x + c"
...         return P
...     try:
...         a= float(input(entrez le coefficient a"))
...                        
SyntaxError: unterminated string literal (detected at line 8)
>>> def dervee(a,b):
...     D = f"f' (x)={2 * a}x+{b}" if b !=0 else f"f' {2*a}x"
...     return D
...     def primitive(a,b,c):
...         P = f"F(x)={a/3}x^3 + {b/2}^2 + {c}x + c"
...         return P
...     try:
...         a= float(input("entrez le coefficient a"))
...         b= float (input(entrez le coefficient b"))
...                         
SyntaxError: unterminated string literal (detected at line 9)
>>> def dervee(a,b):
...     D = f"f' (x)={2 * a}x+{b}" if b !=0 else f"f' {2*a}x"
...     return D
...     def primitive(a,b,c):
...         P = f"F(x)={a/3}x^3 + {b/2}^2 + {c}x + c"
...         return P
...     try:
...         a= float(input("entrez le coefficient a"))
...         b= float (input("entrez le coefficient b"))
...         c= float (input("entrez le coefficient c"))
...         D= derivee(a,b)
...         print(f"primitive{p}")
