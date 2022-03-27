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
for i in range(1, csr):
    sp += i
for i in range(1, fsr):
    sq += i
quest=sq-sp
Stoken=(sq-sp)*10
rtoken=(fsr-csr)*1559
st.title(f'Quest Point Required:{quest} | Stoken Required:{Stoken} | Rtoken Required:{rtoken}')
