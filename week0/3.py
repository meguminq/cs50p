def convert(st):
    st = st.replace(':(', '🙁 ')
    st = st.replace(':)', '🙂 ')
    return st
result = input()
print(convert(result))