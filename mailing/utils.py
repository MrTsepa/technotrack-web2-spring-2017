from datetime import datetime, timedelta, time

from ugc.models import Post

from templated_email import send_templated_mail, InlineImage


def send_daily_template_mail(user, day):
    tomorrow = day + timedelta(1)
    day_start = datetime.combine(day, time())
    day_end = datetime.combine(tomorrow, time())
    posts = Post.objects.\
        filter(created__lte=day_end, created__gte=day_start).\
        filter(author__in=user.friends.values_list('user2'))
    import os
    path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'ava.png')
    with open(path, 'r') as fin:
        ava_image = fin.read()
    inline_image = InlineImage(filename="ava.png", content=ava_image)

    send_templated_mail(
        template_name='daily',
        from_email='from@example.com',
        recipient_list=[user.email],
        context={
            'username': user.username,
            'posts': posts,
            'date': day,
            'ava_image': inline_image,
        },
        create_link=True
        # Optional:
        # cc=['cc@example.com'],
        # bcc=['bcc@example.com'],
        # headers={'My-Custom-Header':'Custom Value'},
        # template_prefix="my_emails/",
        # template_suffix="email",
    )
