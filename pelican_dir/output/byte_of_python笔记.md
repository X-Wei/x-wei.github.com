Title: A byte of Python 笔记
Date: 2014-04-10
Tags: python
Slug: byte_of_python笔记



据说这本书是最好的入门读物, 况且只有100来页 (减掉前面后面那些扯淡的 不到100页...)

那就用这本书过一下py的基本知识点吧! 看完以后收获不少, 把py涉及的很大一部分都讲到了. 这本书已经是够压缩的了, 不过我还是边看边自己再压缩了一遍(写在zim笔记里). 

我看的是1.20版本, 2004年的, 因为这个版本针对的是py2.x, 作者主页上现在的版本针对的是py3. 另外感觉没必要看中文翻译版, 因为这里用的英语比较简单, 而且有的时候中文翻译反而不如原文表达的恰当.


preface+ch1+ch2
===============

扯淡...

ch3. First Steps
================

* There are two ways of using Python to run your program - using the interactive interpreter prompt or using a source file.



* Anything to the right of the # symbol is a comment.



* **the shebang line** - whenever the first two characters of the source file are ``#!`` followed by the location of a program, this tells your Linux/Unix system that this program should be run with this interpreter when you execute the program.

(Note that you can always run the program on any platform by specifying the interpreter directly on the command line such as the command python helloworld.py .)


* use the built-in help functionality.

or example, run ``help(str)`` - this displays the help for the str class which is used to store all text (strings) that you use in your program.

ch4. The Basics
===============

Literal Constants
-----------------
It is called a literal because it is literal - you use its value literally. ex. number 2, or string "hello".

**number**

* Numbers in Python are of four types - integers, long integers, floating point and complex numbers.

-Examples of floating point numbers (or floats for short) are 3.23 and 52.3E-4. The E notation indicates powers of 10. In this case, 52.3E-4 means 52.3 * 10-4.
-Examples of complex numbers are (-5+4j) and (2.3 - 4.6j)

**string**

* string可以用Single/Double/Triple Quotes括起来



* *escape sequence*: \', \n, \t, 以及在行末作为续行符号



* **raw string**: to specify some strings where no special processing such as escape sequences are handled, then what you need is to specify a raw string by prefixing r or R to the string. 

ex. ``r"Newlines are indicated by \n"``


* unicode text:  prefix u or U. For example, ``u"This is a Unicode string."``

Remember to use Unicode strings when you are dealing with text files, especially when you know that the file will contain text written in languages other than English.


* Strings are immutable:  once you have created a string, you cannot change it.



* String literal concatenation: If you place two string literals side by side, they are automatically concatenated by Python. For example, '``What\'s' 'your name?``' is automatically converted in to ``"What's your name?".``



* Note for Regular Expression Users: Always use raw strings when dealing with regular expressions. Otherwise, a lot of backwhacking may be required. 


Variables
---------

顾名思义就是可以可以变的量...
Unlike literal constants, you need some method of accessing these variables *and hence you give them names*.


* Identifier(标示符)

**Identifiers** are names given to identify something. 
The first character of the identifier must be a letter of the alphabet (upper or lowercase) *or an underscore ('_')*.


* Objects

Python refers to anything used in a program as an object.
Python is **strongly object-oriented** in the sense that everything is an object *including numbers, strings and even functions*.


* Variables are used by just assigning them a value. No declaration or data type definition is needed/used.



* Logical and Physical Lines: Implicitly, Python encourages the use of a single statement per line which makes code more readable. If you want to specify more than one logical line on a single physical line, then you have to explicitly specify this using a semicolon (;)



* explicit line joining: ex. 续行符\;

implicit line joining: ex. 括号...

Indentation
-----------

* Leading whitespace (spaces and tabs) at the beginning of the logical line is used to determine the indentation level of the logical line, which in turn is used to determine the grouping of statements.



* This means that statements which go together must have the same indentation. Each such set of state- ments is called a *block*. 



* Do not use a mixture of tabs and spaces for the indentation as it does not work across different platforms properly. 



ch5. Operators and Expressions
==============================


* **expressions**

An expression can be broken down into *operators* and *operands*. 


* 一些oprators: 

``**, //, <<, >>, &, |, ^, ~, not, and, or``


* Operator Precedence: 优先级的一个表...



* Associativity: 

Operators are usually associated from left to right i.e. operators with same precedence are evaluated in a left to right manner. For example, ``2 + 3 + 4`` is evaluated as ``(2 + 3) + 4``. Some operators like assignment operators have right to left associativity i.e. ``a = b = c`` is treated as ``a = (b = c)``.

ch6. Control Flow
=================


* if

``if-elif-else`` statement: This makes the program easier and reduces the amount of indentation required. 


* There is *no switch statement in Python:* You can use an if..elif..else statement to do the same thing (and in some cases, use a dictionary to do it quickly)



* while

Remember that you can have *an ***else*** clause for the while loop*.


* for

-The ``for..in`` statement is another looping statement which *iterates* over a sequence of objects i.e. go
through each item in a sequence, a *sequence* is just an ordered collection of items.
-optional **else** part  also.


* break

- to break out of a loop statement i.e. stop the execution of a looping statement, even if the loop condition has not become False or the sequence of items has been completely iterated over.
-An important note is that if you break out of a for or while loop, *any corresponding loop else block is ***not*** executed.*


* continue

used to tell Python to skip the rest of the statements in the current loop block and to continue to the *next iteration* of the loop.

ch7. Functions
==============

Functions are reusable pieces of programs. 


* def func_name()



* parameters:

Note the terminology used - the names given in the function definition are called *parameters(行参)* whereas the values you supply in the function call are called *arguments(实参)*.

scope
-----

* local variables:

All variables have the **scope** of the block they are declared in starting from the point of definition of the name.


* **global variables**:

If you want to assign a value to a name defined outside the function, then you have to tell Python that the name is not local, but it is global. We do this using the ``global`` statement. 

Default Argument Values
-----------------------
Default Argument Values默认参数

* You can specify default argument values for parameters by following the parameter name in the function definition with the assignment operator (=) followed by the default value.



* Note that the default argument value should be *immutable.*



* you cannot have a parameter with a default argument value *before* a parameter without a default argument value in the order of parameters declared in the function parameter list.

This is because the values are *assigned to the parameters by position*. For example, ``def func(a, b=5)`` is valid, but ``def func(a=5, b)`` is not valid.


* Keyword Arguments

If you have some functions with many parameters and you want to specify only some of them, then you can give values for such parameters by naming them - this is called keyword arguments - we *use the name (keyword) instead of the position* to specify the arguments to the function.


* return

used to *return* from a function i.e. break out of the function. We can optionally return a value from the function as well.


* return None

-a return statement without a value is equivalent to ``return None``. None is a special type in Python that represents nothingness. For example, it is used to indicate that a variable has no value if it has a value of None.
-Every function implicitly contains a return None statement at the end unless you have written your own return statement.


* pass

the ``pass`` statement is used in Python to indicate an empty block of statements.

DocStrings
----------

* *A string on the first logical line of a function* is the **docstring** for that function (also apply to modules and classes). 

``func.__doc__``


* The convention: a multi-line string where the first line starts with a capital letter and ends with a dot. Then the second line is blank followed by any detailed explanation starting from the third line. 



ch8. Modules
============


* A module is basically **a file*** containing all your functions and variables that you have defined*. 
* To reuse the module in other programs, the filename of the module must have a .py extension.


ex. sys module
--------------

* When Python executes the ``import sys`` statement, it looks for the sys.py module in one of the directores listed in its ``sys.path`` variable. If the file is found, then the statements in the main block of that module is run and then the module is made available for you to use.



* The ``sys.argv`` variable is a list of strings, contains the list of command line arguments i.e. the arguments passed to your program using the command line. 即程序执行时传给的参数列表.



* The ``sys.path`` contains *the list of directory names where modules are imported* from. 

Observe that the first string in sys.path is empty - this empty string indicates that *the current directory* is also part of the sys.path which is same as the ``PYTHONPATH`` environment variable. This means that you can directly import modules located in the current directory. Otherwise, you will have to place your module in one of the directories listed in sys.path .


* Byte-compiled .pyc files

Importing a module is a relatively costly affair.
This .pyc file is useful when you import the module the next time from a different program - it will be much faster since part of the processing required in importing a module is already done. Also, these byte-compiled files are platform-independent. 


* from..import 

If you want to directly import the ``argv`` variable into your program (to avoid typing the ``sys.`` everytime for it), then you can use the ``from sys import argv`` statement.
not recommended...


* ``__name__``

Every Python module has it's ``__name__`` defined and if this is '``__main__``', it implies that the module is being run standalone by the user and we can do corresponding appropriate actions.


* Every Python program is also a module. You just have to make sure it has a .py extension. 


dir() function
--------------

* You can use the built-in dir function to *list the identifiers* that a module defines. The identifiers are the **functions, classes, variables and imported modules** defined in that module.



* When you supply a module name to the dir() function, it returns the list of the names defined in that module. 
* When no argument is applied to it, it returns the list of names defined in the current module.


ch9. Data Structures
====================


* Data structures are structures which can hold some data together. In other words, they are used to store a collection of related data.
* 3 built-in data structures in Python - **list, tuple and dictionary**.


List [a,b,c]
------------

* a data structure that holds an ordered collection of items. 
* a *mutable* data type
* you can add any kind of object to a list including numbers and even other lists.


methods:

* *indexing *operator: ``a_list[1]``
* ``len(a_list)``
* ``a_list.append()``
* ``for..in`` loop to iterate through the items of the list
* ``a_list.sort()``: this method affects the list itself and does not return a modified list
* ``del a_list[0]``


Tuple (a,b,c)
-------------

* Tuples are just like lists except that they are **immutable**
* Tuples are usually used in cases where a statement or a user-defined function can safely assume that the collection of values (i.e. the tuple of values) used will not change.
* can contain another tuple, another list......
* singleton: ``t=(2,) ``(comma is necessary!)
* empth: t=()


methods:

* indexing: a_touple[0]
* len(a_tuple)
* used for output format:

``print '%s is %d years old' % (name, age)``

Dictionary {k1:v1, k2:v2}
-------------------------

* key-value mapping
* you can use only immutable objects (like strings) for the keys of a dictionary but you can use either immutable or mutable objects for the values of the dictionary. (This basically translates to say that you should use only simple objects for keys.)
* 一个dict中的keys不必同样type, values也是! 
* key/value pairs in a dictionary are *not ordered* in any manner.
* instances/objects of the dict class.


methods:

* adding key-value pair by indexing: ``dic[key]=val ``*(overwrite if key already exists!)*
* deleting: ``del dic[key] ``*(KeyError if key doesn't exist!)*
* ``dic.items() ``*返回一个list of tuples*:

    dic.items()
    [(k1,v1), (k2,v2)]
    for k,v in dic.items:
        print k, v


* ``dic.keys() ``*返回keys的list*
* test: 

the ``in`` operator: ``if akey in dic``
or even the ``has_key`` method of the dict class: ``if dic.has_key(k)``

Sequences
---------

* Lists, tuples and strings are examples of sequences
* Two of the main features of a sequence is the **indexing** operation which allows us to fetch a particular item in the sequence directly and the **slicing** operation which allows us to retrieve a slice of the sequence i.e. a part of the sequence.
* The great thing about sequences is that you can access tuples, lists and strings all in the same way!




* indexing(seq can be List or Tuple or String):

seq``[2], seq[-1]``

* slicing

seq``[1:3]`` *(from 1 to 2!)*
``seq[:]`` *(a whole copy of the list)*

References
----------

* What you need to remember is that if you want to make a copy of a list or such kinds of sequences or complex objects (not simple objects such as integers), then you have to use the slicing operation(``list[:]``) to make a copy.
* If you just assign the variable name to another name, both of them will refer to the same object and this could lead to all sorts of trouble if you are not careful.


String
------
methods:

* ``str.startswith('a')`` *return boolean*
* ``str.find(substr)`` *return index of subster or -1 if not found*
* ``substr in str`` *return boolean*
* ``str.join(strseq)`` *use str as delimiter to joint the items in strseq*


ch10. Problem Solving - Writing a Python Script
===============================================

"a program which creates a backup of all my important files"

1st version
-----------

* Run the command using the ``os.system`` function which runs the command as if it was run from the system i.e. in the shell - it returns 0 if the command was successfully, else it returns an error number.


        source = ['/home/swaroop/byte', '/home/swaroop/bin']
        target_dir = '/mnt/e/backup/'
        target = target_dir + time.strftime('%Y%m%d%H%M%S') + '.zip'
        zip_command = "zip -qr '%s' %s" % (target, ' '.join(source))
        if os.system(zip_command) == 0:
            print 'Successful backup to', target
        else:
            print 'Backup FAILED'
    

2nd version
-----------

* using the time as the name of the file within a directory with the current date as a directory within the main backup directory.


        if not os.path.exists(today):
            os.mkdir(today) # make directory
        ...
        target = today + os.sep + now + '.zip'

* ``os.sep`` variable - this gives the directory separator according to your operating system i.e. it will be '/' in Linux, Unix, it will be '\\' in Windows and ':' in Mac OS.


3rd version
-----------

* attaching a user-supplied comment to the name of the zip archive.


        comment = raw_input('Enter a comment --> ')
        if len(comment) == 0: # check if a comment was entered
            target = today + os.sep + now + '.zip'
        else:
            target = today + os.sep + now + '_' + \
            comment.replace(' ', '_') + '.zip'

More Refinements
----------------

* allow extra files and directories to be passed to the script at the command line. We will get these from the sys.argv list and we can add them to our source list using the extend method provided by the list class.
* use of the tar command instead of the zip command. 

One advantage is that when you use the tar command along with gzip, the backup is much faster and the backup created is also much smaller. If I need to use this archive in Windows, then WinZip handles such .tar.gz files easily as well.

``tar = 'tar -cvzf %s %s -X /home/swaroop/excludes.txt' % (target, ' '.join(srcdir))``


* The most preferred way of creating such kind of archives would be using the zipfile or tarfile module respectively.
* "Software is grown, not built"



ch11. Object-Oriented Programming
=================================

fields, methods
---------------

* class: **fields**, **methods**
* Fields are of two types - they can belong to each instance/object of the class or they can belong to the class itself. They are called **instance variables** and **class variables** respectively.
* ou must refer to the variables and methods of the same object using the ``self`` variable only. This is called an *attribute reference*.
* we refer to the class variable as ``ClassName.var`` and not as ``self.var``.


self
----

* Class methods have only one specific difference from ordinary functions - *they must have an extra first name that has to be added to the beginning of the parameter list*, but you do do not give a value for this parameter when you call the method, Python will provide it. 
* create an object/instance of this class using the name of the class followed by a pair of parentheses.


The __init__ method
-------------------

* The ``__init__()`` method is run as soon as an object of a class is instantiated. The method is useful to do any initialization you want to do with your object. 
* analogous to a constructor in C++, C# or Java.
* the same, __``del__()`` method: run when the object is no longer in use and there is no guarantee when that method will be run. If you want to explicitly do this, you just have to use the del statement.
* *All class members (including the data members) are ***public*** and all the methods are ***virtual*** in Python.*
* One exception: If you use data members with names using the double underscore prefix such as ``__privatevar``, Python uses name-mangling to effectively make it a private variable.


Inheritance
-----------

* ex:

        class Teacher(SchoolMember)://
            '''Represents a teacher.'''
            def __init__(self, name, age, salary):
                SchoolMember.__init__(self, name, age)
                self.salary = salary
                print '(Initialized Teacher: %s)' % self.name

* To use inheritance, we specify the base class names in a **tuple** following the class name in the class definition. --*multiple inheritance.*
* the ``__init__`` method of the base class is explicitly called using the ``self`` variable so that we can initialize the base class part of the object. This is very important to remember - *Python does not automatically call the constructor of the base class, you have to explicitly call it yourself.*


ch12. Input/Output
==================

Files
-----

* open and use files for reading or writing by creating an object of the ``file`` class and using its ``read``, ``readline`` or ``write`` methods appropriately to read from or write to the file. Then finally, when you are finished with the file, you call the ``close`` method to tell Python that we are done using the file.


        f = file('poem.txt', 'w') # open for 'w'riting
        f.write(poem) # write text to file
        f.close() # close the file
        f = file('poem.txt') # if no mode is specified, 'r'ead mode is assumed by default
        while True:
            line = f.readline()# This method returns a complete line including the newline character at the end of the line.
            if len(line) == 0: # Zero length indicates EOF
            break
            print line, # Notice comma to avoid automatic newline added by Python
        f.close() # close the file

Pickle
------

* *Python provides a standard module called *``pickle``* using which you can store any Python object in a file and then get it back later intact. This is called storing the object persistently.*
* There is another module called ``cPickle`` which functions exactly same as the ``pickle`` module except that it is written in the C language and is (upto 1000 times) faster. 
* pickling & unpickling:


        import cPickle as p
        f = file(shoplistfile, 'w')
        p.dump(shoplist, f)
        f.close()
        f = file(shoplistfile)
        storedlist = p.load(f)
        print storedlist


* To store an object in a file, first we open a file object in write mode and store the object into the open file by calling the ``dump`` function of the pickle module. This process is called *pickling*.
* Next, we retrieve the object using the ``load`` function of the pickle module which returns the object. This process is called *unpickling*.



ch13. Exceptions
================

Try..Except
-----------

* We can handle exceptions using the ``try..except`` statement. We basically put our usual statements within the try-block and put all our error handlers in the except-block.



* ex


        import sys
        try:
            s = raw_input('Enter something --> ')
        except EOFError:
            print '\nWhy did you do an EOF on me?'
            sys.exit() # exit the program
        except:
            print '\nSome error/exception occurred.'
            # here, we are not exiting the program
        print 'Done'

* The ``except`` clause can handle a single specified error or exception, or a parenthesized list of errors/exceptions. If no names of errors or exceptions are supplied, it will handle all errors and exceptions.
* If any error or exception is not handled, then the default Python handler is called which just stops the execution of the program and prints a message.
* You can also have an ``else`` clause associated with a ``try..catch`` block. The ``else`` clause is executed if no exception occurs.


Raising Exceptions
------------------

* using the ``raise`` statement. 
* You also have to specify the name of the error/exception and the exception object that is to be thrown along with the exception. 
* The error or exception that you can arise should be class which directly or indirectly is a derived class of the ``Error`` or ``Exception`` class respectively.
* ex.


        class ShortInputException(Exception):
            '''A user-defined exception class.'''
            def __init__(self, length, atleast):
                Exception.__init__(self)
                self.length = length
                self.atleast = atleast
        
        try:
            s = raw_input('Enter something --> ')
            if len(s) < 3:
                raise ShortInputException(len(s), 3)#  specify the name of the error/exception and the exception object that is to be thrown 
        
        except EOFError:
            print '\nWhy did you do an EOF on me?'
        except ShortInputException, x:
            print 'ShortInputException: The input was of length %d, \
                        was expecting at least %d' % (x.length, x.atleast)
        else:
            print 'No exception was raised.'

Try..Finally
------------

* What if you were reading a file and you wanted to close the file *whether or not an exception was raised*?
* before the program exits, the finally clause is executed and the file is closed.


ch14. The Python Standard Library
=================================

sys module
----------

* ``sys.argv``

there is always at least one item in the ``sys.argv`` list which is the name of the current program being run and is available as ``sys.argv[0]`` . Other command line arguments follow this item.

* ``sys.exit`` : to exit the running program.


os module
---------

* ``os.getcwd()``

gets the current working directory i.e. the path of the directory from which the curent Python script is working.

* ``os.listdir()``
* ``os.remove()``
* ``os.system()``: run a shell command.
* ``os.linesep``: string gives the line terminator used in the current platform. 
* ``os.path.split()``: returns the directory name and file name of the path.
* ``os.path.isfile()`` and ``os.path.isdir()``


ch15. More Python
=================

Special Methods
---------------

* Generally, special methods are used to mimic certain behavior. 
* For example, if you want to use the ``x[key]`` indexing operation for your class (just like you use for lists and tuples) then just implement the ``__getitem__()`` method and your job is done.
* ``__init__(self, ...)`` 
* ``__del__(self)`` 
* ``__str__(self)`` 

Called when we use the ``print`` statement with the object or when ``str()`` is used.

* ``__lt__(self, other)`` 

Called when the *less than* operator ( < ) is used. Similarly, there are special methods for all the operators (+, >, etc.)

* ``__getitem__(self, key)`` 

Called when x[key] indexing operation is used.

* ``__len__(self)`` 

Called when the built-in ``len()`` function is used for the sequence object.

List Comprehension
------------------

* used to derive a new list from an existing list.
* ex


        listone = [2, 3, 4]
        listtwo = [2*i for i in listone if i > 2]


* Here, we derive a new list by specifying the manipulation to be done (2*i) when some condition is satisfied (if i > 2).


Receiving Tuples and Lists in Functions
---------------------------------------

* receiving parameters to a function as a *tuple* or a *dictionary* using the ``*`` or ``**`` prefix respectively. 
* This is useful when taking variable number of arguments in the function.

``def powersum(power, *args):...``

* Due to the * prefix on the args variable, all extra arguments passed to the function are stored in args as a tuple. If a ** prefix had been used instead, the extra parameters would be considered to be key/value pairs of a dictionary.


Lambda Forms
------------

* A ``lambda`` statement is used to create new function objects and then return them *at runtime*.
* ex. 
    
        def make_repeater(n):
            return lambda s: s * n
        twice = make_repeater(2)
        print twice('word')
        print twice(5)

output:

        $ python lambda.py
        wordword
        10
    

* A ``lambda`` statement is used to create *the function object*.
* Essentially, *the lambda takes a parameter followed by a single expression only which becomes the body of the function and the value of this expression is returned by the new function.* 
* Note that even a print statement cannot be used inside a lambda form, only *expressions*.


The exec and eval statements
----------------------------

* The ``exec`` statement is used to execute Python statements which are stored in a string or file.
* The ``eval`` statement is used to evaluate valid Python expressions which are stored in a string. 


The assert statement
--------------------

* to assert that something is true. 
* For example, if you are very sure that you will have at least one element in a list you are using and want to check this, and raise an error if it is not true, then assert statement is ideal in this situation. 
* When the assert statement fails, an AssertionError is raised.


The repr function or Backticks(`)
---------------------------------

* to obtain a canonical string representation of the object.
* you will have ``eval(repr(object)) == object`` most of the time.
* Basically, the repr function or the backticks are used to obtain a printable representation of the object.
* can control what your objects return for the repr function by defining the __``repr__`` method in your class.

