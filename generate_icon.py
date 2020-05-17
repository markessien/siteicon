from PIL import Image, ImageDraw
 

def generate_icon(text):
    img = Image.new('RGB', (256, 256), color = (73, 109, 137))
    
    d = ImageDraw.Draw(img)
    d.text((10,10), "Hello World", fill=(255,255,0))
    
    img_url = 'avatar.png'
    img.save(img_url)
    return img_url