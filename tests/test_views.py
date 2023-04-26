import json
import uuid

import pytest
from django.core.management import call_command
from rest_framework import status
from api.models import User


@pytest.fixture
def create_users():
    users = [
        {'id': uuid.uuid4(), 'name': 'User Test 10', 'email': 'usertest10@email.com'},
        {'id': uuid.uuid4(), 'name': 'User Test 20', 'email': 'usertest20@email.com'},
        {'id': uuid.uuid4(), 'name': 'User Test 30', 'email': 'usertest30@email.com'}
    ]

    for user in users:
        User.objects.create(**user)


@pytest.mark.django_db
class TestListUsersView:
    def test_list_users_view_success(self, client, create_users):
        response = client.get('/test/users/list')

        assert response.status_code == status.HTTP_200_OK
        assert len(response.json()) == 3

    def test_list_users_empty(self, client):
        response = client.get('/test/users/list')

        assert response.status_code == status.HTTP_200_OK
        assert len(response.json()) == 0


@pytest.mark.django_db
class TestUserCreateView:
    def test_create_user(self, client):
        data = {'name': 'User Test 2', 'email': 'testuser2@email.com'}
        response = client.post('/test/users/create', data, format='json')

        assert response.status_code == status.HTTP_201_CREATED
        assert User.objects.count() == 1
        assert User.objects.get().name == 'User Test 2'

    def test_create_user_invalid_data(self, client):
        data = {'name': 'User Test 2'}
        response = client.post('/test/users/create', data, format='json')

        assert response.status_code == status.HTTP_400_BAD_REQUEST


@pytest.mark.django_db
class TestUserUpdateView:
    def test_update_email_user(self, client, create_users):
        user = User.objects.create(id=uuid.uuid4(), name='User to Update', email='userupdate@email.com')
        data = {'user_id': str(user.id), 'email': 'newuser@email.com'}

        client.put('/test/users/update/', data, content_type='application/json')
        user.refresh_from_db()

        assert user.email == data.get('email')
