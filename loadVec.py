def read(name):
    Lines =   []
    Figures = []
    file = open(f"{name}", "rb")
    data = file.read()
    file.close()
    i = 0
    while len(data)-1>i:
        i+=1
        if data[i-1]==0x01: #0x01 line; 0x02 figure
            colorLine = (int(data[i]), int(data[i+1]), int(data[i+2])); i+=3
            width = int(data[i]); i+=1
            ln = int(data[i]); i+=1
            Lines.append([colorLine, width, []])
            for n in range(ln):
                x = int(data[i]); i+=1
                y = int(data[i]); i+=1
                Lines[-1][2].append((x, y))
        elif data[i-1]==0x02: #0x01 line; 0x02 figure
            color = (int(data[i]), int(data[i+1]), int(data[i+2])); i+=3
            ln = int(data[i]); i+=1
            Figures.append([color, []])
            for _ in range(ln):
                x = int(data[i]); i+=1
                y = int(data[i]); i+=1
                Figures[-1][1].append((x, y))
        else:
            i+=1
    print(Lines, Figures)
    return Lines, Figures

def getHexColor(color):
    return color[0].to_bytes(1, byteorder='big') + color[1].to_bytes(1, byteorder='big') + color[2].to_bytes(1, byteorder='big')

def write(name, Figures = [], Lines = []):
    file = open(f"{name}", "wb")
    
    text = b""
    for f in Figures:
        text += b"\x02" + getHexColor(f[0]) + len(f[1]).to_bytes(1, byteorder='big')
        for i in f[1]:
            text += i[0].to_bytes(1, byteorder='big') + i[1].to_bytes(1, byteorder='big')
    for l in Lines:
        text += b"\x01" + getHexColor(l[0]) + l[1].to_bytes(1, byteorder='big') + len(l[2]).to_bytes(1, byteorder='big')
        for i in l[2]:
            text += i[0].to_bytes(1, byteorder='big') + i[1].to_bytes(1, byteorder='big')
    
    file.write(text)
    file.close()

if __name__=="__main__":
    #write("none.vec", Figures = [[(181, 181, 181), [(1, 0), (2, 2), (0, 2)]]], Lines = [[(0, 0, 0), 58, [(1, 0), (2, 2), (0, 2), (1, 0)]]])
    pass
