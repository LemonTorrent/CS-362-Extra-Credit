def reverse( inputStr ):
    revStr = ""
    for i in range(len(inputStr)):
        revStr += inputStr[-(i+1)]

    return revStr

print(reverse("Nope not for Me"))
