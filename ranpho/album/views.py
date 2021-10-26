from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import Http404
from .models import Pic
from .serializers import PicSerializer

# SUAS OUTRAS FUNÇÕES CONTINUAM AQUI


def index (request):
    return render("Oi")

@api_view(['GET', 'POST'])
def api_note_get(request, note_id):
    try:
        pic = Pic.objects.get(id=note_id)
    except Pic.DoesNotExist:
        raise Http404()

    
    serialized_pic = PicSerializer(pic)
    return Response(serialized_pic.data)

@api_view(['GET', 'POST'])

def api_note_post(request):
    if request.method == 'POST':
        new_note_data = request.data
        pic = Pic()
        pic.title = new_note_data['title']
        pic.content = new_note_data['content']
        pic.save()
    
    serialized_pic = PicSerializer(pic)
    return Response(serialized_pic.data)
