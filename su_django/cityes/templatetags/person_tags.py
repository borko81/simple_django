from django import template

from cityes.models import Person

register = template.Library()


@register.simple_tag
def total_posts():
    return Person.objects.all().count()


@register.simple_tag
def below_forty():
    return Person.objects.filter(age__lt=40).count()


@register.simple_tag
def under_forty():
    return Person.objects.filter(age__gte=40).count()


@register.simple_tag
def all_person(count=5):
    return Person.objects.all()[:count]

