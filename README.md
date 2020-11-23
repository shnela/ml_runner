# README

## Jinja filters

## Assignment (Filters)
[truncate doc](https://jinja2docs.readthedocs.io/en/stable/templates.html#truncate)

* Truncate name if longer than 10
* Make sure that we don't display all "admin" forms in list - "Admin", "ADMIN", "adMIn" all should be displayed once.

Tips!:
* You can use `upper` filter when detecting if user is "admin"

* http://127.0.0.1:5000/user/aDmiN/5/ should display "Hello aDmiN (5)!"
* http://127.0.0.1:5000/user/very_long_string_much_longer_than_10_characters/1/ should display "* very_lo..."