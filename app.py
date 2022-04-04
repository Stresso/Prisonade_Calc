import streamlit as st

st.title("Cherry SR Calculator, By:ExStresso")

csr = int(st.text_input('Current SR (Default is 0)', 0))
fsr = int(st.text_input('SR to Reach (Default is 4000)', 4000))
f = 0
g = 0
sp = 0
sq = 0
for i in range(0, csr + 1):
    f += i
for i in range(0, fsr + 1):
    g += i
for i in range(1, csr+1):
    sp += i
for i in range(1, fsr+1):
    sq += i
cheapSR=st.radio("Cheap SR Unlocked (S tokens is 10x Cheaper",("Yes","No"))
quest=sq-sp
if cheapSR='Yes':
    Stoken=(sq-sp)*1000000   
else:
    Stoken=(sq-sp)*10000000
rtoken=(fsr-csr)*1553
st.title(f'Quest Point Required:{quest:,d} ')
st.title(f'S-token Required :{Stoken:,d}')
st.title(f'R-token Required:{rtoken:,d}')
