# HPGL - ReGIS converter

This python code converts simple HPGL plot file to ReGIS graphics file. Result can be output to vintage computer terminals that supports ReGIS graphics, for example DEC VT125 or VT240. This program is made to make demonstration of the vintage graphics terminals easier. It's made to be used with a HPGL plot files that are output by AutoCAD.

## How to use this program?
This instruction is tested as working using an AutoCAD 2006.
1. In AutoCAD make a drawing inside a 767x469mm rectangle. Each 1mm corresponds to one pixel on the screen of a terminal.
2. I suggest to use a snap to grid function so lines starts and ends in exact locations of the pixels.
3. Add a plotter that supports HPGL, for example a good old HP7475. This will let you output a HPGL file.
4. Define a new paper size with 0mm margins. This is required so you could use whole screen of the terminal.
5. In plot settings use scaling 1:10, offset 0, use a 767x469mm window, tick "plot to file" option.
6. Resulting plot file should be ASCII HPGL file.

Now you can use a converter program to convert a HPGL file to ReGIS with a command plothpgl.py [name of the file]. The resulting ReGIS file will be output to te screen. If you're connected to the Linux machine from the vintage graphics terminal, it wil display a resulting graphics. If you pipe the script output to a file, you can later send it to the terminal to display a graphics.

Problems:
Inkscape outputs HPGL files, but its format is a bit different than AutoCAD output and my program is not properly understanding it.
Circle drawing commands are not supported, but that's not a problem, because AutoCAD outputs circles as a bunch of short lines.
Only three "pens" (colors) - 1,2,3 are supported. All others defaults to 0 (background). That's because only four different colors are supported by VT125.




TODO:
Check if lines goes out of the screen
Circle support?
Scaling support?
Inkscape HPGL support
