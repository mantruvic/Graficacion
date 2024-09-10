from PIL import Image, ImageDraw, ImageFont

im = Image.open("IMG_27.jpg")
width, height = im.size # 400x266

draw = ImageDraw.Draw(im)
text = "ITSTE"

font = ImageFont.truetype('C:/Windows/Fonts/trebucit.ttf', 20)
""" #textwidth, textheight = draw.textsize(text, font=font)
textwidth, textheight = font.getlength(text)

# calculate new x,y coordinates of the text
x = (width - textwidth)/2
y = (height - textheight)/2 """

# draw watermark in the center
draw.text((0, 0), text, font)

im.save('pillow-watermark.jpg')