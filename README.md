# Chainalysis Take Home:
## A crypto exchange recommendation service

### Getting Started

Live version link: http://ahmed-kamal-chainalysis.azurewebsites.net

To build and run the app, clone this repository to a local directory on a machine with Python 3.X installed. Navigate to the newly cloned repository and activate the virtual environment the app is built in:


**Windows:**
```
venv\Scripts\activate.bat
```


**Unix or MacOS:**
```
. venv/bin/activate
```


Now the app can be run using the command
```
flask run
```

### FAQs

1. #### Are there any sub-optimal choices in the implementation?
    
    There are a couple of things that are lacking in the implementation as it stands right now.

    For starters, the same thread fetches prices from both exchanges. This means our data for the exchanges is not perfectly comparable as there may have been a price update on the first exchange while we were fetching from the second. A better design would have two threads, each fetching data simultaneously from each exchange.

    Second, the "database" here is really just a document on the server. This is not atomic nor does it follow REST principles. The code is set up to simply add a database.py file and call it from the backend in the future. Most NoSQL databases would pair well with the exisiting stack.

2. #### Is any part of it over-designed?
    
    The architecture of the system is fairly straightforward, and not largely over-designed. It can be argued that the code could be compressed into a smaller package, such as consolidating the api_wrapper.py and backend.py files. However, this would reduce the modularity of the code, negatively impacting testing and future extensiblity.

3. #### If the system has to scale to 100 users/second traffic what changes should be made, if any?
    
    To scale up the system, we could do with inserting a load balancer between the application and users. Nginx might be a good fit for this.
    

4. #### What are some other enhancements that could be made?

    The first set of improvements would be to address the sub-optimal choices in (1). Additionally, the UI/UX has room for improvement in its current state.
    A key improvement for future development would be to move the app from a python virtual environment to a docker container.

### Notes on the Stack:

- Python backend
- Flask + Jinja frontend (rendered to HTML/Javascript/CSS, implements Bootstrap framework)
- Hosted as an Azure web app for the live version
