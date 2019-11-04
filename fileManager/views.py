from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
import os

STATIC_PATH = os.path.dirname(__file__) +'/'+'StaticFolder'

@api_view(['GET'])
def index(request):
    return Response(os.listdir(STATIC_PATH))

@api_view(['GET'])
def view(request, id):
    return Response(os.listdir(STATIC_PATH+'/'+str(id)))

@api_view(['GET'])
def create(request, id):
    dirName = STATIC_PATH + '/' +id
    if not os.path.exists(dirName):
        os.mkdir(dirName)
        response = "Directory " + str(id) +  " Created "
    else:    
        response = "Directory " + str(id) + " already exists"
    return Response({"response":response})

@api_view(['DELETE'])
def delete(request, id):
    pathToFile = STATIC_PATH + '/' + str(id)
    print(pathToFile)
    if os.path.exists(pathToFile):
        os.rmdir(pathToFile)
        response = "Directory " + str(id) +  " Deleted "
    else:    
        response = "Directory not exists " + str(id)
    return Response({"response":response})

@api_view(['GET'])
def download(request, id):
    for file in os.listdir(STATIC_PATH):
        if id == file.split('.')[0]: id = file
    path_to_file = STATIC_PATH + '/' + str(id)
    FilePointer = open(path_to_file,"r")
    response = HttpResponse(FilePointer,content_type='application/msword')
    response['Content-Disposition'] = 'attachment; filename=NameOfFile'
    return response