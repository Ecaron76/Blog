from django.contrib.auth import get_user_model
from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse

# Create your models here.

User = get_user_model()


class Category(models.Model):
    name = models.CharField(max_length=36)
    slug = models.SlugField()

    def __str__(self):
        return self.name


def caroussel_view(request):
    # Récupérer les 3 articles les plus récents
    latest_posts = BlogPost.objects.order_by('-created_on')[:3]

    context = {
        'latest_posts': latest_posts
    }

    return render(request, 'caroussel.html', context)
class BlogPost(models.Model):
    title = models.CharField(max_length=255, unique=True, verbose_name="Titre")
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    image = models.ImageField(upload_to='blog/', null=True, blank=True)
    category = models.ManyToManyField(Category)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    description = models.TextField(max_length=150)
    content = models.TextField(blank=True, verbose_name="Contenu")
    last_updated = models.DateTimeField(auto_now=True)
    created_on = models.DateField(blank=True, null=True)
    published = models.BooleanField(blank=False, null=True, verbose_name="Publié")

    class Meta:
        ordering = ['-created_on']
        verbose_name = "Article"

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)

        super().save(*args, **kwargs)

    def author_or_default(self):
        if self.author:
            return self.author.username
        return "L'auteur inconnu"

    def get_categories(self):
        return ", ".join(category.name for category in self.category.all())

    def get_category(self):
        first_category = self.category.first()
        if first_category:
            return first_category.slug
    @staticmethod
    def get_latest_posts():
        return BlogPost.objects.order_by('-created_on')[:3]

    def get_absolute_url(self):
        return reverse('posts:home')



