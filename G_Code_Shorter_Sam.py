import re

lower_value= 3.440924
upper_value= 14.573949


control_dict= []
linesthaticareabout=[]
lineNumbersThatICareAbout = []


with open("C:\Python\UM2+_magnetTest.py") as f:
       for Line_number, line in enumerate(f):
        regex = re.compile(r'G0\sX\d+\.\d+\sY\d+\.\d+\sZ[0-9][0-9]?\.\d+')
        z_matches = regex.search(line)
        if z_matches is not None:
            line_dict={}
            line_dict ["line_No"] = Line_number + 1
            line_dict["line"]=line
            control_dict.append(line_dict)
            Z_component= line.split()[3]
            Z_number= Z_component[1:]
            linesthaticareabout.append(float(Z_number))


for f in linesthaticareabout:
    if f <= lower_value:
        prev_01 = f
    elif f <= upper_value:
        prev_02 = f


for f in control_dict:
    if str("Z") + str(prev_01) in f["line"] or str("Z") + str(prev_02) in f["line"]:
            lineNumbersThatICareAbout.append(f["line_No"])

        #if result_01 in f["Line"]
        #print f["Line_No"]
        #print f["Line"]

        

print lineNumbersThatICareAbout