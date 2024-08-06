from rest_framework import permissions, viewsets, status
from rest_framework.response import Response
from .models import Pass, User
from .serializers import PassSerializer, UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-id')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class PassViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows passes to be viewed, edited, and created.
    """
    queryset = Pass.objects.all()
    serializer_class = PassSerializer
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        """
        Custom create method to handle additional logic if needed.
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
