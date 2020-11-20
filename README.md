# people-recognizer-python
Recognizes a face from an encoded list of faces stored in mongodb

# Create with
* face-recognition 1.3.0
* pymongo 3.11.1
* dnspython 2.0.0

# Installation
* python3 -m venv ./venv
* source venv/bin/activate
* pip3 install -r requirements.txt

# Commands

### parameter.py
>> parameters to edit before using the commands, contains the connection to the mongo server, database, the collection, and the maximum tolerance to recognize a person

### loadPerson.py
>> Used to add a new person in mongodb

### recognize.py
>> Used to compare an image of an unknown person with stored records.

# Register person

> python loadPerson.py john ../johnProfile.png

## Result

<img  src="https://raw.githubusercontent.com/carlosmata96/people-recognizer-python/main/img/johnRegister.png">

# Compare person

> python recognize.py ../unknownPerson.png

## Result

>> [{'name':'john', 'distance': '0.334556'}]

Create with ❤️ by [Carlos Mata](https://github.com/carlosmata96)
