def sentence_reverse(text):
    a = text.split()
    a.reverse()
    return ' '.join(a)
    
x="We are ready"
r=sentence_reverse(x)
print(r)