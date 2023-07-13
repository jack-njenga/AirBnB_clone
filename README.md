# AirBnB clone - The console

![](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2018/6/65f4a1dd9c51265f49d0.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20230712%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230712T194425Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=1b84923d0831d6f843b8df5b82bd1b85c9585e323cfd0c3e01fc013b0d922069)

### Requirements
#### Python Scripts
- Allowed editors: vi, vim, emacs
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
- All your files should end with a new line
- The first line of all your files should be exactly #!/usr/bin/python3
- A README.md file, at the root of the folder of the project, is mandatory
- Your code should use the pycodestyle (version 2.8.*)
- All your files must be executable
- The length of your files will be tested using wc
- All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
- All your classes should have a documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)')
- All your functions (inside and outside a class) should have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')
- A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)

#### Python Unit Tests
- Allowed editors: vi, vim, emacs
- All your files should end with a new line
- All your test files should be inside a folder tests
- You have to use the unittest module
- All your test files should be python files (extension: .py)
- All your test files and folders should start by test_
- Your file organization in the tests folder should be the same as your project
- e.g., For models/base_model.py, unit tests must be in: tests/test_models/test_base_model.py
- e.g., For models/user.py, unit tests must be in: tests/test_models/test_user.py
- All your tests should be executed by using this command: python3 -m unittest discover tests
- You can also test file by file by using this command: python3 -m unittest tests/test_models/test_base_model.py
- All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
- All your classes should have a documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)')
- All your functions (inside and outside a class) should have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')
- We strongly encourage you to work together on test cases, so that you don’t miss any edge case

#### Usage
```console

$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  all  count  create  destroy  help  quit  show  update

(hbnb) help all
Print string representation of all or named classes

(hbnb) help create
Create new instance of a class, saves and prints the id

(hbnb) help show
Print string representation of all or named classes

(hbnb) quit
$
```

- layout
![](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2018/6/815046647d23428a14ca.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20230712%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230712T194425Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=7fe2137bf66a5e19a965a6cbd7ac72701fcb5d03f707f860339aa1d3166bf006)

#### Example
```console
$ ./console.py
(hbnb) count User
3
(hbnb) create User
5a211fbb-c161-4d77-8b14-ab694cbaf73f
(hbnb) count User
4
(hbnb) show User 5a211fbb-c161-4d77-8b14-ab694cbaf73f
[User] (5a211fbb-c161-4d77-8b14-ab694cbaf73f) {'id': '5a211fbb-c161-4d77-8b14-ab694cbaf73f', 'created_at': datetime.datetime(2023, 7, 13, 10, 31, 6, 828252), 'updated_at': datetime.datetime(2023, 7, 13, 10, 31, 6, 829057)}
(hbnb) destroy User 5a211fbb-c161-4d77-8b14-ab694cbaf73f
(hbnb) show User 5a211fbb-c161-4d77-8b14-ab694cbaf73f
** no instance found **
(hbnb) count User
3
(hbnb) quit
```
