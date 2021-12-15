# Introduction to OOP

Object Oriented Programming (OOP for short) is the most commonly used **programming paradigm**
in the modern world. It essentially is a paradigm that organizes functionality into the **objects**,
rather than just plain functions.

## An Example

Assume you're a factory that makes every single phone on the planet. Obviously, the phones you're making
will all follow some sort of **blueprint**. If you think about it, a phone (like all objects in the universe)
have both **attributes** and **functions**.

### Attributes

Attributes of an object may include things like _color, size, make, model,_ etc.
Although all objects made from a template will have the same attributes (e.g. in a phone,
all phones have size, color, etc.), the VALUES of these attributes may change from
phone to phone. For example, one phone might be red, one might be blue, etc.

### Functions

Functions are anything the **object does**. For example, some functions in a phone
may be to _call, text, play YouTube, etc_. Unlike attributes, the functions for
every single phone made from the same template will have more or less _the same functions_.
For example, all functions, regardless of color, size, etc. have the ability to call.

### The Phone Template

Now that you know about functions and attributes, here's what the template for
a phone may look like:

- Phone
  - Attributes (change from phone to phone)
    - Color
    - Size
    - Operating System
    - Company
  - Functions (all phones have these)
    - Call
    - Text
    - Watch YouTube

## In The Code
Now, move on to the document on classes and we're going to see how to represent this
template in Python.
