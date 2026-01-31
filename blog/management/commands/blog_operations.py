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

