from django.test import TestCase
from django.urls import reverse

from rest_framework.test import force_authenticate


from blog.models import User, Comment, Blog, Author

# Create your tests here.


class AuthTest(TestCase):
    def test_auth(self):
        res = self.client.get(reverse("blog:list_create"))
        self.assertEqual(res.status_code, 200)
        res = self.client.post(reverse("blog:list_create"), {"title":"test", "text":"This is test."})
        self.assertEqual(res.status_code, 403)
        res = self.client.delete(reverse("blog:comment_delete", args=[1]))
        self.assertEqual(res.status_code, 403)
        user = User.objects.create(username='admin', password="12345678")
        self.client.force_login(user)
        res = self.client.delete(reverse("blog:comment_delete", args=[1]))
        self.assertEqual(res.status_code, 404)
        

