import pytest

from django.test.client import Client
from test.factories import PostFactory

from posts.models import Post


@pytest.mark.django_db
class TestViews:

    def setup_method(self):
        self.client = Client()

    def test_posts_list(self):
        PostFactory.create_batch(5)
        response = self.client.get("/api/posts/")

        assert response.status_code == 200
        assert len(response.data) == 5

    def test_posts_create(self):
        data = {"title": "test", "slug": "test", "text": "test"}
        response = self.client.post("/api/posts/", data=data)
        assert response.status_code == 201

        response = self.client.get("/api/posts/")
        assert response.status_code == 200
        assert len(response.data) == 1