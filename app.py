
import streamlit as st

st.set_page_config(page_title="Prisonade Calculator")
st.subheader("Which Realm:")
dim = st.radio("",('River', 'Ranch', 'Port','Empire','Citadel'))
st.subheader("Which Block")
if dim=="River":
     block = st.radio(
          "",
          ('Stone-Iron Mix', 'Iron-Diamond Mix', 'Diamond-Emerald Mix','River Mix'))
     val=int(st.text_input('How Many Blocks?', 0))
     if block=='Stone-Iron Mix':
          a = int(val / 64)
          b = val % 64
          if ((b % 64)==0):
               st.header(f"You need {a:,d} Stacks of  T3 Emerald")
          else:
               st.header(f"You need {a:,d} stacks and {b} blocks of T3 Emerald")
elif dim=="Ranch":
     block = st.radio(
          "",
          ('Granite-Coal Mix','Coal-Copper Mix','Copper-Redstone Gem Mix','Ranch Mix'))
     val = int(st.text_input('How Many Blocks?', 0))
     if block == 'Granite-Coal Mix':
          a=val*2
          b = int(a / 64)
          c = a % 64
          if ((c % 64)==0):
               st.header(f"You need {b:,d} Stacks of T3 Granite and Coal ")
          else:
               st.header(f"You need {b:,d} stacks and {c} blocks of T3 Granite and Coal ")
     elif block == "Coal-Copper Mix":
          pri = val * 6
          fd=val*5
          if ((pri % 64)==0):
               st.header(f"You need {int(pri/64):,d} Stacks of T3 Coal")
          else:
               st.header(f"You need {int(pri/64):,d} stacks and {pri%64} blocks of T3 Coal")
          if ((fd % 64)==0):
               st.header(f"You need {int(fd/64):,d} Stacks of T3 Copper")
          else:
               st.header(f"You need {int(fd/64):,d} stacks and {fd%64} blocks of T3 Copper")
     elif block == "Copper-Redstone Mix":
          a = val * 10
          b = int(a / 64)
          c = a % 64
          if ((c % 64)==0):
               st.header(f"You need {b:,d} Stacks of T3 Copper and Redstone")
          else:
               st.header(f"You need {b:,d} stacks and {c} blocks of T3 Copper and Redstone ")
     else:
          ame = val * 24
          fd = val * 60
          pri = val * 40
          if ((ame % 64)==0):
               st.header(f"You need {int(ame/64):,d} Stacks of T3 Coal")
          else:
               st.header(f"You need {int(ame / 64):,d} Stacks and {ame % 64} T3 Coal ")
          if ((fd % 64)==0):
               st.header(f"You need {int(fd/64):,d} Stacks of T3 Copper")
          else:
               st.header(f"You need {int(fd / 64):,d} Stacks and {fd % 64} T3 Copper")
          if ((pri % 64)==0):
               st.header(f"You need {int(pri/64):,d} Stacks of T3 Redstone")
          else:
               st.header(f"You need {int(pri / 64):,d} Stacks and {pri % 64} T3 Redstone")
elif dim=="Port":
     block = st.radio(
          "",
          ('Sandstone-Prismarine Mix','Prismarine-Oceanstone Mix','Oceanstone-Seashine Mix','Port Mix'))
     val = int(st.text_input('How Many Blocks?', 0))
     if block == 'Sandstone-Prismarine Mix':
          a=val*4
          b = int(a / 64)
          c = a % 64
          if ((c % 64)==0):
               st.header(f"You need {b:,d} Stacks of T3 Sandstone and Prismarine")
          else:
               st.header(f"You need {b:,d} stacks and {c} blocks of T3 Sandstone and Prismarine ")
     elif block == "Prismarine-Oceanstone Mix":
          fg=val*8
          hr=val*6
          if ((fg % 64)==0):
               st.header(f"You need {int(fg/64):,d} Stacks of T3 Prismarine")
          else:
               st.header(f"You need {int(fg / 64):,d} Stacks and {fg % 64} T3 Prismarine")
          if ((hr % 64)==0):
               st.header(f"You need {int(hr/64):,d} Stacks of T3 Oceanstone")
          else:
               st.header(f"You need {int(hr / 64):,d} Stacks and {hr % 64} T3 Oceanstone")
     elif block == "Oceanstone-Seashine Mix":
          a = val * 12
          b = int(a / 64)
          c = a % 64
          if ((c % 64)==0):
               st.header(f"You need {b:,d} Stacks of T3 Oceanstone and Seashine")
          else:
               st.header(f"You need {b:,d} stacks and {c} blocks of T3 Oceanstone and Seashine ")
     else:
          mg = val * 40
          fg = val * 90
          hr = val * 60
          if ((mg % 64)==0):
               st.header(f"You need {int(mg/64):,d} Stacks of T3 Prismarine")
          else:
               st.header(f"You need {int(mg / 64):,d} Stacks and {mg % 64} T3 Prismarine")
          if ((fg % 64)==0):
               st.header(f"You need {int(fg/64):,d} Stacks of T3 Oceanstone")
          else:
               st.header(f"You need {int(fg / 64):,d} Stacks and {fg % 64} T3 Oceanstone ")
          if ((hr % 64)==0):
               st.header(f"You need {int(hr/64):,d} Stacks of T3 Seashine")
          else:
               st.header(f"You need {int(hr / 64):,d} Stacks and {hr % 64} T3 Seashine")
elif dim=="Empire":
     block = st.radio(
          "",
          ('Moss Stone-Star Rock Mix','Star Rock-Aztez Relic Mix','Aztec Relic-Amethyst Mix','Empire Mix'))
     val = int(st.text_input('How Many Blocks?', 0))
     if block == 'Moss Stone-Star Rock Mix':
          a=val*5
          b = int(a / 64)
          c = a % 64
          if ((c % 64)==0):
               st.header(f"You need {b:,d} Stacks of T3 Gold and Moss Stone and Star Rock")
          else:
               st.header(f"You need {b:,d} stacks and {c} blocks of T3 Moss Stone and Star Rock ")
     elif block == "Star Rock-Aztez Relic Mix":
          fg=val*8
          hr=val*7
          if ((fg % 64)==0):
               st.header(f"You need {int(fg/64):,d} Stacks of T3 Star Rock")
          else:
               st.header(f"You need {int(fg / 64):,d} Stacks and {fg % 64} T3 Star Rock ")
          if ((hr % 64)==0):
               st.header(f"You need {int(hr/64):,d} Stacks of T3 Aztec Relic")
          else:
               st.header(f"You need {int(hr / 64):,d} Stacks and {hr % 64} T3 Azteec Relic")
     elif block == "Aztec Relic-Amethyst Mix Mix":
          a = val * 13
          b = int(a / 64)
          c = a % 64
          if ((c % 64)==0):
               st.header(f"You need {b:,d} Stacks of T3 Aztec Relic and Amethyst")
          else:
               st.header(f"You need {b:,d} stacks and {c} blocks of T3 Aztec Relic and Amethyst")
     else:
          mg = val * 48
          fg = val * 120
          hr = val * 78
          if ((mg % 64)==0):
               st.header(f"You need {int(mg/64):,d} Stacks of T3 Star Rock")
          else:
               st.header(f"You need {int(mg / 64):,d} Stacks and {mg % 64} T3 Star Rock")
          if ((fg % 64)==0):
               st.header(f"You need {int(fg/64):,d} Stacks of T3 Aztec Relic")
          else:
               st.header(f"You need {int(fg / 64):,d} Stacks and {fg % 64} T3 Aztec Relic ")
          if ((hr % 64)==0):
               st.header(f"You need {int(hr/64):,d} Stacks of T3 Amethyst")
          else:
               st.header(f"You need {int(hr / 64):,d} Stacks and {hr % 64} T3 Amethyst")
elif dim=="Citadel":
     block = st.radio(
          "",
          ('Marble-Purpur Mix','Purpur-Magma Mix','Magma-Obsidian Mix','Citadel Mix'))
     val = int(st.text_input('How Many Blocks?', 0))
     if block == 'Marble-Purpur Mix':
          a=val*6
          b = int(a / 64)
          c = a % 64
          if ((c % 64)==0):
               st.header(f"You need {b:,d} Stacks of T3 Marble and Purpur")
          else:
               st.header(f"You need {b:,d} stacks and {c} blocks of T3 Marble and Purpur ")
     elif block == "Purpur-Magma Mix":
          fg=val*10
          hr=val*8
          if ((fg % 64)==0):
               st.header(f"You need {int(fg/64):,d} Stacks of T3 Purpur")
          else:
               st.header(f"You need {int(fg / 64):,d} Stacks and {fg % 64} T3 Purpur ")
          if ((hr % 64)==0):
               st.header(f"You need {int(hr/64):,d} Stacks of T3 Magma")
          else:
               st.header(f"You need {int(hr / 64):,d} Stacks and {hr % 64} T3 Magma")
     elif block == "Magma-Obsidian Mix":
          fg=val*15
          hr=val*8
          if ((fg % 64)==0):
               st.header(f"You need {int(fg/64):,d} Stacks of T3 Magma")
          else:
               st.header(f"You need {int(fg / 64):,d} Stacks and {fg % 64} T3 Magma ")
          if ((hr % 64)==0):
               st.header(f"You need {int(hr/64):,d} Stacks of T3 Obsidian")
          else:
          fg = val * 184
          hr = val * 64
          mg = val *80
          if ((fg % 64)==0):
               st.header(f"You need {int(mg/64):,d} Stacks of Purpur")
          else:
               st.header(f"You need {int(mg / 64):,d} Stacks and {mg % 64} T3 Purpur")
          if ((fg % 64)==0):
               st.header(f"You need {int(fg/64):,d} Stacks of T3 Magma")
          else:
               st.header(f"You need {int(fg / 64):,d} Stacks and {fg % 64} T3 Magma ")
          if ((hr % 64)==0):
               st.header(f"You need {int(hr/64):,d} Stacks of T3 Obsidian")
          else:
               st.header(f"You need {int(hr / 64):,d} Stacks and {hr % 64} T3 Obsidian ")
st.caption(f"Any Bugs ?")
st.caption(f"Message Illusioner_#0127 On Discord ")
