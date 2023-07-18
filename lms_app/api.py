from django.http import Http404
from .models import Book, Category
from django.http.response import JsonResponse
from rest_framework import status,filters
from rest_framework.decorators import api_view, APIView
from .serializers import BookSerialzier, CategorySerilaizer
from rest_framework.response import Response
from rest_framework import viewsets, mixins, generics
from rest_framework.authentication import BaseAuthentication, TokenAuthentication
from rest_framework.permissions import AllowAny,IsAdminUser, IsAuthenticated, IsAuthenticatedOrReadOnly

def model_no_rest(request):
    book = Book.objects.all()
    response = {
        'books' : list(book.values('id','title'))
    }
    return JsonResponse(response)

@api_view(['GET','POST'])
def FBV_list(request):
    if request.method == 'GET':
        book = Book.objects.all()
        serializer = BookSerialzier(book , many =True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = BookSerialzier(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data , status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET','PUT','DELETE'])
def FBV_id(request, id):


    try:
        book = Book.objects.get(id=id)
    except Book.DoesNotExist:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == "GET":
        serializer = BookSerialzier(book)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        serializer = BookSerialzier(book,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        if request.method == 'DELETE':
            book.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

class CBV_list(APIView):
    def get(self,request):
        if request.method == 'GET':
            book = Book.objects.all()
            serializer = BookSerialzier(book, many = True)
            return Response(serializer.data, status=status.HTTP_200_OK)
    def post(self,request):
        if request.method == 'POST':
            serialzier = BookSerialzier(data=request.data)
            if serialzier.is_valid():
                serialzier.save()
                return Response(serialzier.data, status=status.HTTP_201_CREATED)
            return Response(serialzier.data, status=status.HTTP_400_BAD_REQUEST)


class mixins_list(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    generics.GenericAPIView

):
    queryset = Book.objects.all()
    serializer_class = BookSerialzier

    def get(self, request):
        return self.list(request)
    def post(self,request):
        return self.create(request)
    

class mixins_id(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.GenericAPIView,
):
    queryset = Book.objects.all()
    serializer_class = BookSerialzier

    def get(self, request, id):
        return self.retrieve(request)
    def put(self, request, id):
        return self.update(request)
    def delete(self, request, id):
        return self.destroy(request)
    
    

class CBV_id(APIView):
    def get_object(self, id):
        try:
            return Book.objects.get(id=id)
        except Book.DoesNotExist:
            raise Http404
        
    def get(self, request, id):
        book = self.get_object(id)
        serialzier = BookSerialzier(book)
        return Response(serialzier.data , status=status.HTTP_200_OK)
    def put(self, request, id):
        book = self.get_object(id)
        serializer = BookSerialzier(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data , status=status.HTTP_201_CREATED)
        return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,id):
        book = self.get_object(id)
        book.delete()
        return Response( status=status.HTTP_400_BAD_REQUEST)



class generic_list(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerialzier

class generic_id(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'id'
    queryset = Book.objects.all()
    serializer_class = BookSerialzier


class viewsets_cat(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerilaizer


class viesets(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerialzier
    filter_backends = [filters.SearchFilter]
    search_field = ['title']
    authentication_classes = TokenAuthentication
    permission_classes = IsAuthenticated
