def is_palindrome(str_to_evaluate):
    cleaned = ""    #cadena vacía para guardar lo que tengamos de resultado
    
    for char in str_to_evaluate.lower():
        if char.isalnum():      #es letra o número, se queda. cualquier otra cosa se va
            cleaned += char     #ya que se quedó, lo guardamos en cleaned
            
    return cleaned == cleaned[::-1]     #compara lo que quedó al final en cleaned y lo lee en reversa para decir si es T o F