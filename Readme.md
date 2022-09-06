
An extremely hacky script to get data from my i1 Display Pro Colorimeter and display it on a CIE1931 Chromaticity diagram. I did this out of sheer spite and anger that xrite didn't provide an ability to use my colorimeter as anything but a display profiler, despite being a perfectly capable light meter and the _manual that shipped with it_ giving instructions on how to use it as an ambient light sensor.


This requires argyllcms to be installed and its binaries accessible by the system path. It also requires the `colour-science`, `colormath`, and `matplotlib` python packages installed. I'm too lazy to package this in a properly idiomatic format for distribution.

