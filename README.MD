Python Gitignore Matcher
======
[![Build status](https://github.com/thehanimo/py-gitignore/actions/workflows/python-ci.yaml/badge.svg)]

A python implementation of a gitignore file path matcher. Based on a .gitignore file, the matcher will output a match if the path is to be ignored. Can be used along with a walker or any directory explorer for ignoring files. Follows the gitignore file path conventions. Based off the [RipGrep gitignore implementation](https://github.com/BurntSushi/ripgrep/tree/master/crates/ignore)

## Features

- **Programming Language**: Python
- **Runtime environment**: Python v3.11.x
- **Testing Framework**: unittest
- **Continuous Integration**: GitHub Actions
- **Static Analysis**: Flake8
- **Code Formatting**: Black
- **Package Manager**: pip
- **License**: MIT License

## Usage

First, install the package using pip

`pip install py_gitignore_2`

Then, create the builder for adding .gitignore files

~~~
from py_gitignore_2 import GitignoreBuilder

builder = GitignoreBuilder(DIRECTORY_ROOT) # add your root for the project
builder.add(GITIGNORE FILE PATH) # add your filepath to the gitignore file
~~~

Then, you can create the matcher. After this, you can pass any path and it will return a Boolean indicating if its ignored.

~~~
matcher = builder.build()
return matcher.match(TEST PATH)
~~~

## Example

To walk through a directory and look at files that arent supposed to be ignored:

~~~
for root, _, files in os.walk(directory):     
        for file in files:
            filepath = os.path.join(root, file)
            if not matcher.match(filepath):
                # Apply the test function if matcher returns False
                test_function(filepath)
            # If matcher returns True, the file is ignored
~~~



### Development
### Unit Testing

```sh
python -m unittest tests/test_gitignore.py
```



