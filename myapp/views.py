from django.shortcuts import render, redirect
from .models import ImageModel
from PIL import Image, ImageDraw, ImageFont
import uuid 


def copyright_apply(input_path, output_path, text) ->str:
    photo = Image.open(input_path)
    w , h = photo.size
    drawing = ImageDraw.Draw(photo)
    text = f" © {text}"
    font = ImageFont.truetype('arialbi.ttf', 68)
    text_w, text_h = drawing.textsize(text, font)
    pos = w - text_w , (h - text_h) - 50
    c_text = Image.new('RGB' , (text_w, text_h), color="#000000")
    drawing.text((0 , 0) , text , fill="#fff", font = font)

    c_text.putalpha(100)
    photo.paste(c_text , pos , c_text)

    photo.save(f'public/static/{uuid.uuid4()}.png')

    return ''

def index(request):
    if request.method == "POST":
        image = request.FILES['image']
        watermark_text = request.POST.get('watermark_text')
        image = ImageModel.objects.create(image=image, watermark_text=watermark_text)
        copyright_apply(f'public/static/{image.image}', 'public/static/output/', watermark_text)
        return redirect('/')
    return render(request, 'index.html')
