import os
import colour
from colormath.color_objects import sRGBColor, XYZColor
from colormath.color_conversions import convert_color


xyz_input = os.popen("spotread -a -O | grep Result | awk '{print $4,$5,$6}' | tr -d ','").read()
XYZ = [float(num) for num in xyz_input.split(" ")]
#XYZ = [ 35.664770, 35.025429, 19.647311]

xyz = XYZColor(*[component/100 for component in XYZ])
rgb = convert_color(xyz, sRGBColor)
RGB = [255*col for col in rgb.get_value_tuple()]

colour.plotting.plot_RGB_chromaticities_in_chromaticity_diagram_CIE1931(RGB)
