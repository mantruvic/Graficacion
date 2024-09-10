from PIL import Image
#se indica la imagen a redimensionar 
image = Image.open("IMG_27.jpg")
print(f"Original size : {image.size}") # 5464x3640
#redimensionado al tamaño indicado
sunset_resized = image.resize((400, 400))
sunset_resized.save('sunset_400.jpeg')
#redimensionado (Maintain Aspect Ratio)
image.thumbnail((400, 400))
image.save("sunset-aspect.jpeg")
