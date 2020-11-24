# Integration Flask-WTF with Flask-Bootstrap


We're using [`Flask-WTF`](https://flask-wtf.readthedocs.io/en/stable/quickstart.html#creating-forms)
for generating `LoginForm` in `main.py`.  
We're struggling with displaying it in `login.html`.

Let's integrate `Flask-WTF` with [`Flask-Bootstrap`](https://pythonhosted.org/Flask-Bootstrap/basic-usage.html)

## Why?
### More beautiful
[Bootstrap forms](https://getbootstrap.com/docs/3.3/css/#forms) -
looks nice

### Simpler to use in html
```html
<form method="POST">
  {{ wtf.quick_form(form) }}
</form>
```

But first [wtf macro](https://pythonhosted.org/Flask-Bootstrap/macros.html#macros) is required.
```html
{% import "bootstrap/wtf.html" as wtf %}
```
Add it to `base.html`