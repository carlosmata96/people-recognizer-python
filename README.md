# people-recognizer-python
Recognizes a face from an encoded list of faces stored in mongodb
# Register person

> python loadPerson.py john ../johnProfile.png

## Result

<img  src="https://raw.githubusercontent.com/carlosmata96/people-recognizer-python/main/img/johnRegister.png">

# Compare person

> python recognize.py ../unknownPerson.png

## Result

>> [{'name':'john', 'distance': '0.334556'}]

Create with ❤️ by [Carlos Mata](https://github.com/carlosmata96)