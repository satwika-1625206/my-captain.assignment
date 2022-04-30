Python 3.10.3 (tags/v3.10.3:a342a49, Mar 16 2022, 13:07:40) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
def most_frequent(string):
    d=dict()
    for key in string :
        if key not in d:
            d[key]=1
        else:
            d[key]+=1
    return d
print(most_frequent("Mississippi"))
{'i': 4, 's': 4, 'p': 2, 'M':1}
