Title: [Scala MOOC I] Lec0: Getting Started
Date: 2016-06-20
Slug:  progfun1_lec0_setup   
Tags: scala
Series: Functional Programming Principles in Scala
 
[TOC]
 
>Get up and running with Scala on your computer. Complete an example assignment to familiarize yourself with our unique way of submitting assignments.

Tool setup
==========

### IntelliJ
*use worksheet as a better REPL*

### SBT
navigate to the directory of the assignment you are working on, then start ``sbt``. 
(when first running ``sbt``, will take 5~10 minutes to download files...)

#### REPL
type ``console`` to enter scala REPL, hit ``ctrl-d`` to exit REPL. 

#### Compile / run / test

* ``compile``: The compile task will compile the source code of the assignment which is located in the directory ``src/main/scala``.
* ``test``: The directory ``src/test/scala`` contains unit tests for the project. In order to run these tests in sbt, you can use the test command.
* ``run``: If your project has an object with a main method (or an object extending the trait App), then you can run the code in sbt easily by typing run. In case sbt finds multiple main methods, it will ask you which one you'd like to execute.


#### submit
submitting assignments in sbt: 
``submit your@email.com YourSubmissionPassWord``


Scala tutorial
==============

### Classes, Traits, Objects and Packages

#### Classes

Classes in Scala are very similar to classes in Java. They are templates containing fields and methods. Like in Java, classes can be instantiated using the new construct, there can be many “instances” (or “objects”) of the same class.

In Scala there exists **a special kind of class named case classes**. You will learn about case classes during the course.

Classes in Scala **cannot have static members**. You can use *objects* (see below) to achieve similar functionality as with static members in Java.

#### Traits

Traits are like **interfaces** in Java, but they *can also contain concrete members*, i.e. method implementations or field definitions.

#### Objects

Object in Scala are like classes, but for every object definition there is only one single instance. *It is not possible to create instances of objects using new*, instead you can just access the members (methods or fields) of an object using its name.

#### Packages

Adding a statement such as package foo.bar at the top of a file makes the code in a file part of the package foo.bar. You can then do import foo.bar._ to make everything from package foo.bar available in your code. The content of a package can be scattered across many files. If you define a class MyClass in package foo.bar, you can import that specific class (and not anything else from that package) with import foo.bar.MyClass.

*In Scala, everything can be imported, not only class names*. So for instance if you have an object baz in package foo.bar, then import foo.bar.baz._ would import all the members of that object.

### Hello, World! in Scala
In Scala, the main or *entry point method is defined in an object*. An object can be made executable by either adding extending the type ``App`` or by adding a method ``def main(args: Array[String])``.

Here are two ways to define a program which outputs “Hello, World!” in Scala:

	object HelloWorld extends App {
	  println("Hello, World!")
	}

or: 

	object HelloWorld {
	  def main(args: Array[String]) {
	    println("Hello, World!")
	  }
	}


### Source Files, Classfiles and the JVM
Scala source code is stored in text files with the extension ``.scala``. Typically Scala programmers create one source file for each class, or one source file for a class hierarchy: In fact, Scala *allows multiple classes and objects to be defined in the same source file*.


* The name of a Scala source file can be chosen *freely*, but it is recommended to use the name of a class which is defined in that file.
* Package hierarchies should be reflected in directory structure: a source file defining class C in package foo.bar should be stored in a subdirectory as foo/bar/C.scala. Scala does not really enforce this convention, but some tools such as the Scala IDE for eclipse might have problems otherwise.

The scala compiler compiles ``.scala`` source files to ``.class`` files, like the Java compiler. Classfiles are binary files containing machine code for the Java Virtual Machine. In order to run a Scala program, the JVM has to know the directory where classfiles are stored. This parameter is called the “classpath”.

If you are using eclipse or sbt to compile and run your Scala code, you don’t need to do any of the above manually - these tools take care of invoking the Scala compiler and the JVM with the correct arguments.


Scala Style Guide
=================
style checker: <http://www.scalastyle.org/>
(in IntelliJ: You can enable scalastyle in Intellij by selecting Settings->Editor->Inspections, then searching for Scala style inspections.)

1. *Avoid Casts and Type Tests*: Never use isInstanceOf or asInstanceOf - there’s always a better solution.
2. Indentation 
3. *Line Length and Whitespace*
4. *Use local Values to simplify complex Expressions*
5. *Choose meaningful Names for Methods and Values*
6. *Common Subexpressions*
7. *Don’t Copy-Paste Code!: factor out common parts into separate methods instead of copying code around. *
8. *Scala doesn’t require Semicolons*
9. *Don’t submit Code with “print” Statements: the final code should be free of debugging statements.*
10. *Avoid using Return*: often don’t need to use explicit returns. 
11. *Avoid mutable local Variables*: You can often rewrite code that uses mutable local variables to code with helper functions that take accumulators.
12. *Eliminate redundant “If” Expressions*


Cheatsheet
==========
<https://github.com/lampepfl/progfun-wiki/blob/gh-pages/CheatSheet.md>

Example Assignment
==================

### implementation
implement ``max`` and ``sum`` method for ``List[Int]``. 
trick: use recursion. 

    def sum(xs: List[Int]): Int = {
        if (xs.isEmpty) 0
        else xs.head + sum(xs.tail)
    }

    def max(xs: List[Int]): Int = {
        if (xs.isEmpty) throw new java.util.NoSuchElementException()
        max(xs, Int.MinValue)
    }
    def max(xs: List[Int], m: Int): Int = {
        if (xs.isEmpty) m
        else if (xs.head > m) max(xs.tail, xs.head)
        else max(xs.tail, m)
    }


### ScalaTest

* A test suite is simply a collection of individual tests for some specific component of a program. A test suite is created by defining a class which extends the type ``org.scalatest.FunSuite``. When running ScalaTest, it will automatically find this class and execute all of its tests.


You have two options for running this test suite:
- Start the sbt console and run the "``test``" command
- Right-click this file in eclipse and chose "Run As" - "JUnit Test"


* Tests are written using the ``test`` operator which takes two arguments:


- A description of the test. This description has to be unique, no two tests can have the same description. 
- The test body, a piece of Scala code that implements the test 
The most common way to implement a test body is using the method ``assert`` which tests that its argument evaluates to ``true``. So one of the simplest successful tests is the following:

``test("one plus one is two")(assert(1 + 1 == 2))``

In Scala, it is allowed to pass an argument to a method using the block  syntax, i.e. ``{ argument }`` instead of parentheses``(argument)``.
This allows tests to be written in a more readable manner:

    test("one plus one is three?") {
        assert(1 + 1 == 3) // This assertion fails! Go ahead and fix it.
    }

One problem with the previous (failing) test is that ScalaTest will        
only tell you that a test failed, but it will not tell you what was        
the reason for the failure. The output looks like this:                    
                                                                           
	{{{                                                                        
	   [info] - one plus one is three? *** FAILED ***                          
	}}}
                                                                        
                                                                           
This situation can be improved by **using a special equality operator **``===`` instead of ``==`` (this is only possible in ScalaTest). So if you  run the next test, ScalaTest will show the following output:               
                                                                           
	{{{                                                                        
	   [info] - details why one plus one is not three *** FAILED ***           
	   [info]   2 did not equal 3 (ListsSuite.scala:67)                        
	}}}
                                                                        
                                                                           
**We recommend to always use the **``===``** equality operator when writing tests.** 

In order to test the exceptional behavior of a methods, ScalaTest offers the ``intercept ``operation.                                              
                                                                        
In the following example, we test the fact that the method ``intNotZero`` throws an ``IllegalArgumentException`` if its argument is ``0``.     

    def intNotZero(x: Int): Int = {
        if (x == 0) throw new IllegalArgumentException("zero is not allowed")
        else x
      }     
    test("intNotZero throws an exception if its argument is 0") {
        intercept[IllegalArgumentException] {
          intNotZero(0)
        }
      }

It is allowed to have multiple ``assert`` statements inside one test, however it is recommended to write an individual ``test`` statement for every tested aspect of a method.

      test("sum of a few numbers") {
        assert(sum(List(1,2,0)) === 3)
      }
      test("sum of empty list"){
        assert(sum(List())===0)
      }
      test("sum of negative numbers"){
        assert(sum(List(-1,-1,-1)) === -3)
      }

      test("max of a few numbers") {
        assert(max(List(3, 7, 2)) === 7)
      }
      test("max of empty list throws NoSuchElementException"){
        intercept[NoSuchElementException]{
          max(List())
        }
      }


