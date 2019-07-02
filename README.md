___

# AirBnB Clone Project

`0x00.AirBnb_Clone` project from Holberton School, it's a project to implement the console which will be the command interpreter. The project has been done in python language. The present project is the first part of the AirBnB clone. The command interpreter will be manipulate data without a visual interface, like in a Shell.

![N|Solid](https://pbs.twimg.com/media/D-WTgbVWkAAUd9W.png)

# The console

Will do the next task, just as it is propused: **create the data model, manage the data: create, update, destroy, read objects via the console (command interpreter), finally, store and persist objects to a file JSON file**
___
### Console Description
> It is to manipulate a storage system. This storage engine will give an
> abstraction between an “object” and “How they are stored and persisted”. From the 
> console code (command interpreter) and from the front-end.
> This abstraction will also allow you to change the type of storage easily without
> updating all of your codebase. The console is a tool to validate the storage
> engine
___

### How to compile
Just because it has been written on python language the compile process is easier than you can imagine, so in a certain way of explanation the python language does the compile process by itself. But, to run it, the console has to be with execution permissions. As the next example:
```
# if doesn't have execution permission use the next command
$ chmod u+x console.py
# Run it in this way
$ ./console.py
```
___

### How to use

 - Run the console.py file: `./console.py`
 - Use the commands `EOF` `quit` `help` `create` `show` `destroy` `update` `all`
___

### In the console is posible to use the commands previously stated:

| command | Meaning |
| --- | --- |
| `EOF` | exit the program |
| `quit` | exit the program |
| `help` | Shows help as documentation |
| `create` | Creates a new instance of BaseModel, saves it (to the JSON file) and prints the id |
| `show` | Prints the string representation of an instance based on the class name and id |
| `destroy` | Deletes an instance based on the class name and id |
| `all` | Prints all string representation of all instances based or not on the class name |
| `update` | Updates an instance based on the class name and id by adding or updating attribute |
___
### Examples:
 - Executing the `console.py` file
```
vagrant@vagrant-ubuntu-trusty-64:~/AirBnB_clone$ ./console.py
(hbnb)
```
 - Using the console command `create`
```
vagrant@vagrant-ubuntu-trusty-64:~/AirBnB_clone$ ./console.py
(hbnb) create User
3a567188-23c2-444d-a1a2-4ae6c175a76b
(hbnb)
```
 - Using the console command 'show'
```
vagrant@vagrant-ubuntu-trusty-64:~/AirBnB_clone$ ./console.py
(hbnb) show User 3a567188-23c2-444d-a1a2-4ae6c175a76b
[User] (3a567188-23c2-444d-a1a2-4ae6c175a76b) {'id': '3a567188-23c2-444d-a1a2-4ae6c175a76b', 'updated_at': datetime.datetime(2019, 7, 2, 22, 11, 12, 967606), 'created_at': datetime.datetime(2019, 7, 2, 22, 11, 12, 967526)}
(hbnb)
```
 - Using the console command `Update`
```
vagrant@vagrant-ubuntu-trusty-64:~/AirBnB_clone$ ./console.py
(hbnb) update User 3a567188-23c2-444d-a1a2-4ae6c175a76b first_name Ricardo
(hbnb) show User 3a567188-23c2-444d-a1a2-4ae6c175a76b
[User] (3a567188-23c2-444d-a1a2-4ae6c175a76b) {'id': '3a567188-23c2-444d-a1a2-4ae6c175a76b', 'updated_at': datetime.datetime(2019, 7, 2, 22, 11, 12, 967606), 'first_name': 'Ricardo', 'created_at': datetime.datetime(2019, 7, 2, 22, 11, 12, 967526)}
(hbnb)
```
___
#### AUTHORS
| Name | Cohort | Social media |
| ---| --- | --- |
| **Paula Gutierrez** | Cohort 8 - Bog | [![N\|Solid](https://www.allininteractive.com/wp-content/uploads/2015/04/twitter.png)](https://twitter.com/AndZapata1) |
| **Ricardo Gutierrez** | Cohort 8 - Bog | [![N\|Solid](https://www.allininteractive.com/wp-content/uploads/2015/04/twitter.png)](https://twitter.com/kyeeh) |
___
