# README

## New requirements
Flask-WTF  # https://flask-wtf.readthedocs.io/en/stable/

### Flask-WTF is baed on WTF-Forms
https://wtforms.readthedocs.io/en/2.3.x/


Different field types: https://wtforms.readthedocs.io/en/2.3.x/fields/#basic-fields
Different validators: https://wtforms.readthedocs.io/en/2.3.x/validators/#built-in-validators

## Prerequisite 
SECRET_KEY required (https://pinetools.com/random-string-generator)
Add it in pyCharm config run.

## Assignments
* Display name of logged in user in top right corner, or 'Unknown'
* Add new field in form - `age` and save value in `session`.
This field should be positive integer, so IntegerField and NumberRange should be used.
If `age` isn't present in session - display 0.
Test form with missing data, negative values and strings instead of int.
After sending ('user1', 43), we should be redirected to `index` which will display "Hello fasada (32)!"
* Implement logout view which will remove `name` and `age` keys from session
Then link new view to "Log out" button in right top corner.
This should be simple GET function (no form required)
(use del)