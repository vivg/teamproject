from rest_framework import generics
from .serializers import TeamSerializer
from .models import Member

# Create your views here.
class CreateView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = Member.objects.all()
    serializer_class = TeamSerializer

class DetailsView(generics.RetrieveUpdateDestroyAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = Member.objects.all()
    serializer_class = TeamSerializer
