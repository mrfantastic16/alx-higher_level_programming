# 0x00-python-hello_world

## Resources

* [The Python tutorial(Only the first three chapters)](https://docs.python.org/3/tutorial/index.html)
* [Whetting Your Appetite](https://docs.python.org/3/tutorial/appetite.html)
* [Using the python interpreter](https://docs.python.org/3/tutorial/interpreter.html)
* [How to Use String Formaters in Python3](https://realpython.com/python-f-strings/)
* [Learn to Program](https://www.youtube.com/playlist?list=PLGLfVvz_LVvTn3cK5e6LjhgGiSeVlIRwt)
* [Pycodestyle - style Guide for Python Code](https://pypi.org/project/pycodestyle/)


## Tasks


### 0. Run Python file

mandatory ✅

Write a shell script that runs a python script

The Python file name would be saved in the environment variable $PYFILE

```
guillaume@ubuntu:~/py/0x00$ cat main.py
#!/usr/bin/python3
print("Best School")

guillaume@ubuntu:~/py/0x00$ export PYFILE=main.py
guillaume@ubuntu:~/py/0x00$ ./0-run
Best School
guillaume@ubuntu:~/py/0x00$
```

**Repo:**

- GitHub repository: `alx-higher_level_programming`
- Directory: `0x00-python-hello_world`
- File: `0-run`


### 1. Run Inline

mandatory ✅

Write a shell script that runs python code.

The python code would be saved in the environment variable $PYCODE

```
guillaume@ubuntu:~/py/0x00$ export PYCODE='print(f"Best School: {88+10}")'
guillaume@ubuntu:~/py/0x00$ ./1-run_inline
Best School: 98
guillaume@ubuntu:~/py/0x00$
```

**Repo:**
- GitHub repository: `alx-higher_level_programming`
- Directory: `0x00-python-hello_world`
- File: `1-run_inline`


### 2. Hello, print
mandatory ✅

Write a Python script that prints exactly "Programming is like building a multilingual puzzle, followed by a new line.

Use the function print

```
guillaume@ubuntu:~/py/0x00$ ./2-print.py 
"Programming is like building a multilingual puzzle
guillaume@ubuntu:~/py/0x00$
```

**Repo:**

- GitHub repository: `alx-higher_level_programming`
- Directory: `0x00-python-hello_world`
- File: `2-print.py`



### 3. Print integer
mandatory ✅

Complete this source code in order to print the integer stored in the variable number, followed by Battery street, followed by a new line.

- You can find the source code [here](https://github.com/alx-tools/0x00.py/blob/master/3-print_number.py) 
- The output of the script should be:
  * the number, followed by Battery street,
  * followed by a new line
- You are not allowed to cast the variable number into a string
- Your code must be 3 lines long
- You have to use f-strings [tips](https://realpython.com/python-f-strings/)

```
guillaume@ubuntu:~/py/0x00$ ./3-print_number.py
98 Battery street
guillaume@ubuntu:~/py/0x00$
```

**Repo:**

- GitHub repository: `alx-higher_level_programming`
- Directory: `0x00-python-hello_world`
- File: `3-print_number.py`


### 4. Print float

mandatory 

Complete the source code in order to print the float stored in the variable number with a precision of 2 digits.

- You can find the source code [here](https://github.com/alx-tools/0x00.py/blob/master/4-print_float.py)
- The output of the program should be:
  - Float:, followed by the float with only 2 digits
  - followed by a new line
- You are not allowed to cast number to string
- You have to use f-strings

```
guillaume@ubuntu:~/py/0x00$ ./4-print_float.py
Float: 3.14
guillaume@ubuntu:~/py/0x00$
```

**Repo:**
- GitHub repository: `alx-higher_level_programming`
- Directory: `0x00-python-hello_world`
- File: `4-print_float.py`