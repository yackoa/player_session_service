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
3. write the following code

```python
from flask import Flask
app = Flask(__name__)

@app.route("/hello")
def hello():
    return "hello world"
    
if __name__== '__main__':
    app.run(debug=True) 
```