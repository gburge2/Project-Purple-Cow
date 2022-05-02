<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-">About</a>
	  <ul>
        <li><a href="#development-tools">Development Tools</a></li>
		<li><a href="#testing-tools">Testing Tools</a></li>
      </ul>
    </li>
    <li>
      <a href="#running-the-project">Running The Project</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#run-the-solution">Run The Solution</a></li>
		<li><a href="#using-the-solution">Using The Solution</a></li>
      </ul>
    </li>
	<li><a href="#future-features">Future Features</a></li>  
	<li><a href="#assumptions-and-limitations">Assumptions and Limitations</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>

<!-- ABOUT -->
## About
This project is a 'proof of concept' for an application alled Project Purple Cow. It is a ReSTFUL Web Application API served on [port 3000](http://127.0.0.1:3000/)
that allows a user to set, retrieve and delete a array of *items* stored in memory. This application can also search for items by id and retrieve, update and delete them. 
The item object has two properties: id and name.  The API has an endpoints on the '/items' resource that reponds to a user's requests. 

<p align="right">(<a href="#top">back to top</a>)</p>

### Development Tools
*[Python](https://www.python.org/)
*[Django](https://www.djangoproject.com/)
*[Docker](https://www.docker.com/)

### Testing Tools
*[Insomnia](https://insomnia.rest/)

<p align="right">(<a href="#top">back to top</a>)</p>

## Running The Project
### Prerequisites
You will need to have Python 3, Django, Docker and GitHub. 
### Run The Solution
1. Clone or download from [Project-Purple-Cow](https://github.com/gburge2/Project-Purple-Cow). Make sure you have master branch checked out/downloaded. 
2. Open command prompt at the root directory or the project. The next steps will all be in the command prompt. 
3. Create virtual environemnt by typing 'python -m venv venv. This will create a folder called 'venv' which will store the virtual environemnt. 
4. Activate the virtual environment by typing 'venv\Scripts\activate.bat'. You should now see (venv) on your command line. 
5. With your virtual environment activated you can now install django. Type 'pip install django'. 
6. To make migrations we type 'python manage.py makemigrations'. 
7. Type 'python manage.py makemigrations core'. 
8. Type 'python manage.py migrate' 
9. Next, we will create the docker image by typing 'docker build --tag python-django .'. You should see the image name appear in the docker desktop app. 
10. Finally we create the docker container by typing 'docker run --publish 3000:3000 python-django'. You should see the container name appear in the docker desktop app.
11. You can now use any web brower and navigate to the address http://localhost:3000/ and you should see the text 'Project Purple Cow' on the webpage. 

# Using the solution

| OPERATION     | ENDPOINT      | Param/Body     | RESPONSE                             |Description                        |
| ------------- |:-------------:| --------------:| -----------------------------------: |-----------------------------------:
| GET           | /             | None           	    | Text                          | Homepage.
| GET           | /items        | None           	    | Array of Items                | Retrieve all items. 
| POST          | /items        | Array of JSON Objects | Array of Items                | Overwrite and set list of item(s). 
| DELETE        | /items        | None                  | Empty Array                   | Delete all item(s). 
| GET           | /items/{id}   | None                  | Single element array of items | Get Item by id. 
| PUT           | /items/{id}   | JSON Object           | Array of Items                | Updates name of item by id. 
| DELETE        | /items/{id}   | None                  | Empty Array                   | Delete Item by id. 
For the Param/Body for the POST operation on the /items endpoint each object in the needs to have a field for name and id. 
For the Param/Body for the PUT operation on the /items/{id} endpoint the JSON object needs to only have a name. 

# Future Features
- [ ] Additional fields to the items object such as person address, phone number, age etc. 
- [ ] Methods to handle Item object's with the same ID number. 
- [ ] User Login.
- [ ] Additional methods to filter items through different fields. 
- [ ] User Interface.  
- [ ] Method to return an alphabetically sorted array of JSON objects.
- [ ] MEthod to return an numerically sorted array of JSON objects. 
- [ ] Website security measures. 

# Assumptions and Limitations
1. Each Item object only has two fields id and name. 
2. The name field in the Item object is a string. 
3. The id field in the Item object is an integer. 
4. Two JSON object's can technically have the same ID number if the user chooses to do this. 
5. This is a ReSTFUL API built with Python and Django. 

# Contact
Grant Burgess - gpburgess1@gmail.com
Project Link - https://github.com/gburge2/Project-Purple-Cow
