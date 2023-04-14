# HPGL - ReGIS converter

This python code converts simple HPGL plot file to ReGIS graphics file. Result can be output to vintage computer terminals that supports ReGIS graphics, for example DEC VT125 or VT240. This program is made to make demonstration of the vintage graphics terminals easier. It's made to be used with a HPGL plot files that are output by AutoCAD or other vector graphics design programs.

## How to use this program?
This instruction is tested as working using an AutoCAD 2006.
1. In AutoCAD make a drawing inside a 767x469mm rectangle. Each 1mm corresponds to one pixel on the screen of a terminal.
2. I suggest to use a snap to grid function so lines starts and ends in exact locations of the pixels.
3. Add a plotter driver that supports HPGL, for example a good old HP7475. This will let you output a HPGL file.
4. Define a new paper size with 0mm margins. Size does not matter. This is required so you could use whole screen of the terminal.
5. In plot settings use scaling 1:10, offset 0, use a 767x469mm window, tick "plot to file" option.
6. Resulting plot file should be ASCII HPGL file within the ReGIS screen limits.

Now you can use a converter program to convert a HPGL file to ReGIS. The resulting ReGIS file will be output to te screen. If you're connected to the Linux machine from the vintage graphics terminal, it wil display a resulting graphics. If you pipe the script output to a file, you can later send it to the terminal to display a graphics. At the moment this program is only tested with DEC VT125 terminal that's connected to a Linux machine over LAT.

Program arguments:\
-f [filename] - specifies HPGL file to be converted to ReGIS\
-ne - do not erase screen before drawing\
-c0 [RGBCMYWD] - sets channel 0 color to Red, Gree, Blue, Cyan, Magenta, Yellow, White or Dark (black)\
-c1, -c2, -c3 - same as -c0 but for other channels\
-l0 [0-100] - sets channel 0 B&W luminosity 0-100%. Works in 25% steps.\
-l1, -l2, -l3 - same as -l0 but for other channels\
-ct - draws color test pattern - a square for each color with all other color numbers drawn on it\x

Examples:\
regisdraw.py #just clears graphics from the screen\
regisdraw.py -f test.plt #clears screen for other graphics and draws a test.plt file\
regisdraw.py -c0 R -l0 50 #sets channel 0 color to red and channel 0 b&w luminosity to 50%\
regisdraw.py -c0 D -c1 C -c2 M -c3 Y -ct #sets colors for all four channels and draws a color test\

Problems:
- Inkscape outputs HPGL files, but its format is a bit different than AutoCAD output and my program is not properly understanding it at the moment.
- Circle drawing commands are not supported, but that's not a problem, because AutoCAD outputs circles as a bunch of short lines.
- Only four channels (colors) - 0,1,2,3 are supported. All others defaults to 0 (background). That's because only four different colors are supported by VT125.

TODO:
- Check if lines goes out of the screen
- Circle support?
- Scaling support?
- Inkscape HPGL support
- Luminosity check allowed range
- Test all example commands from readme
- Check what's wrhong with the inch-mm coefficient
- Add sample files - simple drawings and HPGL files
