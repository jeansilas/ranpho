from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import Http404
from .models import AlbumTitle, Pic
from .serializers import PicSerializer

# SUAS OUTRAS FUNÇÕES CONTINUAM AQUI

@api_view(['GET', 'POST'])
def index (request):
    return render("Oi")

@api_view(['GET', 'POST'])
def api_pic_get(request, note_id):
    try:
        pic = Pic.objects.get(id=note_id)
    except Pic.DoesNotExist:
        raise Http404()

    
    serialized_pic = PicSerializer(pic)
    return Response(serialized_pic.data)

@api_view(['GET', 'POST'])

def api_pic_post(request):
    if request.method == 'POST':
        new_pic_data = request.data
        pic_album_name = new_pic_data['albumTitle']
        pic_src_img = new_pic_data['content']
        
        print(request)

        if AlbumTitle.objects.filter(albumTitle = pic_album_name).exists():
            t = AlbumTitle.objects.get(albumTitle = pic_album_name)
            
            newPic = Pic(albumTitle=t, content=pic_src_img)
            newPic.save()
            
            serialized_pic = PicSerializer(newPic)
            return Response(serialized_pic.data)

        else:
            newAlbum = AlbumTitle(albumTitle = pic_album_name)
            newAlbum.save()

            # TAREFA: Utilize o title e content para criar um novo Note no banco de dados
            newPic = Pic(albumTitle=newAlbum, content=pic_src_img)
            newPic.save()
    
            serialized_pic = PicSerializer(newPic)
            return Response(serialized_pic.data)
