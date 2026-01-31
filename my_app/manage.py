#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
from django.db import models
from django.utils import timezone
from datetime import timedelta


class PostManager(models.Manager):
    def published(self):
        return self.filter(is_published=True)

    def recent(self):
        return self.filter(
            created_at__gte=timezone.now() - timedelta(days=7)
        )

    def with_comments(self):
        return self.filter(comments__isnull=False).distinct()


class CommentManager(models.Manager):
    def for_post(self, post):
        return self.filter(
            content_type__model='post',
            object_id=post.id
        )

    def recent(self):
        return self.filter(
            created_at__gte=timezone.now() - timedelta(hours=24)
        )


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)
    from django.db import models


    class PostManager(models.Manager):
     pass


    class CommentManager(models.Manager):
     pass


if __name__ == '__main__':
    main()
