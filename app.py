import streamlit as st

st.set_page_config(page_title="Prisonade Calculator")
st.subheader("Which Dimension:")
dim = st.radio("",('Spawn', 'Frozen', 'Hell'))
st.subheader("Which Block")
if dim=="Spawn":
     block = st.radio(
          "",
          ('Iron-Stone Mix', 'Diamond-Iron Mix', 'Emerald-Diamond Mix','Ridge Mix'))
     val=int(st.text_input('How Many Blocks?', 0))
     if block=='Iron-Stone Mix':
          a = int(val / 64)
          b = val % 64
          st.header(f"You need {a:,d} stacks and {b} blocks of T3 Stone and Iron ")
     elif block=="Diamond-Iron Mix":
          a=val*4
          b=int(a/64)
          c=a%64
          st.header(f"You need {b:,d} stacks and {c} blocks of T3 Iron and Diamond ")
     elif block=="Emerald-Diamond Mix":
          a=val*10
          b=int(a/64)
          c=a%64
          st.header(f"You need {b:,d} stacks and {c} blocks of T3 Emerald and Diamond ")
     else:
          dia=val*42
          eme=val*30
          iron=val*12
          st.header(f"You need {int(dia/64):,d} Stacks and {dia%64} T3 Diamond")
          st.header(f"You need {int(eme / 64):,d} Stacks and {eme % 64} T3 Emerald")
          st.header(f"You need {int(iron / 64):,d} Stacks and {iron % 64} T3 Iron")
elif dim=="Frozen":
     block = st.radio(
          "",
          ('Blue Ice - Prismarine Mix','Prismarine - Frozen Diamond Mix','Frozen Diamond - Amethyst Mix','Frozen Mix'))
     val = int(st.text_input('How Many Blocks?', 0))
     if block == 'Blue Ice - Prismarine Mix':
          a=val*4
          b = int(a / 64)
          c = a % 64
          st.header(f"You need {b:,d} stacks and {c} blocks of T3 Ice and Prismarine ")
     elif block == "Prismarine - Frozen Diamond Mix":
          pri = val * 8
          fd=val*6
          st.header(f"You need {int(pri/64):,d} stacks and {pri%64} blocks of T3 Prismarine")
          st.header(f"You need {int(fd/64):,d} stacks and {fd%64} blocks of T3 Frozen Diamond")
     elif block == "Frozen Diamond - Amethyst Mix":
          a = val * 12
          b = int(a / 64)
          c = a % 64
          st.header(f"You need {b:,d} stacks and {c} blocks of T3 Frozen Diamond and Amethyst ")
     else:
          ame = val * 60
          fd = val * 90
          pri = val * 40
          st.header(f"You need {int(ame / 64):,d} Stacks and {ame % 64} T3 Amethyst ")
          st.header(f"You need {int(fd / 64):,d} Stacks and {fd % 64} T3 Frozen Diamond")
          st.header(f"You need {int(pri / 64):,d} Stacks and {pri % 64} T3 Prismarine")
elif dim=="Hell":
     block = st.radio(
          "",
          ('Netherrack - Magma Mix','Magma - Fire Gold Mix','Fire Gold - Hell Rock Mix','Hell Mix'))
     val = int(st.text_input('How Many Blocks?', 0))
     if block == 'Netherrack - Magma Mix':
          a=val*4
          b = int(a / 64)
          c = a % 64
          st.header(f"You need {b:,d} stacks and {c} blocks of T3 Netherrack and Magma ")
     elif block == "Magma - Fire Gold Mix":
          a = val * 7
          b = int(a / 64)
          c = a % 64
          st.header(f"You need {b:,d} stacks and {c} blocks of T3 Magma and Fire Gold ")
     elif block == "Fire Gold - Hell Rock Mix":
          fg=val*12
          hr=val*6
          st.header(f"You need {int(fg / 64):,d} Stacks and {fg % 64} T3 Fire Gold ")
          st.header(f"You need {int(hr / 64):,d} Stacks and {hr % 64} T3 Hell Rock")
     else:
          mg = val * 56
          fg = val * 176
          hr = val * 60
          st.header(f"You need {int(mg / 64):,d} Stacks and {mg % 64} T3 Magma")
          st.header(f"You need {int(fg / 64):,d} Stacks and {fg % 64} T3 Fire Gold")
          st.header(f"You need {int(hr / 64):,d} Stacks and {hr % 64} T3 Hell Rock")
st.caption(f"Any Bugs ?")
st.caption(f"Message Stresso#6710 On Discord")
