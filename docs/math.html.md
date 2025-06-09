# Math formulas ​


# Math formulas ​

Math formulas are a way to do mathematics operations inside your WeWeb formulas.


## average ​

`average`
The average formula takes any number of values, variables of arrays (that are of type Number) and returns the average of all of these values (or the values inside the variables or arrays).

`average`

### Example ​

Here, both examples show the result of the average of the numbers 2, 3, 5 and 3, which is 3.25.




## rollupSum ​

`rollupSum`
This formulas loops over an array of object, and in each object, will take the value for a specific key and sum all of these values.


### Example ​

Here, we use a variable called user orders which equals an array of objects. Let's see its content:

`user orders`
```
[
    {"name": "Quentin", "orders": 3},
    {"name": "Kevin", "orders": 2},
    {"name": "Joyce", "orders": 1},
    {"name": "Damien", "orders": 5}
]
```

`[
    {"name": "Quentin", "orders": 3},
    {"name": "Kevin", "orders": 2},
    {"name": "Joyce", "orders": 1},
    {"name": "Damien", "orders": 5}
]`
We'll tell rollupSum to loop over user orders, take the orders key in each object, and sum all of them. And the sum of 3 + 2 + 1 + 5 is indeed 11.

`rollupSum`
`user orders`
`orders`



## round ​

`round`
This formula will round the value given to it (could be a variable, but it needs to be a number). The precision of this rounding (meaning the number of decimals) can be set as a second parameter, which is zero by default.


### Example ​

In this example, we round the number 3.265 with a precision of zero (meaning to the nearest integer), and then with a precision of 1 (meaning 1 decimal).




## sum ​

`sum`
This formula will sum all the values given to it (they should be all of type number). These values can be multiple variables or an array of numbers.


### Example ​

Here, we'll sum the numbers 2, 3, 5 and 3 to give 13. In the second example, these values are given through a variables which is an array of these values.




## toNumber ​

`toNumber`
The toNumber formula will convert a string to a number, when possible.

`toNumber`
It can work with strings containing integer or decimal numbers. The decimal character has to be a dot (.) as the function is based on English notation.

`.`

### 🔥 Pro tip 🔥 ​

This formula is useful when you need to send a number to your backend, or du computation on numbers, but when the number is cast as a string initially. This can happen when you get the number from another API where it's sent as a string, or when using a value from a form input.


### Example ​

In this example, we'll convert a string to a integer and then another string to a decimal. Watch how strings were converted as the result isn't enclosed in " anymore, meaning it's indeed a number now.

`"`


