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

mandatory

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

