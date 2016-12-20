def rot13(message):
    alphabet = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'
    for i in message:
        index = alphabet.find(i)
        message = message.replace(i, alphabet[index:index+1]
    return message

print message("hello")
