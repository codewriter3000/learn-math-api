from django.http import Http404
from django.shortcuts import render
from rest_framework import serializers, status

from rest_framework.views import APIView
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response

from modules.forms import TermForm
from modules.models import Term


# Create your views here.
def create_term(request):
    if request.method == 'GET':
        return render(request, 'modules/create_term.html')


class TermSerializer(serializers.Serializer):
    term = serializers.CharField(max_length=100)
    definition = serializers.CharField()


class TermList(APIView):
    """
    List all terms, or create a new term.
    """
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'modules/term_list.html'

    def get(self, request, format=None):
        terms = Term.objects.all()
        serializer = TermSerializer(terms, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = TermSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TermDetail(APIView):
    """
    Retrieve, update, or delete a term instance.
    """
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'modules/term_details.html'
    def get_object(self, pk):
        try:
            return Term.objects.get(pk=pk)
        except Term.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        term = self.get_object(pk)
        serializer = TermSerializer(term)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        term = self.get_object(pk)
        serializer = TermSerializer(term, data=request.data)
        if term.is_valid():
            serializer.save()
            return Response(serializer.data)

    def delete(self, request, pk, format=None):
        term = self.get_object(pk)
        term.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
