import string
alphabet_string = string.ascii_lowercase
print(alphabet_string)
alphabet_string_idex = [alphabet_string.index(i) for i in alphabet_string]
print(alphabet_string_idex)

message = "You have a list in a list so its not working the way you think it should"
def encrypte (text, n = 0):
    text = list(text.split(sep=" "))
    codeText = []
    for w in text:
        w = w.lower()
        emptyList_1 = []
        for l in w:
            for a in alphabet_string:
                if l == a:
                    emptyList_1.append(alphabet_string.index(a)+n)
        emptyList_12 = []
        for i in emptyList_1:
            if i > 25 :
                i -= 26
            elif i < 0:
                i += 26
            else :
                i = i
            emptyList_12.append(i)
        codeText.append(emptyList_12)
    textCode = []
    for x in codeText:
        emptyList_2 = []
        for y in x:
            for z in alphabet_string_idex:
                if y == z:
                    emptyList_2.append(alphabet_string[z])
        emptyList_2 = "".join(map(str, emptyList_2))
        textCode.append(emptyList_2)
    textCode = " ".join(word for word in textCode)
    return textCode

encrypte(message,n=-5)



"The solution of 365DS"
import string
alphabet_string = string.ascii_lowercase

def shift_amount(amount):
    return amount%26

def encryte_message (texte, shift):
    texte = texte.lower()
    output = ""
    for char in texte:
        if char not in alphabet_string:
            output = output + char
        else:
            alphabet_idex = alphabet_string.find(char)
            output = output + alphabet_string[shift_amount(alphabet_idex + shift)]
    return output

message = "The cat sat on the mat"

message_encrypted = encryte_message(message, 11)
print(message_encrypted)

message_decrypted = encryte_message(message_encrypted, -11)
print(message_decrypted)
