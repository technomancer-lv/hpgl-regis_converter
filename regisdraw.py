#!/usr/bin/python3
import argparse

# Initantiate the parser
parser = argparse.ArgumentParser(prog='HPGL to ReGIS converter',description='Program that converts HPGL plotter file to ReGIS vector graphics file. It can be used to demonstrate a vintage computer terminals that support ReGIS graphics commands. HPGL plotter file can be generated from various modern vector graphics design programs like AutoCAD or Inkscape.',epilog='Feel free to use this program for your own fun on your own risk. If you find it useful, feel free to contact me or have a look at my retro-computer related twitter profile twitter.com/nuclearlighter')
parser.add_argument('-f',help='HPGL file name')
parser.add_argument('-c0',help='Color 0,RGBCMYWD')
parser.add_argument('-c1',help='Color 1,RGBCMYWD')
parser.add_argument('-c2',help='Color 2,RGBCMYWD')
parser.add_argument('-c3',help='Color 3,RGBCMYWD')
parser.add_argument('-l0',type=int,help='B&W luminosity 0,0-100')
parser.add_argument('-l1',type=int,help='B&W luminosity 1,0-100')
parser.add_argument('-l2',type=int,help='B&W luminosity 2,0-100')
parser.add_argument('-l3',type=int,help='B&W luminosity 3,0-100')
parser.add_argument('-ne',action='store_true',help='Do not erase screen')
parser.add_argument('-nd',action='store_true',help='Do not draw, only set colors')
parser.add_argument('-ct',action='store_true',help='Draw color test')
args = parser.parse_args()

#Movement modes h and i are from BBC-GL graphical language.
#This program is based on my HPGL to BBC-GL converter, that's why these letters are used.
MovementMode="h"	#h-pen up, i-pen down

#Dictionary for colors
ColorDict={
	'R':'(AH120L50S100)',	#Red
	'G':'(AH240L50S100)',	#Green
	'B':'(AH0L50S100)',	#Blue
	'C':'(AH300L50S100)',	#Cyan
	'M':'(AH60L50S100)',	#Magenta
	'Y':'(AH180L50S100)',	#Yellow
	'W':'(AH0L100S100)',	#White
	'D':'(L0)(AH0L0S100)'}	#Black (Dark)

#Initialises ReGIS mode and clears screen if requested
if(args.ne==True):
	OutFile="\x1BP0p,"
else:
	OutFile="\x1BP0p,S(E),"

#Sets colors if requested
if(args.c0!=None):
	try:
		OutFile+="S(M0"+ColorDict[args.c0]+"),"
	except:
		parser.error("Wrong C0 color")

if(args.c1!=None):
	try:
		OutFile+="S(M1"+ColorDict[args.c1]+"),"
	except:
		parser.error("Wrong C1 color")

if(args.c2!=None):
	try:
		OutFile+="S(M2"+ColorDict[args.c2]+"),"
	except:
		parser.error("Wrong C2 color")

if(args.c3!=None):
	try:
		OutFile+="S(M3"+ColorDict[args.c3]+"),"
	except:
		parser.error("Wrong C3 color")

if(args.l0!=None):
	OutFile+="S(M0(L"+str(args.l0)+")),"
if(args.l1!=None):
	OutFile+="S(M1(L"+str(args.l1)+")),"
if(args.l2!=None):
	OutFile+="S(M2(L"+str(args.l2)+")),"
if(args.l3!=None):
	OutFile+="S(M3(L"+str(args.l3)+")),"

#Draw color test if requested
if(args.ct==True):
	OutFile+="P[10,240],W(S1),W(I0),P[233,89],V[383,89],W(I1),P[383,89],V[533,89],W(I2),P[233,392],V[383,392],W(I3),P[383,392],V[533,392],W(S0),W(I0),P[266,152],V[258,144],[258,111],[266,102],[275,102],[283,111],[283,144],[275,152],[266,152],P[417,152],V[408,144],[408,111],[417,102],[425,102],[433,111],[433,144],[425,152],[417,152],P[266,303],V[258,295],[258,262],[266,253],[275,253],[283,262],[283,295],[275,303],[266,303],P[417,303],V[408,295],[408,262],[417,253],[425,253],[433,262],[433,295],[425,303],[417,303],W(I1),P[337,111],V[346,102],[346,152],P[337,152],V[354,152],P[488,111],V[496,102],[496,152],P[488,152],V[504,152],P[337,262],V[346,253],[346,303],P[337,303],V[354,303],P[488,262],V[496,253],[496,303],P[488,303],V[504,303],W(I2),P[254,186],V[262,177],[279,177],[287,186],[287,194],[279,202],[262,202],[254,211],[254,228],[287,228],P[404,186],V[412,177],[429,177],[437,186],[437,194],[429,202],[412,202],[404,211],[404,228],[437,228],P[254,337],V[262,329],[279,329],[287,337],[287,345],[279,354],[262,354],[254,362],[254,379],[287,379],P[404,337],V[412,329],[429,329],[437,337],[437,345],[429,354],[412,354],[404,362],[404,379],[437,379],W(I3),P[329,186],V[337,177],[354,177],[362,186],[362,194],[354,202],[346,202],P[354,202],V[362,211],[362,219],[354,228],[337,228],[329,219],P[479,186],V[488,177],[504,177],[512,186],[512,194],[504,202],[496,202],P[504,202],V[512,211],[512,219],[504,228],[488,228],[479,219],P[329,337],V[337,329],[354,329],[362,337],[362,345],[354,354],[346,354],P[354,354],V[362,362],[362,370],[354,379],[337,379],[329,370],P[479,337],V[488,329],[504,329],[512,337],[512,345],[504,354],[496,354],P[504,354],V[512,362],[512,370],[504,379],[488,379],[479,370],"

#If "do not draw" argument is not set, draws HPGL drawing
if((args.nd!=True)and(args.f!=None)):
	#Opens a HPGL file specified by user
	try:
		f=open(args.f,"r")
		plotfile=f.read()
		f.close()
	except:
		parser.error("File not found")

	#print (plotfile)
	#Splits HPGL file in an array. Each array member is one command.
	plotfile=plotfile.split(";")
	#print (plotfile)

	#Do a loop for each HPGL command
	for CommandCycle in range(0,len(plotfile)):
		#Pen change command
		if plotfile[CommandCycle][0:2]=="SP":
			if(len(plotfile[CommandCycle])>2):
				#Pens 1,2,3 are used only, because VT125 can only support three colors.
				#All other defaults to 0 - background
				if(int(plotfile[CommandCycle][2:])>3):
					OutFile+=("W(I0),")
				else:
					OutFile+=("W(I"+plotfile[CommandCycle][2:]+"),")

		#Pen Up command
		if plotfile[CommandCycle][0:2]=="PU":
		#	print ("PU")
			MovementMode="h"
			if(len(plotfile[CommandCycle])>2):
				plotfile[CommandCycle]=plotfile[CommandCycle][2:]

		#Pen Down command
		if plotfile[CommandCycle][0:2]=="PD":
		#	print ("PD")
			MovementMode="i"
			if(len(plotfile[CommandCycle])>2):
				plotfile[CommandCycle]=plotfile[CommandCycle][2:]

		#Plot command
		if plotfile[CommandCycle][0:2]=="PA":
			if(MovementMode=="h"):
				#If pen is up - move pixel cursor (Position command)
				MovementCommand="P"
			else:
				#If pen is down - draw a line (Vector command)
				MovementCommand="V"
			PositionArray=(plotfile[CommandCycle][2:]).split(",")
			for PositionPointer in range (0,int(len(PositionArray)/2)):
				#For some reason, Autocad outputs HPGL file as 1 inch=24,9mm not 25,4.
				#That's why coefficient is 0,249
				MovementCommand+="["+(str(int(int(PositionArray[(PositionPointer*2)])*0.249))+","+str(479-int(int(PositionArray[(PositionPointer*2)+1])*0.249))+"],")
			OutFile+=(MovementCommand)

#Exits from ReGIS mode and outputs all data on screen where it's displayed as a graphics.
OutFile+="\x1B\\"

print (OutFile)
