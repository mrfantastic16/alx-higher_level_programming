## Methods
Methods are just functions with accordance with Guido's saying "First class everything"

## The \_\_inti__ Method
The init method is a magic method that is called immediately an instance of a class has been created. It core purpose is to initialize these instances


## Data Abstraction, Data Encapsulation, and Information Hiding

```
Encapsulation = bundling of data with the methods that operate on that data
```

Encapsulation is usually achieved by providing two kinds of methods for attributes (**getter methods** - which return the value of the attribute and **setter methods** - which can be used to change the value of attributes)


**Information Hiding** = Information hiding is the principle that some internal information or data is "hidden" so that it cannot be accidentally changed

**Data Abstraction** = Data Encapsulation + Information Hiding


## \__str\__ and \__repr\__ Methods
The str function magically uses the \__str\__ method of the corresponding data type to change the data to a string. \__repr\__ is similar

## Public, -Protected-, and Private Attributes
- Private attribute should be used only by the owner i.e inside the class definition itself
- Protected (restricted) Attributes may be used, but at your own risk. They should used in some essential conditions
- Public attributes can be and should be freely used


## Properties vs Getters and Setters

Getters(data accessors) and Setter (data mutators) ensure the principle of data encapsulation which is bundling data with method which operate on these datas or data.