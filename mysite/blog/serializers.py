
from rest_framework import serializers
from rest_framework.authtoken.models import Token

from channels.layers import get_channel_layer

from asgiref.sync import async_to_sync

from blog.models import Blog, Comment, User, Author




class CommentSerializer(serializers.ModelSerializer):
    blog_id = serializers.IntegerField()
    class Meta:
        model = Comment
        fields = ("id", "blog_id", "created", "text")

    def create(self, validated_data):
        inst = super().create(validated_data)
        layer = get_channel_layer()
        async_to_sync(layer.group_send)('all', {
            'type': 'comment',
            'content': {"id": inst.id, **validated_data}
        })
        return inst
    

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ("id", "text", "title", "comment_set", "auth0r")
    
    auth0r = serializers.SerializerMethodField(read_only=True)
    comment_set = CommentSerializer(many=True, read_only=True)

    def get_auth0r(self, obj):
        user = obj.author.user
        return f"{user.first_name} {user.last_name}"

    def create(self, validated_data):
        author = self.context["request"].user.author
        return Blog.objects.create(**validated_data, author=author)


class AuthorSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    token = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "password", "token"]

    def get_token(self, obj):
        token, _ = Token.objects.get_or_create(user=obj)
        return token.key

    def create(self, validated_data):
        u = User.objects.create(username=validated_data.get("username"),
         first_name=validated_data.get("first_name"),
          last_name=validated_data.get("last_name"))
        u.set_password(validated_data.get("password"))
        u.save()
        Author.objects.create(user=u)
        return u

class MeSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username", "first_name", "last_name")

