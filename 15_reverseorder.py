def reverseorder(a):
    split = a.split()
    reversedsplit = split[::-1]
    joined = " ".join(reversedsplit)
    return joined

sentence = input("Enter a sentence you would like reversed: ")
reversedtext = reverseorder(sentence)
print(reversedtext)
