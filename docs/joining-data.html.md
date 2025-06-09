# Joining data from multiple collections ​


# Joining data from multiple collections ​

Most real-world applications need to combine data from different tables to create complete, useful information for users. This guide will teach you how to query related data across multiple tables using different techniques in WeWeb.


## Understanding the need for joins ​

In a well-designed database, information is organized into separate tables to avoid duplication. For example:

- a customers table stores customer details (name, email, etc.)
- an orders table stores order information (date, total, etc.)
- an orderItems table stores the individual items in each order

`customers`
`orders`
`orderItems`
To display a complete order summary, you need to combine data from all three tables. This process of combining related data is called "joining."


## Join methods in WeWeb ​

There are two primary ways to join data from multiple tables in WeWeb:

- backend joins: using your data source's native join capabilities
- frontend joins: using WeWeb's formulas to combine data after it's fetched

Let's explore both approaches:


### Backend joins (preferred method) ​

Backend joins happen at your data source, before the data reaches WeWeb. This is the recommended approach whenever possible because it's more efficient and secure.

Different data sources have different approaches to backend joins:


#### Supabase ​

Supabase provides a powerful way to perform joins directly in your queries:

When using Supabase with WeWeb, you can leverage foreign key relationships by:

- using the advanced query mode in your collection setup
- specifying related tables you want to include
- accessing nested data in your WeWeb interface

For example, if you have a companies table with a foreign key to a cities table:

`companies`
`cities`
- set up your Supabase collection in WeWeb using the Advanced mode
- include the related table fields (e.g., cities(id, name))
- in your WeWeb interface, you can now access cities.name directly from your companies collection

`cities(id, name)`
`cities.name`
This approach is efficient because Supabase handles the join at the database level before sending data to WeWeb.


#### Xano ​

Xano provides a feature called "Add-ons" that makes it easy to include related data:

To use Xano Add-ons for joins:

- create or edit your API endpoint in Xano
- navigate to the output settings of your endpoint
- add an "add-on" to include related data: select the table you want to join (e.g., users)choose the relation type (e.g., "Single item" for one-to-many)specify the foreign key to match (e.g., user_id)name the field for the joined data (e.g., _user)
- select the table you want to join (e.g., users)
- choose the relation type (e.g., "Single item" for one-to-many)
- specify the foreign key to match (e.g., user_id)
- name the field for the joined data (e.g., _user)
- save and publish your endpoint
- in WeWeb, refresh your collection, and the joined data will be available as a nested object

- select the table you want to join (e.g., users)
- choose the relation type (e.g., "Single item" for one-to-many)
- specify the foreign key to match (e.g., user_id)
- name the field for the joined data (e.g., _user)

`users`
`user_id`
`_user`
This approach is powerful because it handles the join server-side, reducing the amount of data transferred and processing required in the browser.


#### Other backend tools ​

Most backend services and database tools provide ways to perform joins or include related data. The specific implementation will vary depending on the tool you're using:

- firebase/firestore: use sub-collections or denormalized data
- airtable: use linked records and the "Fields from linked records" option
- custom REST APIs: implement endpoints that return pre-joined data
- graphQL: use nested queries to fetch related data in a single request

TIP

Always check your backend tool's documentation for the most efficient way to join data. Creating properly joined data on the backend will almost always be more efficient than joining in the frontend.


### Frontend joins ​

When backend joins aren't available or you need more flexibility, you can perform joins in WeWeb using JavaScript formulas:


#### Method 1: Using lookup formula ​

The lookup formula allows you to find a matching item in a collection based on a key value:

`lookup`
```
// Find a specific user based on user_id
lookup(item.user_id, page.users.data, "id")
```

`// Find a specific user based on user_id
lookup(item.user_id, page.users.data, "id")`
This formula takes three parameters:

- the value to search for (e.g., item.user_id)
- the collection to search in (e.g., page.users.data)
- the key to match against (e.g., "id")

`item.user_id`
`page.users.data`
`"id"`
It returns the first matching item from the collection, or undefined if no match is found.

`undefined`
Learn about the lookup formula


#### Method 2: Using filter by key formula ​

The filterByKey formula allows you to filter a collection to only include items where a specific key matches a value:

`filterByKey`
```
// Get all appointments for a specific contact
filterByKey(page.appointments.data, "contact_id", item.id)
```

`// Get all appointments for a specific contact
filterByKey(page.appointments.data, "contact_id", item.id)`
This formula takes three parameters:

- the collection to filter (e.g., page.appointments.data)
- the key to check (e.g., "contact_id")
- the value to match (e.g., item.id)

`page.appointments.data`
`"contact_id"`
`item.id`
It returns a new array containing only the items where the specified key matches the provided value.

This is particularly useful for one-to-many relationships, where you want to find all related items

Learn about the filter by key formula


## Frontend vs. backend joins: pros and cons ​

When deciding how to implement joins in your WeWeb application, it's important to understand the trade-offs between frontend and backend approaches:


### Backend joins ​

Pros:

- better performance: data is filtered and joined before being sent to the browser
- reduced data transfer: only the exact data needed is transmitted
- security: sensitive data can be excluded at the source
- scalability: works well with large datasets (thousands of records)
- consistency: database ensures data integrity during joins

Cons:

- less flexibility: changes may require backend modifications
- setup complexity: may require more initial configuration
- learning curve: need to understand your backend tool's specific join mechanism
- dependency: relies on backend service availability


### Frontend joins ​

Pros:

- flexibility: can create dynamic joins on-the-fly
- quick iteration: changes can be made directly in WeWeb without backend updates
- complex logic: can implement custom join logic beyond what your backend may support
- independence: can work with multiple data sources simultaneously

Cons:

- performance limitations: can slow down with larger datasets (hundreds+ records)
- increased data transfer: must fetch complete collections before joining
- browser load: processing happens on the user's device, potentially affecting UI responsiveness
- memory usage: multiple large collections can consume significant browser memory


### When to choose each method ​

Choose Backend Joins When:

- working with large datasets
- joins are stable and well-defined
- performance is critical
- security concerns require data filtering at the source
- the same joined data is used in multiple places

Choose Frontend Joins When:

- working with smaller datasets
- needing highly dynamic or conditional joins
- rapidly prototyping or iterating
- combining data from multiple different backends
- backend modification is not feasible

