alpha=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def position(c):
    for i in range(0,26):
        if c==alpha[i]:
            return i         
def vigenerCrypt(n,k):
    pn = position(n)
    pk = position(k)
    pChi = (pn+pk)%26
    return pChi
    
def vigenerDecrypt(n,k):
    pn = position(n)
    pk = position(k)
    pDechi = (pn-pk)%26
    return pDechi

def chiffrer(text,cle):
    chainChiffre = ''
    if len(cle)<len(text):
        for i in range(len(text)):
            cle = cle + cle[i]
            if len(cle) == len(text):
                break
    for i in range(len(text)):
        chainChiffre=chainChiffre + alpha[vigenerCrypt(text[i],cle[i])]
    return chainChiffre

def dechiffrer(text,cle):
     chainDechiffre = ''
     if len(cle)<len(text):
         for i in range(len(text)):
             cle = cle + cle[i]
             if len(cle) == len(text):
                 break
     for i in range(len(text)):
         chainDechiffre = chainDechiffre + alpha[vigenerDecrypt(text[i],cle[i])]
     return chainDechiffre


msg=input("entrer le message a dechiffrer : ")
cle=input("entrer le cle du chiffrement: ")
mssgchiffre = chiffrer(msg,cle)
print("le message chiffre :"+mssgchiffre)

msg=input("entrer le message a dechiffrer : ")
cle=input("entrer le cle du chiffrement: ")
mssgdechiffre = dechiffrer(msg,cle)
print("le message dechiffre :"+mssgdechiffre)

