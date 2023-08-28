# Python - Web framework

# Objectives

    * What is a Web Framework
    * How to build a web framework with Flask
    * How to define routes in Flask
    * What is a route
    * How to handle variables in a route
    * What is a template
    * How to create a HTML response in Flask by using a template
    * How to create a dynamic template (loops, conditions…)
    * How to display in HTML data from a MySQL database

# Task:

1. Write a script that starts a Flask web application
    * Your web application must be
    * listening on 0.0.0.0, port 5000
        Routes:
            * /: display “Hello HBNB!”
            * /hbnb: display “HBNB”

2. Copy the previous task to a new script that starts a Flask web application
    * Your web application must be listening on 0.0.0.0, port 5000
        Routes:
            * /: display “Hello HBNB!”
            * /hbnb: display “HBNB”
            * /c/<text>: display “C ” followed by the value of the text variable (replace underscore _ symbols with a space )

3. Copy the previous task to a new script that starts a Flask web application
    * Your web application must be listening on 0.0.0.0, port 5000
        Routes:
            /: display “Hello HBNB!”
            /hbnb: display “HBNB”
            /c/<text>: display “C ”, followed by the value of the text variable (replace underscore _ symbols with a space )
            /python/(<text>): display “Python ”, followed by the value of the text variable (replace underscore _ symbols with a space )
            The default value of text is “is cool”

4. Copy the previous task to a new script that starts a Flask web application
    Your web application must be listening on 0.0.0.0, port 5000
        Routes:
            * /: display “Hello HBNB!”
            * /hbnb: display “HBNB”
            * /c/<text>: display “C ”, followed by the value of the text variable (replace underscore _ symbols with a space )
            * /python/(<text>): display “Python ”, followed by the value of the text variable (replace underscore _ symbols with a space )
            * The default value of text is “is cool”
            * /number/<n>: display “n is a number” only if n is an integer

5. Copy the previous task to a new script that starts a Flask web application:
    Your web application must be listening on 0.0.0.0, port 5000
        Routes:
            * /: display “Hello HBNB!”
            * /hbnb: display “HBNB”
            * /c/<text>: display “C ”, followed by the value of the text variable (replace underscore _ symbols with a space )
            /python/(<text>): display “Python ”, followed by the value of the text variable (replace underscore _ symbols with a space )
        The default value of text is “is cool”
            * /number/<n>: display “n is a number” only if n is an integer
            * /number_template/<n>: display a HTML page only if n is an integer:
            * H1 tag: “Number: n” inside the tag BODY

6. Copy the previous task to a new script that starts a Flask web application:
    * Your web application must be listening on 0.0.0.0, port 5000
        Routes:
            * /: display “Hello HBNB!”
            * /hbnb: display “HBNB”
            * /c/<text>: display “C ”, followed by the value of the text variable (replace underscore _ symbols with a space )
            * /python/(<text>): display “Python ”, followed by the value of the text variable (replace underscore _ symbols with a space )
        The default value of text is “is cool”
            * /number/<n>: display “n is a number” only if n is an integer
            * /number_template/<n>: display a HTML page only if n is an integer:
        H1 tag: “Number: n” inside the tag BODY
            * /number_odd_or_even/<n>: display a HTML page only if n is an integer:
        H1 tag: “Number: n is even|odd” inside the tag BODY


