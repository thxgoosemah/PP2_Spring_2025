def reversed_s(sentence):
    words = sentence.split()  
    reversed_words = words[::-1]  
    return ' '.join(reversed_words)  

sentence = input(": ")
reversed_sentences = reversed_s(sentence)
print("Reversed sentence:", reversed_sentences)
