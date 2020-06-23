# django_dramatiq_example

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

An example app demonstrating [django_dramatiq][django_dramatiq].


## Setup

### From Original Author
1. Clone the repo, then run `pipenv install`.
1. Run [Redis][redis].
1. Run the web server: `python manage.py runserver`
1. Run the workers: `python manage.py rundramatiq`

### Additions by Manny E. - June 23rd 2020
to build docker images 
1. cd into the root of this app
1. on windows the `setup_env.py` works for me, i did not test it on linux, let me know if you have any issues, this script assumes you have your env in `venv` folder
	* Run `python setup_env.py` to setup your virtual python env
1. activate the Virtual Environment
	* ##### Windows
		1. in cmd run `.\venv\Scripts\activate`
		1. you should see your cmd starts with something like this `(venv) J:\W\python\django_dramatiq_example>`, note the `(venv)` at the begining, that means you entered the virtual env, now you can have fun
	* ##### Linux
		1. in /bin/bash run `source venv/bin/activate`

1. then run `pip install -r req.txt`
1. run `docker build -t threew/dramatiq:1 .` If you choose a different name, make sure to change the image name in the `docker_django.py` file

I have included basic [Redis][redis] image build to get up and running fast.
Run `python docker_redis.py` to build that image.

To exit the virtual environment, just run `deactivate`, this is valid for both linux and windows as far as i know.

## License

django_dramatiq_example is licensed under Apache 2.0.  Please see
[LICENSE][license] for licensing details.


[django_dramatiq]: https://github.com/Bogdanp/django_dramatiq
[redis]: https://redis.io
[license]: https://github.com/Bogdanp/django_dramatiq_example/blob/master/LICENSE
