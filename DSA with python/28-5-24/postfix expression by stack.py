s="5678+-*"
st=[]
for i in s:
    if i.isdigit():
        st.append(int(i))
    elif i == "+":
        a=st.pop()
        b=st.pop()
        st.append(a+b)
    elif i == "-":
        a=st.pop()
        b=st.pop()
        st.append(a-b)
    elif i == "*":
        a=st.pop()
        b=st.pop()
        st.append(a*b)
    elif i == "/":
        a=st.pop()
        b=st.pop()
        st.append(a/b)
print(st[0])
    
        





