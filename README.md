# guh Programming Language
guh is a programming language that is designed to be easy to learn, read and use. It is a compiled language, and it is interpreted by a python interpreter.

<p align="center">
  <img src="assets/guh.jpg" />
</p>

## Table of Contents
* [Origin](#origin)
* [Features](#features)
* [Usage](#usage)
  * [Example of guh file](#example-of-guh-file)
  * [Commands](#commands)

## Origin
One night I decided to drink my first ever Monster Energy, it was a terrible idea because my body (I don't drink caffeine) immediatly started reacting by shaking and my heart started beating way faster than usual.

It kinda felt like being overclocked but I also felt terrible, I just had to do something demanding to get rid of the energy. So I decided to make a "programming language".

So this was how this abomination is born.

It is pronounced like you are a caveman and you got hit in the head with a rock.

## Features
* Easy to learn and use, you just have to now the characters and what they do.
* Easy to read, it is designed to be read like a book.
* The only three types used are strings and arrays and dictionaries. The advantage of doing this is that it is impossible to overflow a variable.


## Usage
guh files contain mathematical expressions and functions. The compiler will compile the guh file into a json file, and the runner will run the json file.

### Example of guh file:
```guh
func test(x) = 3x + 12

12+3=45
4+test(3)
```
When compiled and ran through the interpreter, it will print out:
```
12+3=45 → 0
4+test(3) → 25
```

### Commands

To run the compiler, run the following command:
```bash
python compiler -h
```

To run the interpreter, run the following command:
```bash
python runner -h
```

## Future
Right now, guh is in a very early stage, and it is not very useful. No idea if I will maintain it or not but below is the features I would like to add to it if I ever come back to it.

* Add more mathematical operations
* Add built-in functions
* Add priority to mathematical operations (yeah right now it is just left to right)
* Bundle project into something you can install and use without cloning
* Error handling, right now it just says "Error" when something goes wrong, I would like a more detailed error message containing at least the line where the error occured.
