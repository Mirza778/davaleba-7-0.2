from django.core.management.base import BaseCommand
from faker import Faker
import random
from blog.models import Author, Post, Comment, Image
from django.contrib.contenttypes.models import ContentType

fake = Faker()


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        authors = []
        for _ in range(5):
            authors.append(
                Author.objects.create(
                    name=fake.name(),
                    email=fake.email(),
                    bio=fake.text()
                )
            )

        posts = []
        for _ in range(20):
            post = Post.objects.create(
                author=random.choice(authors),
                title=fake.sentence(),
                content=fake.text(),
                is_published=random.choice([True, False])
            )
            posts.append(post)

            for _ in range(random.randint(2, 3)):
                Image.objects.create(
                    url=fake.image_url(),
                    description=fake.word(),
                    content_object=post
                )

        for author in authors:
            Image.objects.create(
                url=fake.image_url(),
                description="Author image",
                content_object=author
            )

        for _ in range(random.randint(5, 10)):
            Comment.objects.create(
                text=fake.text(),
                content_object=random.choice(posts)
            )

        self.stdout.write(self.style.SUCCESS("Blog data created"))
import time
start = time.time()
Post.objects.bulk_create([
    Post(
        author=random.choice(authors),
        title=fake.sentence(),
        content=fake.text(),
        is_published=True
    ) for _ in range(100)
])
print("Time:", time.time() - start)