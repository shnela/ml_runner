# README

## Request context and `url_for`

## Assignment
* Override `index`'s user_info with `name` and `age` passed as request get argument.
If no such parameter, keep default values.
Use `request.args`.
  * For http://127.0.0.1:5000/?name=chris&age=10 view should render "Hello chris (10)!"
  * For http://127.0.0.1:5000/?age=10 view should render "Hello Mike (10)!"
  * For http://127.0.0.1:5000/?dummy_arg=fasada view should render "Hello Mike (42)!"
  
* Replace all static href from `base.html` with urls rendered with `url_for`