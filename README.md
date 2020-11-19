# README

## Jinja templates
[Instrukcja](https://flask.palletsprojects.com/en/1.1.x/quickstart/#rendering-templates

## Assignment (Statements)
* [Statements doc](https://jinja2docs.readthedocs.io/en/stable/templates.html#list-of-control-structures)

### For statement
* [Statements doc - for](https://jinja2docs.readthedocs.io/en/stable/templates.html#for)
* [HTML unordered list doc](https://www.w3schools.com/HTML/html_lists.asp)
* Update: `def hello_from_kwargs(name, amount):`. `name` and `amount` should be obtained from url kwargs.
* For `hello_from_kwargs` create new template which will display `name` and `amount` as `index.html` does.
* Update new template which will display `name` value `anount` times using html list.

Tips!:
* Python loop iterating n times: `for _ in range(n):`
* `amount` passed from kwargs is of type str (must be converted to int `int(amount)`)

### If statement
* [Statements doc - if](https://jinja2docs.readthedocs.io/en/stable/templates.html#if)
* [HTML strong tag doc](https://www.w3schools.com/tags/tag_strong.asp)
* If `name` pased to `hello_from_kwargs` equals `Admin` - display name only once. All other names should work as before.
* Additionally wrap every second name in list with `<strong>This text is important!</strong>`

Tips!:
* use `loop.index` and check modulo 2 to detect even / odd elements