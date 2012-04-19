from django import template
import time, datetime

def example(value):
    return value

register = template.Library()
register.filter('example', example)