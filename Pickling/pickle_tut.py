'''
What is pickling?
Pickling is the process of serializing an object. Serializing means storing the object in the form of binary
representation so it can be saved in our main memory. The object could be of any type. It could be a string, tuple,
or any other sort of object that Python supports. The data is stored in the main memory in a file. While writing
the code for pickling, we open the file in "wb" mode, also known as writing binary mode. So, to use the pickle module,
we have to make a file with the .pkl extension and send it in a dump() function along with the object.
dump() is a built-in function in the Pickle module, made for pickling.
'''

import pickle

## Pickling python object
# py_dict = {'name': 'harry', 'salary': 9000, 'language': 'Hindi'}
# file = 'mydetails.pkl'
# myfile = open(file, 'wb')
# pickle.dump(py_dict, myfile)
# myfile.close()

## How to unpickle an object
file = "mydetails.pkl"
fileobj = open(file, 'rb')
mydetail = pickle.load(fileobj)
print(mydetail)
print(type(mydetail))

'''
Disadvantages:
There are some situations in which pickling is discouraged. For example, when we are working with multiple programming 
    languages, pickle is discouraged.
Pickle has been found slower than its alternatives.
In some cases, it has also shown a few security vulnerabilities.
When we update our program to a newer version, pickled data through the previous version can cause issues
'''