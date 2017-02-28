from django.contrib.contenttypes.models import ContentType
from django.test import TestCase

from core.models import User
from feed.models import CreationEvent
from likes.models import Like
from ugc.models import Post


class CreationEventTestCase(TestCase):
    def setUp(self):
        pass

    def test_event_created(self):
        u = User.objects.create()
        p = Post.objects.create(author=u)
        Like.objects.create(author=u, target=p)

        self.assertEqual(CreationEvent.objects.count(), 2)
        ids = []
        for creation_event in CreationEvent.objects.all():
            ids.append(creation_event.id)
        e1 = CreationEvent.objects.get(pk=ids[0])
        e2 = CreationEvent.objects.get(pk=ids[1])
        self.assertEqual(
            e1.object_content_type_id,
            ContentType.objects.get_for_model(Post).id
        )
        self.assertEqual(
            e2.object_content_type_id,
            ContentType.objects.get_for_model(Like).id
        )

    def tearDown(self):
        pass
