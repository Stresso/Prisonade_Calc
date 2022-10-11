import streamlit as st

st.set_page_config(page_title="Prisonade Calculator")
st.subheader("Which Realm:")
dim = st.radio("",('Spawn', 'Desert', 'Jungle','Ocean','Abyss'))
st.subheader("Which Block")
if dim=="Spawn":
     block = st.radio(
          "",
          ('Stone-Iron Mix', 'Iron-Diamond Mix', 'Diamond-Emerald Mix','Summit Mix'))
     val=int(st.text_input('How Many Blocks?', 0))
     if block=='Stone-Iron Mix':
          a = int(val / 64)
          b = val % 64
          st.header(f"You need {a:,d} stacks and {b} blocks of T3 Stone and Iron ")
     elif block=="Iron-Diamond Mix":
          a=val*4
          b=int(a/64)
          c=a%64
          st.header(f"You need {b:,d} stacks and {c} blocks of T3 Iron and Diamond ")
     elif block=="Diamond-Emerald Mix":
          a=val*8
          b=int(a/64)
          c=a%64
          st.header(f"You need {b:,d} stacks and {c} blocks of T3 Emerald and Diamond ")
     else:
          dia=val*36
          eme=val*24
          iron=val*12
          if ((iron % 64)==0):
               st.header(f"You need {int(iron / 64):,d} Stacks of T3 Iron")
          else:
               st.header(f"You need {int(iron / 64):,d} Stacks and {iron % 64} T3 Iron")12
          if ((dia % 64)==0):
               st.header(f"You need {int(dia / 64):,d} Stacks of T3 Diamond")
          else:
               st.header(f"You need {int(dia/64):,d} Stacks and {dia%64} T3 Diamond")12
          if ((eme % 64)==0):
               st.header(f"You need {int(eme / 64):,d} Stacks of T3 Emerald")
          else:
               st.header(f"You need {int(eme / 64):,d} Stacks and {eme % 64} T3 Emerald")
elif dim=="Desert":
     block = st.radio(
          "",
          ('Sandstone-Copper Mix','Copper-Gold Mix','Gold-Desert Gem Mix','Desert Mix'))
     val = int(st.text_input('How Many Blocks?', 0))
     if block == 'Sandstone-Copper Mix':
          a=val*2
          b = int(a / 64)
          c = a % 64
          st.header(f"You need {b:,d} stacks and {c} blocks of T3 Sandstone and Copper ")
     elif block == "Copper-Gold Mix":
          pri = val * 6
          fd=val*5
          st.header(f"You need {int(pri/64):,d} stacks and {pri%64} blocks of T3 Copper")
          st.header(f"You need {int(fd/64):,d} stacks and {fd%64} blocks of T3 Gold")
     elif block == "Gold-Desert Gem Mix":
          a = val * 10
          b = int(a / 64)
          c = a % 64
          st.header(f"You need {b:,d} stacks and {c} blocks of T3 Gold and Desert Gem ")
     else:
          ame = val * 24
          fd = val * 60
          pri = val * 40
          st.header(f"You need {int(ame / 64):,d} Stacks and {ame % 64} T3 Copper ")
          st.header(f"You need {int(fd / 64):,d} Stacks and {fd % 64} T3 Gold")
          st.header(f"You need {int(pri / 64):,d} Stacks and {pri % 64} T3 Desert Gem")
elif dim=="Jungle":
     block = st.radio(
          "",
          ('Granite-Basalt Mix','Basalt-Coal Mix','Coal-Lapis Mix','Jungle Mix'))
     val = int(st.text_input('How Many Blocks?', 0))
     if block == 'Granite-Basalt Mix':
          a=val*4
          b = int(a / 64)
          c = a % 64
          st.header(f"You need {b:,d} stacks and {c} blocks of T3 Granite and Basalt ")
     elif block == "Coal-Lapis Mix":
          a = val * 12
          b = int(a / 64)
          c = a % 64
          st.header(f"You need {b:,d} stacks and {c} blocks of T3 Coal and Lapis ")
     elif block == "Basalt-Coal Mix":
          fg=val*8
          hr=val*6
          st.header(f"You need {int(fg / 64):,d} Stacks and {fg % 64} T3 Basalt ")
          st.header(f"You need {int(hr / 64):,d} Stacks and {hr % 64} T3 Coal")
     else:
          mg = val * 40
          fg = val * 90
          hr = val * 60
          st.header(f"You need {int(mg / 64):,d} Stacks and {mg % 64} T3 Basalt")
          st.header(f"You need {int(fg / 64):,d} Stacks and {fg % 64} T3 Coal ")
          st.header(f"You need {int(hr / 64):,d} Stacks and {hr % 64} T3 Lapis ")
elif dim=="Ocean":
     block = st.radio(
          "",
          ('Prismarine- Pink Coral Mix','Pink Coral-Fire Coral Mix','Fire Coral-Blue Coral Mix','Ocean Mix'))
     val = int(st.text_input('How Many Blocks?', 0))
     if block == 'Prismarine- Pink Coral Mix':
          a=val*5
          b = int(a / 64)
          c = a % 64
          st.header(f"You need {b:,d} stacks and {c} blocks of T3 Prismarine and Pink Coral ")
     elif block == "Fire Coral-Blue Coral Mix":
          a = val * 13
          b = int(a / 64)
          c = a % 64
          st.header(f"You need {b:,d} stacks and {c} blocks of T3 Fire Coral and Blue Coral ")
     elif block == "Pink Coral-Fire Coral Mix":
          fg=val*8
          hr=val*7
          st.header(f"You need {int(fg / 64):,d} Stacks and {fg % 64} T3 Pink Coral ")
          st.header(f"You need {int(hr / 64):,d} Stacks and {hr % 64} T3 Fire Coral")
     else:
          mg = val * 48
          fg = val * 120
          hr = val * 78
          st.header(f"You need {int(mg / 64):,d} Stacks and {mg % 64} T3 Pink Coral")
          st.header(f"You need {int(fg / 64):,d} Stacks and {fg % 64} T3 Fire Coral ")
          st.header(f"You need {int(hr / 64):,d} Stacks and {hr % 64} T3 Blue Coral ")
elif dim=="Abyss":
     block = st.radio(
          "",
          ('Void Stone-Amethyst Mix','Amethyst-Hell Rock Mix','Hell Rock-Obsidian Mix','Abyss Mix'))
     val = int(st.text_input('How Many Blocks?', 0))
     if block == 'Void Stone-Amethyst Mix':
          a=val*6
          b = int(a / 64)
          c = a % 64
          st.header(f"You need {b:,d} stacks and {c} blocks of T3 Void Stone and Amethyst ")
     elif block == "Amethyst-Hell Rock Mix":
          fg=val*10
          hr=val*8
          st.header(f"You need {int(fg / 64):,d} Stacks and {fg % 64} T3 Amethyst ")
          st.header(f"You need {int(hr / 64):,d} Stacks and {hr % 64} T3 Hell Rock")
     elif block == "Hell Rock-Obsidian Mix":
          fg=val*15
          hr=val*8
          st.header(f"You need {int(fg / 64):,d} Stacks and {fg % 64} T3 Hell Rock ")
          st.header(f"You need {int(hr / 64):,d} Stacks and {hr % 64} T3 Obsidian")
     else:
          mg = val * 80
          fg = val * 184
          hr = val * 64
          st.header(f"You need {int(mg / 64):,d} Stacks and {mg % 64} T3 Amethyst")
          st.header(f"You need {int(fg / 64):,d} Stacks and {fg % 64} T3 Hell Rock ")
          st.header(f"You need {int(hr / 64):,d} Stacks and {hr % 64} T3 Obsidian ")
st.caption(f"Any Bugs ?")
st.caption(f"Message Stresso#6710 or Illusioner_#0127 On Discord ")
