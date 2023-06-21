from posts.models import BlogPost


def latest_posts_context(request):
    return {
        'latest_posts': BlogPost.get_latest_posts(),
    }