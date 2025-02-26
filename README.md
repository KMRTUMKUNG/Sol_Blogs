
# Project SOL_Blogs.

This is a project for Sol Company to facilitate various works and for others to visit the website, see how the company operates, both ongoing projects and completed projects as an example in deciding to give the project to Sol Company to develop.


For Sol members, they can add projects, see the results of the projects that we are responsible for, join and help other projects, add and edit their own information displayed on the website.

This project is developed using Python, Django framework for backend, Django tailwindcss template and preline for frontend, sqlite for database.

# Installation
#### Create pip environment for this project. This project. .gitignore file has been created by this project and specified environment folder to be ignored.

```
    python -m venv { name of env.}

```

#### Activate environment.

 ```
    { name of env.}\Scripts\activate
 ```

#### Install all packages pip with and requirements.txt

```
    pip install -r requirements.txt
```

#### install  node_modules all packages
```
    npm install 
```



#### Migrate to create db.

```
    python manage.py migrate
```
#### Create superuser
```
    python manage.py createsuperuser
```

#### Run tailwindcss process
```
    npm run watch:css
```

#### Run server
```
    python manage.py runserver
```


* Normally, if we install django, we will already have sqlite as default database. But I recommend installing sqlite to be able to use sql command line, it will make us work more efficiently. Link for installing sqlite https://www.sqlitetutorial.net/download-install-sqlite/

* There is a chance that there may be a problem installing django-versatileimagefield package. Follow the instructions that are specified in the manual. https://django-versatileimagefield.readthedocs.io/en/latest/installation.html

