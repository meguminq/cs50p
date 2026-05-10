gr = input('Greeting: ').strip().lower()

if gr.startswith('hello'):
    print('$0')
elif gr.startswith('h'):
    print('$20')
else:
    print('$100')