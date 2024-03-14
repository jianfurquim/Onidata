from django.test import TestCase
from django.contrib.auth import authenticate

from apps.user.models import User


class UserTest(TestCase):
    def setUp(self):
        user1 = User.objects.create_user(
            username='usertest1', first_name='User', last_name='Test 1', email='usertest1@test.com')
        user1.set_password('test1userpass123')
        user1.save()

        user2 = User.objects.create_user(
            username='usertest2', first_name='User', last_name='Test 2', email='usertest2@test.com')
        user2.set_password('test2userpass123')
        user2.save()

        super_user1 = User.objects.create_superuser(
            username='superusertest1', first_name='Super User', last_name='Test 1', email='superusertest1@test.com')
        super_user1.set_password('test1superuserpass123')
        super_user1.save()

        super_user2 = User.objects.create_superuser(
            username='superusertest2', first_name='Super User', last_name='Test 2', email='superusertest2@test.com')
        super_user2.set_password('test2superuserpass123')
        super_user2.save()

    def test_user_creation(self):
        user1 = User.objects.get(username='usertest1')
        user2 = User.objects.get(username='usertest2')

        self.assertEqual(user1.username, 'usertest1')
        self.assertEqual(user1.get_full_name(), 'User Test 1')
        self.assertEqual(user1.email, 'usertest1@test.com')

        self.assertEqual(user2.username, 'usertest2')
        self.assertEqual(user2.get_full_name(), 'User Test 2')
        self.assertEqual(user2.email, 'usertest2@test.com')

    def test_user_authentication(self):
        self.assertIsNotNone(authenticate(username='usertest1', password='test1userpass123'))
        self.assertIsNotNone(authenticate(username='usertest2', password='test2userpass123'))

    def test_superuser_creation(self):
        super_user1 = User.objects.get(username='superusertest1')
        super_user2 = User.objects.get(username='superusertest2')

        self.assertEqual(super_user1.username, 'superusertest1')
        self.assertEqual(super_user1.get_full_name(), 'Super User Test 1')
        self.assertEqual(super_user1.email, 'superusertest1@test.com')

        self.assertTrue(super_user1.is_superuser)
        self.assertTrue(super_user1.is_staff)

        self.assertEqual(super_user2.username, 'superusertest2')
        self.assertEqual(super_user2.get_full_name(), 'Super User Test 2')
        self.assertEqual(super_user2.email, 'superusertest2@test.com')

        self.assertTrue(super_user2.is_superuser)
        self.assertTrue(super_user2.is_staff)

    def test_superuser_authentication(self):
        self.assertIsNotNone(authenticate(username='superusertest1', password='test1superuserpass123'))
        self.assertIsNotNone(authenticate(username='superusertest2', password='test2superuserpass123'))

    def test_user_string_representation(self):
        user1 = User.objects.get(username='usertest1')
        user2 = User.objects.get(username='usertest2')

        self.assertEqual(str(user1), user1.get_full_name())
        self.assertEqual(str(user2), user2.get_full_name())

    def test_superuser_string_representation(self):
        super_user1 = User.objects.get(username='superusertest1')
        super_user2 = User.objects.get(username='superusertest2')

        self.assertEqual(str(super_user1), super_user1.get_full_name())
        self.assertEqual(str(super_user2), super_user2.get_full_name())

