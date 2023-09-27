




def anagrama(palabra1, palabra2):
    if sorted(palabra1.lower()) == sorted(palabra2.lower()):
        print("Son anagrama")
    else:
        print("No son anagrama")
            

        
anagrama("zhol", "aloh")