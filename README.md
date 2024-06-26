# people-recognizer-python
Recognizes a face from an encoded list of faces stored in mongodb.
<table>
<thead>
<tr>
<th>
<img  src="https://raw.githubusercontent.com/carlosmata96/people-recognizer-python/main/img/mongodb.png">
</th>
<th>
<img width="50%" src="https://raw.githubusercontent.com/carlosmata96/people-recognizer-python/main/img/pythonlogo.png"> 
</th>
<th>
<img  src="https://raw.githubusercontent.com/carlosmata96/people-recognizer-python/main/img/flask_logo.png"> 
</th>
</tr>
</thead>
</table>

---

# Create with
* face-recognition 1.3.0
* pymongo 3.11.1
* dnspython 2.0.0

# Installation
* python3 -m venv ./venv
* source venv/bin/activate
* pip3 install -r requirements.txt
* install driver nvidia 

or
>> source install.sh

# Commands

### loadPerson.py
>> Used to add a new person in mongodb.

### recognize.py
>> Used to compare an image of an unknown person with stored records.

# Parameters of parameter.py

### parameter.py
Parameters to edit before using the commands, contains the connection to the mongo server, database, the collection and the maximum tolerance value to recognize a person.


>URL_MONGO
>> URL connection for connect  recognition system with it respective storage .

---

>DATABASE_NAME 
>> Name of database that container lots of collections to process the different tasks of system.

---

>COLLECTION_NAME 
>> Name of collection used to storing the matrix encoders faces with it respective identification.

---

>TOLERANCE 
>> It's the tolerance accepted to evaluate encoders matrix saved in database.
>> #### When will you realice changes at this value the results of algorithm processing may vary!!.

# Register person

> python loadPerson.py john ../johnProfile.png

## Result

<img  src="https://raw.githubusercontent.com/carlosmata96/people-recognizer-python/main/img/johnRegister.png">

# Compare person

> python recognize.py ../unknownPerson.png

## Result

>> [{'name':'john', 'distance': '0.334556'}]

## Architecture

<img  src="https://raw.githubusercontent.com/carlosmata96/people-recognizer-python/main/img/architecture_design.png"> 


Create with ❤️ by [Carlos Mata](https://github.com/carlosmata96)
