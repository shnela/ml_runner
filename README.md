# README

## Flask-Bootstrap - ingetration with Flask_WTF
https://pythonhosted.org/Flask-Bootstrap/forms.html

### Flask-WTF is baed on WTF-Forms
https://wtforms.readthedocs.io/en/2.3.x/

### Bootstrap container
https://getbootstrap.com/docs/3.4/css/#overview-container
Show form without container (block content)

### Flask Message Flashing
https://flask.palletsprojects.com/en/1.1.x/quickstart/#message-flashing
Flashed in login -> renders in index.


## Assignments
* Display flash messages as blue [Dismissible alerts](https://getbootstrap.com/docs/3.4/components/#alerts-dismissible)
(class="alert alert-info")
* Add "You've logged out" notification after user loggs out
* Make logout alert yellow with (class="alert alert-warning")
Użyj parametru `category` w funkcji [flash](https://flask.palletsprojects.com/en/1.1.x/api/#flask.flash)
oraz `with_categories` w funkcji [get_flashed_messages](https://flask.palletsprojects.com/en/1.1.x/api/#flask.get_flashed_messages)