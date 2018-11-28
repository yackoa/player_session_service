# flask_sandbox
just a repo to test out and learn flask

**Note** : You would need to know some basic python and a basic idea of what a webservice means

#### pre requisites
 - [github account](https://github.com/)
 - [pycharm](https://www.jetbrains.com/pycharm/)
 - [anaconda](https://www.anaconda.com/download/)
  
**Why did i use anconda?**

i am  a data engineer (well sort off) so its easier for me to use it instead of the other python distributions, because i am more familiar with it.! Feel free to use your own d
 some of the notable distributions are found [here](https://wiki.python.org/moin/PythonDistributions)

####The process 
##### Step 1: Create a project in pycharm
1. From the splash menu or file menu click create new project. [refer](https://www.jetbrains.com/help/pycharm/creating-and-running-your-first-python-project.html)
2. Give a name for the project. Example : flask_tutorial
3. Its reacommended you setup the virtual enviornment by installing Flask.

    
##### Step 1:  Hello world Rest API Style!
1. right click on the project name > new > python file
2. give an name. Example : app.py
3. write the following code in app.py
4. After you write the code, you can use pycharms inbuilt terminal to run the code. You should see a 'Terminal' on the bottom bar. 
5. Type 'python app.py'
6. Go to [http://127.0.0.1:5000/hello](http://127.0.0.1:5000/hello) and you should see the sentence "hello world" Yippe that was simple right ?
```python
from flask import Flask
app = Flask(__name__)

@app.route("/hello")
def print_hello():
    return "hello world"
    
if __name__== '__main__':
    app.run(debug=True) 
```

#### Understanding the code that you just wrote.
##### 1. you instantiated the class by the following line
```python
from flask import Flask
```
This is pretty simple, just like you import any module in python.

##### 2. the weird  variable
Python has special variables called dunder variables. Basically they are variables with trailing and leading double underscores. 
You might have already know one, remember "`__name__`", `__main__`  ? There are many of them eg: `__file__`
Here we use it to let flask know where to look for templates, static files etc.
[Here](https://hackernoon.com/understanding-the-underscore-of-python-309d1a029edc) is a nice read up on dunder variables in python

##### The decorator !
For a nice intro to decorators see this [youtube](https://www.youtube.com/watch?v=FsAPt_9Bf3U) video by [Corey](https://twitter.com/CoreyMSchafer). Please do check out his other videos. They are very easy to understand if you are new to python or  even an expert!
Here `@app.route("/hello")` tells flask to process the requests to `localhost:5000/hello` to trigger our function, ie `print_hello()` and generate the appropriate page.

##### The code in the main block
`app.run(debug=True)`

This code will invoke your  `print_hello()` and also sets the debug mode to True. Its useful to see the way your code executes, but please refrain from using it in production.
