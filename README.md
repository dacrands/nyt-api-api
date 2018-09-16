# Times App API

Provides the back-end for my React/Redux front-end, all based on the New York Times API. 

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
Considering all the time I've spent learning Express, why would I choose Flask?

To be honest the decision was somewhat arbitrary, though some factors may have influenced the decision. First, 

I am also hosting this on a rasperry-pi for debugging and because I can




