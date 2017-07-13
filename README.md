# tasty_search
API end point with web based interface for searching review from data set of ~60k reviews. You can find the live demo [here](http://13.59.179.70) or for the rest api, [here](http://13.59.179.70/api).

### Running locally

Clone this repo
```sh
$ git clone https://github.com/shubham-shrivastava/tasty_search.git
```
Now create the virtualenv of Python3.6 using
```sh
$ virtualenv my_env
```
OR if using conda
```sh
$ conda create --name my_env python=3
```
Now install requirements using pip and run the server

```sh
$ pip install -r requirements.txt
$ python manage.py runserver
```
Your application will now be running at localhost. 

### Framework used
* Django
* Django-Rest

### Load Test Result
* 1 User: 13ms average for 10k sample queries
* 5 User: 20ms average for 10k sample queries