from django import template
from django.contrib.auth.models import Group

# 1. created a templatetags folder at same level as models.py. must be named templatetags
# 2. created empty file called __init__.py
# 3. created this file called whatever I want
# 4. loaded this file in the html using {% load check_group %}
# 5. restarted server

register = template.Library() #it has to say exactly this

@register.filter(name="in_Posters_group") # "in_Posters_group" can be anything.
def in_Posters_group(user):
	return user.groups.filter(name='Posters').exists()

	# this is used in the base generic to make sure only posters can see link to make a post. {% if user|in_Posters_group %}
