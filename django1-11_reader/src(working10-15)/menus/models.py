from django.conf import settings
from django.db import models
from django.core.urlresolvers import reverse

from restaurants.models import RestaurantLocation

from django.db.models.signals import pre_save
from .utils import unique_slug_generator


class Item(models.Model):
    # associations
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    restaurant = models.ForeignKey(RestaurantLocation)
    # item stuff
    name = models.CharField(max_length=120)
    contents = models.TextField(help_text='Separate each item by comma')
    excludes = models.TextField(blank=True, null=True, help_text='Separate each item by comma')
    public = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    slug = models.SlugField(null=True, blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):  # get_absolute_url
        # return f"/restaurants/{self.slug}"
        return reverse('menus:detail', kwargs={'pk': self.pk})

    @property
    def title(self):
        return self.name

    class Meta:
        ordering = ['-updated', '-timestamp']

    def get_contents(self):
        return self.contents.split(",")

    def get_excludes(self):
        return self.excludes.split(",")


def rl_pre_save_receiver(sender, instance, *args, **kwargs):
    #instance.category = instance.category.capitalize()
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


pre_save.connect(rl_pre_save_receiver, sender=Item)
