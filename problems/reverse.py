# = [0,10,20,40]
#L[::-1]
#[40, 20, 10, 0]

def reverse(text):
    if len(text) <= 1:
        return text
    return reverse(text[1:]) + text[0]
print (reverse("Alex"))

