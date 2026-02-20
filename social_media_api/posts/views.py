from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.db.models import Q

from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
from .permissions import IsOwnerOrReadOnly


# =====================================
# POST VIEWSET
# =====================================

class PostViewSet(viewsets.ModelViewSet):

    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer

    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'content']

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


# =====================================
# COMMENT VIEWSET
# =====================================

class CommentViewSet(viewsets.ModelViewSet):

    queryset = Comment.objects.all().order_by('-created_at')
    serializer_class = CommentSerializer

    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


# =====================================
# FEED VIEW
# =====================================

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def feed(request):

    # Users that current user follows
    followed_users = request.user.following.all()


    posts = Post.objects.filter(
        Q(author__in=followed_users) | Q(author=request.user)
    ).select_related('author').order_by('-created_at')

    serializer = PostSerializer(posts, many=True)

    return Response(serializer.data)