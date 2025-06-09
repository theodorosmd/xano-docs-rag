# Conditional formulas ​


# Conditional formulas ​

Conditional formulas are a way to test for truthiness or falsiness of variables or comparisons and return a different value according to this.


## if ​

`if`
if takes 3 arguments, in order:

`if`
- condition the variable or comparison to test truthiness on
- value1 the value to return if the condition is truthy
- value2 the value to return if the condition is falsy

`condition`
`value1`
`value2`

### Example ​

Here, we're using the if formula with a variable (display modal) as a condition. The formula will test if the varibale is true, and because it's false in this case, it'll return the second value.

`if`
`display modal`
`true`
`false`



## ifEmpty ​

`ifEmpty`

### Use case ​

The ifEmpty formula is used to check if a given value is empty or not.

`ifEmpty`
If the value is empty, it returns a specified fallback value. If the value is not empty, it returns the original value.


### Syntax ​

The basic syntax of the ifEmpty formula is: ifEmpty(first_parameter, second_parameter)

`ifEmpty`
`ifEmpty(first_parameter, second_parameter)`
- The first parameter is the value you want to check.
- The second parameter is the value to return if the first parameter is empty.


### Examples ​

Let's say you want to check if user_input is empty and return "Default Value" if it is, the formula would be: ifEmpty(user_input, "Default Value")

`user_input`
`ifEmpty(user_input, "Default Value")`
- If user_input has a value, the formula will return that value.
- If it is empty, it will return "Default Value".

`user_input`
Here's the ifEmpty formula in action to check if a collection has returned items or not:

`ifEmpty`



## not ​

`not`
The not formula takes a variable or camparison, and return the opposite boolean value.

`not`
Ok, so what does it means? 😆

If a variable or comparison is truthy, it will return false. If a variable or comparison is falsy, it will return true.

`false`
`true`
So, this formula is useful when you need to invert a condition.


### Example ​

In this example, we apply not to the display modal from before, which is false. So the return value is true.

`not`
`display modal`
`false`
`true`


If we take back the example from the if formula, it will now return the first value as the comparison is now not(false), so true.

`if`
`not(false)`
`true`



## switch ​

`switch`
The switch formula takes an expression, then checks its equality with each value and return the matching result.

`switch`

### Example ​

Here, switch takes the variable user location as a an expression, which equals to "USA". It'll then loop over values, match the one which equals "USA" too, and return the matching value, which is Hello from the US 👋".

`switch`
`user location`
`"USA"`
`"USA"`
`Hello from the US 👋"`


