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
      </ul>
    </li>
	<li><a href="#future-features">Future Features</a></li>        
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>

<!-- ABOUT -->
## About
This project is a 'proof of concept' for an application alled Project Purple Cow. It is a ReSTFUL Web Application API served on [port 3000](http://127.0.0.1:3000/)
that allows a user to set, retrieve and delete and array of *items* stored in memory. The item object has two properties: id and name. 
The API has an endpoint on the '/items' resource that reponds to a user's requests.  

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

# Future Features
- [ ] Additional fields to the items object such as person address, phone number, age etc. 

# Contact
Grant Burgess - gpburgess1@gmail.com
Project Link - https://github.com/gburge2/Project-Purple-Cow
