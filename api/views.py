from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import NoteSerializer
from rest_framework import status
from django.db.models import Q
from .models import Note

@api_view(['GET'])

def getRoutes(request):
    routes = [
        {
            'Endpoint':'/notes/',
            'method' : 'GET',
            'body' : None,
            'description' : 'Returns an array of notes'
        },
        {
            'Endpoint':'/notes/id',
            'method' : 'GET',
            'body' : None,
            'description' : 'Returns a single note'
        },
        {
            'Endpoint':'/notes/create/',
            'method' : 'POST',
            'body' : {'body': ""},
            'description' : 'Creates a note'
        },
        {
            'Endpoint':'/notes/id/update/',
            'method' : 'PUT',
            'body' : {'body':""},
            'description' : 'Updates a note'
        },
        {
            'Endpoint':'/notes/id/delete',
            'method' : 'DELETE',
            'body' : None,
            'description' : 'Deletes a note'
        },
    ]
    return Response(routes)


@api_view(['GET'])
def getNotes(request):
    notes = Note.objects.all()
    serializer = NoteSerializer(notes, many=True)
    return Response(serializer.data, status = 200)


@api_view(['GET'])
def getNote(request ,pk):
    note = Note.objects.get(id = pk)
    serializer = NoteSerializer(note , many = False)
    return Response(serializer.data)

@api_view(['GET'])
def searchNotes(request):

    query = request.query_params.get('query', None)
    if query:
        notes = Note.objects.filter(Q(title__icontains=query))
        serializer = NoteSerializer(notes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        return Response(status=400)


@api_view(['POST'])
def createNote(request):
    data = request.data
    note = Note.objects.create(
        title = data['title'],
        body = data['body']
    )
    serializer = NoteSerializer(note , many = False)
    return Response(serializer.data, status=201)


@api_view(['PUT'])
def updateNote(request , pk):
    data = request.data
    note = Note.objects.get(id = pk)
    serializer = NoteSerializer(note , data = request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def deleteNote(request , pk):
    note = Note.objects.get(id = pk)
    note.delete()
    return Response('Note was deleted !')