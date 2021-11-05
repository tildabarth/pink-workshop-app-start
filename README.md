# A Basic Introduction to FastAPI
### A Pink Programming Digital Sunday Workshop

## What we'll do

- 👋 We'll start by building a very simple Hello World application to get a first taste of FastAPI.
- 🏃‍♀️ 👟 Then we'll expand the application and add *routes* and *schemas*. We'll work with two kinds of items: runs and shoes.
- 👀 We'll also have a look at the interactive documentation.
- 🖼️  **Finally, we'll set up a web app to consume our API and display the data.**


## 🚀 Getting started

This is the **second part** of the workshop. See the API project on [Replit](https://replit.com/@tildabarth/pink-workshop-api-start) or [GitHub](https://github.com/tildabarth/pink-workshop-api-start) for initial workshop instructions and additional resources.

### A Minimal Web Application

While FastAPI is built to be "API first", we can also use it to build web apps.<br>
The general structure is the same:
```py
import uvicorn
from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def root():
    return {'message': 'Hello FastAPI'}

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0')
```
But instead of returning a dictionary (that will be converted to JSON), we want to return **HTML**. We can do this with a `HTMLResponse`:
```py
from fastapi.responses import HTMLResponse

...

@app.get('/')
async def root():
    """Say hello."""
    return HTMLResponse('<h1>Hello FastAPI</h1>')

```
We import `HTMLResponse` from `fastapi` and return it with some HTML code as content.<br>
It would be rather cumbersome to build our app like this though. Imagine inserting all HTML code in `main.py`, not very elegant.

### A Primer on Templating
Instead, we can use **templates**. To take full advantage of templating, we also need to use a *templating language*. We're going to use **Jinja2** but there are many alternatives.<br>
You can see the template files in `app/templates`, they're ordinary HTML files with some Jinja2 syntax thrown in.
Below is a very short introduction on how to use Jinja2.
```html
<h1>{{ my_title }}</h1>  <!-- This code will output the value of `my_title` between the heading elements -->

<!-- This code will output three paragraphs with an integer (0-2) -->
{% for i in range(3) %}
    <p>{{ i }}</p>
{% endfor %}
```
The resulting HTML code:
```html
<h1>Hello FastAPI</h1>

<p>0</p>
<p>1</p>
<p>2</p>
````
There's a lot more one can do with Jinja2 but we'll stick with the basics. The templates are already written. Our job is to add the API data.

There are a few things we need to do before we can do that.
- We must let FastAPI know *where* our **templates** are.
- We also need to say *where* we keep our **static files** like images and stylesheets.
- Finally, we need to return a `Jinja2Templates.TemplateResponse` instead of our basic `HTMLResponse`.<br>
This also means that we need to create a `context` dictionary. It's a dictionary with all the keys and values we want to pass to our template. There is one mandatory key: `'requests'`. This **must** be present, and it must be a `fastapi.Request` (which is really a `starlette.requests.Request`). The request is passed in a parameter of the route.

### Getting the Data

When fetching the data from our API, we need to know the URL, including the endpoint. This is a combination of your Replit username and the API project name. Note that your API project server must be running to get a response.<br>

To keep it simple, we'll stick with the excellent Python package `requests`. This is *very* easy to use but lacks `async` support. There are several asynchronous alternatives.<br>

To use `requests`, we import it, call the `get` method (to make a `GET` request), pass in our API url and call `json()` on the response.

```py
import requests

...

response = requests.get(f'{API_BASE_URL}/{endpoint}')
api_data = response.json()
```
Now `api_data` holds the API response data.

### Waiting

We haven't enforced any *rate limits* for our API, but there's always a good idea to *wait* between requests.<br>
We may want our `Run` schema to have a `shoe` object rather than just the `shoe_id`. This could be done in the API, but if not, we can make multiple requests to `/shoes/{id}` based on `shoe_id`.<br>
In that case we want to use `time.sleep` from the Standard Library. Different API:s have different rate limits and rules for how often you may make requests. Let's go with one second:
```py
import time

...

for run in runs:
    shoe_dict = requests.get(f'{API_BASE_URL}/shoes/{run.shoe_id}').json()
    if shoe_dict:
        run.shoe = schemas.Shoe(**shoe_dict)
    time.sleep(1)
```

This may not be the most efficient way to solve this particular problem, but it let's us use the concept of waiting for demonstration purposes.<br>
Note that making requests too often can get you **banned** from making any requests to a site. That includes visiting the site via your browser. Always respect the rules and rate limits of the API/site you're consuming/scraping.

## Web App Project Specific Dependencies

- [Jinja2](https://jinja.palletsprojects.com/en/3.0.x/)
- [requests](https://docs.python-requests.org/en/master/index.html)

## Attributions
This project uses images and icons from the below sources:
- Icons made by <a href="https://www.flaticon.com/authors/good-ware" title="Good Ware">Good Ware</a> from <a href="https://www.flaticon.com" title="Flaticon">www.flaticon.com</a>
- Icons made by <a href="https://www.flaticon.com/authors/iconixar" title="iconixar">iconixar</a> from <a href="https://www.flaticon.com" title="Flaticon">www.flaticon.com</a>
- Icons made by <a href="https://www.freepik.com" title="Freepik">Freepik</a> from <a href="https://www.flaticon.com" title="Flaticon">www.flaticon.com</a>
- Icons made by <a href="" title="Nhor Phai">Nhor Phai</a> from <a href="https://www.flaticon.com/" title="Flaticon">www.flaticon.com</a>
- Photo by <a href="https://unsplash.com/@fitmasu?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Fitsum Admasu</a> on <a href="https://unsplash.com/images/things/health?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>
- Photo by <a href="https://unsplash.com/@hannaeberh?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Hanna Eberhard</a> on <a href="https://unsplash.com/images/things/health?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>
- Photo by <a href="https://unsplash.com/@esdesignisms?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Emma Simpson</a> on <a href="https://unsplash.com/s/photos/running-runner-morning?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>
