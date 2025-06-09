# Array formulas ​


# Array formulas ​

These formulas are very useful to manipulate arrays, like changing their content, filtering them, etc.


### 💡 Good to know 💡 ​

These formulas won't replace the array they're using on but will always return a new one. To replace the array by its new value, you should use a workflow to store the returned result as the new content of the array.


## add ​

`add`
This formula will add one or multiple values at the end of an existing array. It's the JavaScript equivalent of push.

`push`

### Example ​

In this example, we have a variable countries which equals to ["France", "USA"], so an array of strings containing the countries where WeWeb employees live. But we're missing some countries! To solve this, we'll use the add formula to add two new countries.

`countries`
`["France", "USA"]`
`add`



## contains ​

`contains`
This formula will check if a value exist in a given array. It always returns a boolean, meaning it will either return true or false.

`true`
`false`

### Example ​

Let's get back to our countries array variable, which now equals ["France", "USA", "Belgium", "Croatia"]. If we use the contains formula with this array and "France", it will return true. With "Canada", it returns false, as Canada isn't in the list of countries.

`countries`
`["France", "USA", "Belgium", "Croatia"]`
`contains`
`"France"`
`true`
`"Canada"`
`false`



## createArray ​

`createArray`
The createArray formula is useful to create a whole array from scratch, without any code. It's the equivalent of writing the whole array in JavaScript.

`createArray`

### Example ​

Let's say we want to create the countries array (containing the places where WeWeb employees live, meaning ["France", "USA", "Belgium", "Croatia"]) in a workflow, without needing to type any JavaScript. To do this, we would write this formula:

`countries`
`["France", "USA", "Belgium", "Croatia"]`



## compare ​

`compare`
This formula will compare that two arrays are equals. Meaning they both have the same values and that their values are in the same order (same index for each). This formula always returns a boolean, which means true or false.

`true`
`false`

### Example ​

If we take our countries array which contain ["France", "USA", "Belgium", "Croatia"], compare will return true or false in these use-cases:

`countries`
`["France", "USA", "Belgium", "Croatia"]`
`compare`
`true`
`false`
- same values, same order -> true

`true`


- same values, different order -> false

`false`


- different values -> false

`false`



## distinct ​

`distinct`
distinct iterates over the values in an array, and will return a new array with only unique values. Meaning that if a value is present twice or more in the array, it will be returned only once.

`distinct`

### Example ​

Let's say we have an array with WeWeb employees names, but we wrote one of them twice by mistake. By using the distinct formula, we're able to correct this mistake.

`distinct`



## filterByKey ​

`filterByKey`
This formula will iterate over an array of objects, and return an array where only the object's with a certain key have a certain value.

It seems hard to understand like that, I know... But check the example and it'll become super clear 😉


### Example ​

Let's say we have an array of users with objects containing their names and role in the web app:

```
[
    {"name": "Quentin", "role": "admin"},
    {"name": "Joyce", "role": "normal"},
    {"name": "Aurélie", "role": "admin"},
    {"name": "Kévin", "role": "normal"}
]
```

`[
    {"name": "Quentin", "role": "admin"},
    {"name": "Joyce", "role": "normal"},
    {"name": "Aurélie", "role": "admin"},
    {"name": "Kévin", "role": "normal"}
]`
We want to filter this array to only have users who are admins. We can do this easily with the filterByKey formula:

`filterByKey`


Learn more about the filterByKey formula in this video tutorial.

`filterByKey`

## findIndex ​

`findIndex`
findIndex, when given and array and a value, will find the index in the array of the first element which equals the given value. If the value isn't found, it will return -1. It's equivalent to JavaScript's indexOf.

`findIndex`
`-1`
`indexOf`
🔥 Pro tip 🔥

Array indexes begin at 0, not 1.


### Example ​

If we take the countries array, which includes ["France", "USA", "Belgium", "Croatia"], it will return 2 when we use findIndex for "Belgium", -1 for "Germany" as it's not in the array.

`countries`
`["France", "USA", "Belgium", "Croatia"]`
`2`
`findIndex`
`"Belgium"`
`-1`
`"Germany"`



## findIndexByKey ​

`findIndexByKey`
This formula is equivalent to the findIndex formula but for arrays of objects. It'll return the index of the first object in the array whose key is equal to value.

`findIndex`

### Example ​

Let's get back to our array of users with objects containing their names and role in the web app:

```
[
    {"name": "Quentin", "role": "admin"},
    {"name": "Joyce", "role": "normal"},
    {"name": "Aurélie", "role": "admin"},
    {"name": "Kévin", "role": "normal"}
]
```

`[
    {"name": "Quentin", "role": "admin"},
    {"name": "Joyce", "role": "normal"},
    {"name": "Aurélie", "role": "admin"},
    {"name": "Kévin", "role": "normal"}
]`
If we try to find the first object whose "role" equals to "normal", we'll get the index 1 (the second object). We'll get the index 2 to match on "name" equals "Aurélie" and -1 when matching on "John" as this name doesn't exist in the array.

`"role"`
`"normal"`
`1`
`2`
`"name"`
`"Aurélie"`
`-1`
`"John"`



## getByIndex ​

`getByIndex`
This formula will return an element in a array at a specific index.


### Example ​

Let's get back to our array of users with objects containing their names and role in the web app:

```
[
    {"name": "Quentin", "role": "admin"},
    {"name": "Joyce", "role": "normal"},
    {"name": "Aurélie", "role": "admin"},
    {"name": "Kévin", "role": "normal"}
]
```

`[
    {"name": "Quentin", "role": "admin"},
    {"name": "Joyce", "role": "normal"},
    {"name": "Aurélie", "role": "admin"},
    {"name": "Kévin", "role": "normal"}
]`
If we use getByIndex on the second index, we'll get back Aurélie's object.

`getByIndex`



## groupBy ​

`groupBy`
groupBy, when given an array of objects, will return a new array where objects are grouped by their value for a given key.

`groupBy`

### Example ​

Again, we go back to our array of users with objects containing their names and role in the web app:

```
[
    {"name": "Quentin", "role": "admin"},
    {"name": "Joyce", "role": "normal"},
    {"name": "Aurélie", "role": "admin"},
    {"name": "Kévin", "role": "normal"}
]
```

`[
    {"name": "Quentin", "role": "admin"},
    {"name": "Joyce", "role": "normal"},
    {"name": "Aurélie", "role": "admin"},
    {"name": "Kévin", "role": "normal"}
]`
Let's say we want to regroup them by role type (admins together and normal users together). We can use the groupBy formula applied on the "role" key for this.

`groupBy`
`"role"`



## join ​

`join`
This formula will join all the elements of an array into a string, separating them by a separator (optional, , by default). It's equivalent to JavaScript's join.

`,`
`join`

### Example ​

Say we want to write a string telling people where WeWeb employees live, using the countries array which equals to ["France", "USA", "Belgium", "Croatia"]. We can easily do this with string concatenation and join.

`countries`
`["France", "USA", "Belgium", "Croatia"]`
`join`



## length ​

`length`
It will return the length of an array, meaning the number of items inside it. Same as JavaScript's length.

`length`

### Example ​

Using it again on countries which is ["France", "USA", "Belgium", "Croatia"], length will return 4 as there's four countries in this array.

`countries`
`["France", "USA", "Belgium", "Croatia"]`
`4`



## lookup ​

`lookup`
Given an array of objects, this formula will return the first object where the key equals to a value. The key is optional, and equals "id" by default. It's equivalent of using getByIndex and findByIndex together.

`"id"`
`getByIndex`
`findByIndex`
💡 Good to know 💡

This formula is very useful to link two arrays together when they are linked by a one-to-one relationship or one-to-many relationship in a database. One example is when you want to link two different Airtable records which are also linked by a lookup inside Airtable.


### Example ​

Let's say, that in our users array, we want to find back the one for Aurélie. We can do this using the lookup formula.

`users`
`lookup`
As a reminder, here the array:

```
[
    {"name": "Quentin", "role": "admin"},
    {"name": "Joyce", "role": "normal"},
    {"name": "Aurélie", "role": "admin"},
    {"name": "Kévin", "role": "normal"}
]
```

`[
    {"name": "Quentin", "role": "admin"},
    {"name": "Joyce", "role": "normal"},
    {"name": "Aurélie", "role": "admin"},
    {"name": "Kévin", "role": "normal"}
]`


Also, small example with getByIndex used with findByIndex.

`getByIndex`
`findByIndex`



## lookupArray ​

`lookupArray`
Same as lookup, but will match an array of values and return all the objects where the value is in the array of values for a given key.

`lookup`
🔥 Pro tip 🔥

This formula is very useful to link two arrays together when they are linked by a many-to-many relationship in a database. One example is when you want to link more than two different Airtable records which are linked by a lookup inside Airtable.


### Example ​

Let's say we improve our users array with a new member, Raphael, who's a "superAdmin":

`users`
`"superAdmin"`
```
[
    { "name": "Quentin", "role": "admin" },
    { "name": "Joyce", "role": "normal" },
    { "name": "Aurélie", "role": "admin" },
    { "name": "Kévin", "role": "normal" },
    { "name": "Raphael", "role": "superAdmin" }
]
```

`[
    { "name": "Quentin", "role": "admin" },
    { "name": "Joyce", "role": "normal" },
    { "name": "Aurélie", "role": "admin" },
    { "name": "Kévin", "role": "normal" },
    { "name": "Raphael", "role": "superAdmin" }
]`
If we wanted to get only users that are either admins or super admins, we would use the lookupArray formula.

`lookupArray`



## map ​

`map`
Given an array of objects, this formula will return an array with only the selected key(s) from each object.


### Example ​

Again, we take our users array of objects:

`users`
```
[
    { "name": "Quentin", "role": "admin" },
    { "name": "Joyce", "role": "normal" },
    { "name": "Aurélie", "role": "admin" },
    { "name": "Kévin", "role": "normal" },
    { "name": "Raphael", "role": "superAdmin" }
]
```

`[
    { "name": "Quentin", "role": "admin" },
    { "name": "Joyce", "role": "normal" },
    { "name": "Aurélie", "role": "admin" },
    { "name": "Kévin", "role": "normal" },
    { "name": "Raphael", "role": "superAdmin" }
]`
If we wanted to get an array of the users' names only, we would use the map formula like so:

`map`



## merge ​

`merge`
Given two or more arrays, the merge formula will return a single array containing all the former arrays.

`merge`

### Example ​

Let's say we have two arrays with these values:

```
// countries array
[
    "France",
    "USA",
    "Belgium",
    "Croatia"
]

// countries2 array
[
    "Germany",
    "India",
    "Japan"
]
```

`// countries array
[
    "France",
    "USA",
    "Belgium",
    "Croatia"
]

// countries2 array
[
    "Germany",
    "India",
    "Japan"
]`
The result of merging those two arrays will give a bigger array containing all the countries:




## prepend ​

`prepend`
The prepend formula adds one or more values at the beginning of a given array.

`prepend`

### Example ​

Let's say we have a countries array with the following values:

`countries`
```
// countries array
[
    "France",
    "USA",
    "Belgium",
    "Croatia"
]
```

`// countries array
[
    "France",
    "USA",
    "Belgium",
    "Croatia"
]`
By prepending "Germany" to it, we'll get this result:

`"Germany"`



## remove ​

`remove`
This formula will remove a given value from an array.


### Example ​

Still with our countries array as an example:

`countries`
```
// countries array
[
    "France",
    "USA",
    "Belgium",
    "Croatia"
]
```

`// countries array
[
    "France",
    "USA",
    "Belgium",
    "Croatia"
]`
Here's what happens when removing "USA" from it:

`"USA"`



## removeByIndex ​

`removeByIndex`
removeByIndex does the same thing as the remove formula, except it does it by removing the element at a certain index in an array, rather than a value.

`removeByIndex`
`remove`

### Example ​

Same example and return as the example for remove, but with the index:

`remove`



## removeByKey ​

`removeByKey`
Given an array of objects, this formula will remove all the objects from the array where the given key is equal to a given value.


### Example ​

Here's an array called users with the following value:

`users`
```
[
    { "name": "Quentin", "role": "admin" },
    { "name": "Joyce", "role": "normal" },
    { "name": "Aurélie", "role": "admin" },
    { "name": "Kévin", "role": "normal" },
    { "name": "Raphael", "role": "superAdmin" }
]
```

`[
    { "name": "Quentin", "role": "admin" },
    { "name": "Joyce", "role": "normal" },
    { "name": "Aurélie", "role": "admin" },
    { "name": "Kévin", "role": "normal" },
    { "name": "Raphael", "role": "superAdmin" }
]`
If we were to remove all the admin users, we would do it like so:




## reverse ​

`reverse`
Given an array, this formula will reverse its values order.


### Example ​

Given back our countries array:

`countries`
```
[
    "France",
    "USA",
    "Belgium",
    "Croatia"
]
```

`[
    "France",
    "USA",
    "Belgium",
    "Croatia"
]`
Reversing it will return this value:




## rollup ​

`rollup`
Given an array of objects, this formula will return all the values for a given key. If the distinct parameter is set to true, it'll return unique values only (false by default).

`distinct`
`true`
`false`

### Example ​

Here's an array called users which equals to:

`users`
```
[
    { "name": "Quentin", "role": "admin" },
    { "name": "Joyce", "role": "normal" },
    { "name": "Aurélie", "role": "admin" },
    { "name": "Kévin", "role": "normal" },
    { "name": "Raphael", "role": "superAdmin" }
]
```

`[
    { "name": "Quentin", "role": "admin" },
    { "name": "Joyce", "role": "normal" },
    { "name": "Aurélie", "role": "admin" },
    { "name": "Kévin", "role": "normal" },
    { "name": "Raphael", "role": "superAdmin" }
]`
If we were to get the possible roles, we would use the rollup formula like this:

`rollup`



## slice ​

`slice`
This formula will return the values from an array from the startIndex up to the endIndex (endIndex not included). It's the exact same function as the JavaScript's slice.

`startIndex`
`endIndex`
`endIndex`

### Example ​

Given a countries array:

`countries`
```
[
    "France",
    "USA",
    "Belgium",
    "Croatia"
]
```

`[
    "France",
    "USA",
    "Belgium",
    "Croatia"
]`
Slicing it to get back only ["USA", "Belgium"] would it be possible by using the slice formula:

`["USA", "Belgium"]`
`slice`



## sort ​

`sort`
Given an array, this formula will sort it in ascending ("asc") or descending ("desc") mode. It can be applied on a given key for arrays of objects.

`"asc"`
`"desc"`

### Example ​

Taking back our array called users which equals to:

`users`
```
[
    { "name": "Quentin", "role": "admin" },
    { "name": "Joyce", "role": "normal" },
    { "name": "Aurélie", "role": "admin" },
    { "name": "Kévin", "role": "normal" },
    { "name": "Raphael", "role": "superAdmin" }
]
```

`[
    { "name": "Quentin", "role": "admin" },
    { "name": "Joyce", "role": "normal" },
    { "name": "Aurélie", "role": "admin" },
    { "name": "Kévin", "role": "normal" },
    { "name": "Raphael", "role": "superAdmin" }
]`
To sort it by user's names in ascending order (alphabetically), we would use the sort formula this way:

`sort`


