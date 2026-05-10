a = input()
if a.endswith('.gif') or a.endswith('.jpg') or a.endswith('.jpeg') or a.endswith('.png'):
    print('image/' + a[-4:])
elif a.endswith('.pdf') or a.endswith('.txt') or a.endswith('.zip'):
    print('application/' + a[-4:])
else:
    print('application/octet-stream')
