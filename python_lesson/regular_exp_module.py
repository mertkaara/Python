import re

result = dir(re)

# re module
myString = "Python kursu: Python Programlama Rehberiniz | 40 saat"

# result = re.findall("Python",myString)    # "Python" ifadesini bulur/bulduğu 2 python ifadesini liste şeklinde yazdırdı
# result = len(result)

# result = re.split(" ",myString) # " " karakterinden itibaren böler

# result = re.sub(" ","-",myString)   # Boşluk karakterlerini - ile değiştirir

result = re.search("Python",myString)   # match objesi döndürdü
# result = result.span()  # Arananın şeyin konumunu verir
result = result.start() # hangi indexten başladığını verir


# print(result)

""" Reguler Expression """

""" [] - Köşeli parantezler arasına yazılan bütün karakterler aranır.add()
        [abc]   => a        :1 match
                => ac       :2 match
                => python   :no match
                
        [a-e]   => [abcde]
        [1-5]   => [12345]
        [0-39]  => [01..39]
        
        [^abc]  => abc dışındaki karakterler.
        [^0-9]  => rakam olmayan karakterler.
        
"""

result = re.findall("[abc]",myString)
result = re.findall("[sat]",myString)
result = re.findall("[a-e]",myString)
result = re.findall("[^a-f]",myString)

""" . herhangi bir tek karakteri belirtir
    
        ..  => a    :no match
            => ab   :1 match
            => abc  :1 match
            => abcd :2 match  
                  
"""
test = "abc"
result = re.findall("...",myString)
result = re.findall("..",test)
result = re.findall("Py...n",myString)


"""   
    ^ - Belirtilen karakterle başlıyor mu?
"""
result = re.findall("^P",myString)

"""
    $ - Belirtilen karakterle bitiyor mu?
"""
result = re.findall("t$",myString)

print(result)