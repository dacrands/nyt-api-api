# Times App API

Provides the back-end for my React/Redux front-end, which features data from the New York Times API. 

## Table of Contents
- [Background](#background)
- [Getting Started](#getStarted)
- [How it works](#how)
- [Hosting](#hosting)


<a name="background"></a>
## Background
I created a front-end application using React and Redux that allows users to interact with data from the New York Times API ([view the repo here](https://github.com/dacrands/times-app)). Unfortunately, the redux actions used to grab the data were making requests directly from NYT API, so people could open up the "Network" tab in dev-tools and see my API key. 

It was obvious I needed some form of back-end, and thus this simple Flask application. This app uses CORS and serves as nothing more than an intermediary between my front-end SPA (Singe Page Application) and the New York Times API.

### Why Flask?
Considering all the time I've spent learning Express, why would I choose Flask for this project?

To be honest the choice was somewhat arbitrary, though some factors may have influenced the decision. First, I knew this app was going to be very minimal, and Flask is a micro-framework. Second, I like writing code in Python and figured this project would me provide me with a small vacation from Javascript.

I am also hosting this application on a rasperry-pi for debugging purposes and because it's cool.

<a name="getStarted"></a>
## Getting Started

### Create a virtualenv
First, create a virtual environment and activate it. For NodeJS folks, you can think of this as `npm init`.
```bash
$ python3 -m venv timesenv
$ source timesenv/bin/activate
(timesenv) $
```

Once your environment is activated, install your dependencies. For Node folks, this is analagous to `npm i`.

```bash
(timesenv) $ pip install requirements.txt
```
Once the packages have been downloaded, let's configure two environment variables. The first, `FLASK_APP`, is the entry point of our application. When we run `flask run`, Flask looks at the value of `FLASK_APP` for the proper file to execute. The second is our `API_KEY` which */config.py* uses so we can access the API-key in the application.

```bash
$ export FLASK_APP=run.py
$ export API_KEY=<yourkey>
```


### Development
Flask comes with a development server built-in,we just need to activate it by running the following:
```bash
$ export FLASK_DEBUG=1
```

