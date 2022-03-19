import svgutils.transform as st
from cairosvg import svg2png

background = st.fromfile('files/test-1.svg')
top1 = st.fromfile('files/test-2.svg')
top2 = st.fromfile('files/test-3.svg')
background.append(top1)
background.append(top2)
background.save('result.svg')

# convert svg to png file
svg2png(url='result.svg', write_to='result.png', dpi=72,
        output_height=600, output_width=600)
