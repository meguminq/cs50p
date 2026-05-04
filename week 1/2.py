gr = input('Greeting: ')

match gr:
    case 'hello' | 'Hello' | 'Hello,' | 'hello,':
        print('$0')
    case 'hey' | 'how' | 'Hey' | 'How' | 'hey,' | 'how,' | 'Hey,' | 'How,':
        print('$20')
    case _:
        print('$100')