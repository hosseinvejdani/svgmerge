import svgutils.transform as st

background = st.fromfile('files/test-1.svg')
top1 = st.fromfile('files/test-2.svg')
top2 = st.fromfile('files/test-3.svg')
background.append(top1)
background.append(top2)
background.save('result.svg')
