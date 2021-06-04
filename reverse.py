def reverse( inputStr ):
    revStr = ""
    splitStr = inputStr.split()

    if (splitStr[-1][-1] == "."):
        splitStr[-1] = splitStr[-1][:-1]
        for i in range(len(splitStr)-1):
            revStr += splitStr[-(i+1)]
            revStr += " "
        revStr += splitStr[0]
        revStr += "."
    else:
        for i in range(len(splitStr)-1):
            revStr += splitStr[-(i+1)]
            revStr += " "
        revStr += splitStr[0]

    return revStr

#print(reverse("Nope not for Me."))
