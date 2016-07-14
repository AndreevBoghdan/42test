import json
from PIL import Image
from django.test import TestCase
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.core.serializers import serialize
from datetime import date
from django.core.files.uploadedfile import SimpleUploadedFile
from django.core.management import call_command
from django.db.models import get_apps, get_models
from StringIO import StringIO
from hello.models import Person, Http_request, Entry
from hello.forms import PersonForm
from hello.templatetags.edit_tag import edit_link

# Create your tests here.


class T1_Tests(TestCase):
    fixtures = ['initial_data.json']

    def test_mainpage_exist(self):
        "testing main page exist"
        response = self.client.get(reverse('hello.views.main'))
        self.assertEquals(response.status_code, 200)

    def test_got_default_database_contact(self):
        "test existig contactin DB default"
        self.assertEquals(Person.objects.count(), 1)
        person = Person.objects.last()
        self.assertEquals(person.name, "Boghdan")
        self.assertEquals(person.last_name, "Andreev")
        self.assertEquals(person.date.strftime("%Y-%m-%d"), "1992-03-01")
        self.assertEquals(person.jubber, "andreevb@khavr.com")
        self.assertEquals(person.skype, "boghdanandreev")

    def test_got_default_database_admin(self):
        "test existig contactin DB default"
        self.assertEquals(User.objects.count(), 1)
        user = User.objects.last()
        self.assertEquals(user.username, "admin")

    def test_mainpage_contains_info(self):
        "testing main page content"
        response = self.client.get(reverse('hello.views.main'))
        person = Person.objects.get()
        self.assertIn(person.name, response.content)
        self.assertIn(person.last_name, response.content)
        self.assertIn(person.email, response.content)
        self.assertIn(person.jubber, response.content)
        self.assertIn(person.skype, response.content)
        S = person.date.strftime("%B %-d, %Y")
        self.assertIn(S, response.content)

    def test_no_info_in_db(self):
        "test case of no info in DB"
        Person.objects.all().delete()
        response = self.client.get(reverse('hello.views.main'))
        self.assertIn(
            "<h2>Sorry, there is no info in DB...</h2>", response.content)


class T3_Tests(TestCase):
    fixtures = ['initial_data.json']

    def setUp(self):
        for i in range(14):
            self.client.get(reverse('hello.views.main'))

    def test_link(self):
        "testing exist of link to requests page"
        response = self.client.get(reverse('hello.views.main'))
        self.assertContains(response,
                            'href="/requests/"')

    def test_requestpage_available(self):
        "test is request page available"
        response = self.client.get(reverse('hello.views.requests'))
        self.assertEquals(response.status_code, 200)

    def test_request_saving(self):
        "testing a number of saved paths and test of reading consequenses"
        request_adresses = Http_request.objects.all()
        self.assertEqual(len(request_adresses), 14)

    def test_read_after_request_page_view(self):
        "test is_read column that shold be true after post"
        request_adresses = Http_request.objects.all()[:10]
        resp = self.client.post(
            reverse('hello.views.requests'),
            HTTP_X_REQUESTED_WITH='XMLHttpRequest'
        )
        self.assertEqual(resp.status_code, 200)
        for elem in request_adresses:
            assert(elem.is_read is True)

    def test_ajax_get_is_success(self):
        "testing info that should be sent as an answer to ajax get"
        resp = self.client.get(
            reverse('hello.views.requests'),
            HTTP_X_REQUESTED_WITH='XMLHttpRequest'
        )
        self.assertEqual(resp.status_code, 200)
        data = json.loads(resp.content)
        requests = Http_request.objects.all()[:10]
        requests = json.loads(serialize('json', requests))
        for elem in data:
            self.assertIn(elem, requests)


class T5_Tests(TestCase):
    fixtures = ['initial_data.json']

    def test_loginpage_available(self):
        "test is login page available"
        response = self.client.get(reverse('django.contrib.auth.views.login'))
        self.assertEquals(response.status_code, 200)

    def test_login(self):
        "testing login"
        args = {'username': 'admin', 'password': 'admin'}
        response = self.client.post(reverse('django.contrib.auth.views.login'),
                                    args)
        self.assertEquals(response.status_code, 302)

    def test_edit_link(self):
            "testing exist of link to requests page"
            args = {'username': 'admin', 'password': 'admin'}
            self.client.post(reverse('django.contrib.auth.views.login'), args)
            response = self.client.get(reverse('hello.views.main'))
            self.assertContains(response,
                                '<a href="/edit/"')
            self.assertContains(response,
                                '<a href="accounts/logout/"')
            self.client.get(reverse('django.contrib.auth.views.logout'))
            response = self.client.get(reverse('hello.views.main'))
            self.assertContains(response,
                                '<a href="/accounts/login/"')

    def test_editpage_available(self):
        "test is edit page available"
        args = {'username': 'admin', 'password': 'admin'}
        self.client.post(reverse('django.contrib.auth.views.login'), args)
        response = self.client.get(reverse('hello.views.edit_person'))
        self.assertEquals(response.status_code, 200)

    def test_post(self):
        """ Testing  request saves changes """
        self.client.login(username="admin", password="admin")
        post = {
            'name': 'Victoria',
            'last_name': 'Prokophuck',
            'date': '1992-08-29',
            'other_contacts': 'contacts',
            'bio': 'bio',
            'email': 'vviicckkyy@gmail.com',
            'jubber': 'vviicckkyy@gmail.com',
            'skype': 'vviicckkyy',
        }
        response = self.client.post(
            reverse('hello.views.edit_person'),
            post)
        self.assertEquals(response.status_code, 302)
        self.client.post(
            reverse('hello.views.edit_person'),
            post,
            HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        person = Person.objects.get(pk=1)
        for field in post.keys():
            value = getattr(person, field)
            if isinstance(value, date):
                value = value.strftime("%Y-%m-%d")
            self.assertEqual(value, post[field])

    def test_resize_image(self):
        """ Testing image save """
        person = Person.objects.get(pk=1)
        photo = open('assets/images/default.png', 'rb')
        data = {
            'name': 'Victoria',
            'last_name': 'Prokophuck',
            'date': '1992-08-29',
            'other_contacts': 'contacts',
            'bio': 'bio',
            'email': 'vviicckkyy@gmail.com',
            'jubber': 'vviicckkyy@gmail.com',
            'skype': 'vviicckkyy',
        }
        photo = SimpleUploadedFile(photo.name,
                                   photo.read())
        form = PersonForm(data, dict(photo=photo), instance=person)
        self.assertTrue(form.is_valid())
        form.save()
        person = Person.objects.get(pk=1)

        self.assertNotEqual(person.photo.url,
                            '/static/images/default.png')
        image_resized = Image.open(person.photo)
        self.assertLessEqual(image_resized.height, 200)
        self.assertLessEqual(image_resized.width, 200)


class EditLinkTest(TestCase):
    fixtures = ['initial_data.json']

    def test_edit_link_tag(self):
        "test exist of edit link"
        person = Person.objects.last()
        self.assertEqual(edit_link(person), '/admin/hello/person/1/')
        self.client.login(username='admin', password='admin')
        response = self.client.get(reverse('hello.views.main'))
        self.assertContains(response, 'href="/admin/hello/person/1/"')

    def test_edit_tag_empty(self):
        "test edit link with no person in DB"
        Person.objects.all().delete()
        self.client.login(username='admin', password='admin')
        response = self.client.get(reverse('hello.views.main'))
        self.assertContains(response, 'href="/admin/"')


class CommandsTest(TestCase):
    """ Test  custom commands """

    def test_models(self):
        """ Test  print_maodel command """
        std_err = StringIO()
        call_command('print_model',
                     stderr=std_err)
        std_err.seek(0)

        for app in get_apps():
            for model in get_models(app):
                objects_count = model.objects.count()
                error_message = ('error: %s: objects: %s\n'
                                 % (model.__name__, objects_count))
                self.assertEqual(std_err.readline(), error_message)


class SignalsTest(TestCase):
    fixtures = ['shipping_fixture.json']

    def test_create(self):
        "test person changes -  creation"
        logs_count = Entry.objects.count()
        pers = {"name": "Barney",
                "last_name": "Steanson",
                "date": "1975-05-07",
                "other_contacts": "",
                "bio": "Oh, please.",
                "email": "awesome@gmail.com",
                "jubber": "legendary@khavr.com",
                "skype": "magic"}
        Person.objects.create(**pers)
        self.assertGreater(Entry.objects.count(), logs_count)

    def test_edit(self):
        "test person changes -  edit"
        test_person = Person.objects.last()
        test_person.bio = 'signature man'
        test_person.save()
        self.assertEqual(Entry.objects.last().action, 'edit')

    def test_delete(self):
        "test person changes -  delete"
        test_person = Person.objects.last()
        test_person.delete()
        self.assertEqual(Entry.objects.last().action, 'delete')


class PriorityTest(TestCase):
    def test_default_priority(self):
        "default priority"
        self.client.get('hello.views.main')
        entry = Http_request.objects.last()
        self.assertEqual(entry.priority, 0)

    def test_priority_ordering(self):
        "test ordering"
        self.client.get(reverse('hello.views.requests'))
        visit = Http_request.objects.last()
        visit.priority = 38
        visit.save()
        for i in range(20):
            self.client.get(reverse('hello.views.main'))
        last = Http_request.objects.all()[:1]
        self.assertEqual(u"/requests/", last[0].path)
