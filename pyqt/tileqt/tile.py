from PIL import Image

data = []

def getTile(height, width, row, col, colorA, colorB):
    data = []
    for i in range(row*height):
        for j in range(col*width):
            rowNum = i//height
            colNum = j//width
            if (rowNum+colNum)%2==0:
                data.append(colorA)
            else:
                data.append(colorB)
    return data

if __name__=="__main__":
    height = 25
    width = 25
    row = 15
    col = 15
    colorA = (0,155,155)
    colorB = (255,255,255)
    data = getTile(height, width, row, col, colorA, colorB)
    
    img = Image.new("RGB", (row*height, col*width))
    img.putdata(data)
    img.save("./output/tile.bmp")