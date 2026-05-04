def main():
    tm = input('What time is it? ')
    if 7 <= convert(tm) <= 8:
        print('breakfast time')
    elif 12 <= convert(tm) <= 13:
        print('lunch time')
    elif 18 <= convert(tm) <= 19:
        print('dinner time')
    

def convert(time):
    h, m = time.split(':')
    hn = float(h)
    mn = float(m)
    return hn + (mn / 60)

if __name__ == '__main__':
    main()
    