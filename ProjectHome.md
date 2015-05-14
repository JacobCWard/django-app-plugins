Allow 3rd party apps to dynamically insert template inclusions into your apps at pre-defined plugin points. Similar to how Eclipse manages plugins via contributors.

You could think of this as the reverse of the {% block %} or {% include %} tags.

templates/myapp/foo.html:
{% load app\_plugins %}
{% plugin\_point "foo" %}

templates/otherapp/plugins/foo.html:
Anything you want...

templates/thirdapp/plugins/foo.html:
yet another plugin...


foo.html is rendered as:
Anything you want...
yet another plugin...