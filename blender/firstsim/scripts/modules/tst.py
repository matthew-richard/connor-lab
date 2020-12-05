newvar = 'first'
print(newvar)
def localvsglobal():
    global newvar

    print('newvar previously:')
    print(newvar)
    newvar = 'New var string'
    print('set newvar')
    print(newvar)
