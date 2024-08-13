from rest_framework import permissions, viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from django.shortcuts import get_object_or_404
from .models import Pass, User
from .serializers import PassSerializer, UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-id')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class PassViewSet(viewsets.ModelViewSet):
    queryset = Pass.objects.all()
    serializer_class = PassSerializer
    permission_classes = [permissions.IsAuthenticated]

    @action(detail=True, methods=['get'], url_path='submitData')
    def get_pass_by_id(self, request, pk=None):
        try:
            pass_instance = get_object_or_404(Pass, pk=pk)
            serializer = self.get_serializer(pass_instance)
            return Response({
                "state": 1,
                "message": "Запись успешно получена.",
                "data": serializer.data
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({
                "state": 0,
                "message": f"Ошибка при получении записи: {str(e)}"
            }, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['patch'], url_path='submitData')
    def update_pass(self, request, pk=None):
        try:
            pass_instance = get_object_or_404(Pass, pk=pk)
            if pass_instance.status != 'new':
                return Response({"state": 0, "message": "Редактирование возможно только для записей в статусе 'new'."},
                                status=status.HTTP_400_BAD_REQUEST)

            data = request.data.copy()
            for field in ['fam', 'name', 'otc', 'email', 'phone']:
                data.pop(field, None)

            serializer = self.get_serializer(pass_instance, data=data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({"state": 1, "message": "Запись успешно обновлена.", "data": serializer.data}, status=status.HTTP_200_OK)
            return Response({"state": 0, "message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({
                "state": 0,
                "message": f"Ошибка при обновлении записи: {str(e)}"
            }, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['get'], url_path='submitData')
    def get_passes_by_user_email(self, request):
        try:
            email = request.query_params.get('user__email')
            if not email:
                return Response({"state": 0, "message": "Необходимо указать параметр user__email."}, status=status.HTTP_400_BAD_REQUEST)

            passes = Pass.objects.filter(user__email=email)
            serializer = self.get_serializer(passes, many=True)
            return Response({
                "state": 1,
                "message": "Записи успешно получены.",
                "data": serializer.data
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({
                "state": 0,
                "message": f"Ошибка при получении записей: {str(e)}"
            }, status=status.HTTP_400_BAD_REQUEST)
