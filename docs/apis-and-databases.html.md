# APIs and databases: the critical connection ​


# APIs and databases: the critical connection ​

When building web applications, you'll need to understand how your frontend (what users see and interact with) connects to your backend database (where your data is stored). This connection is typically handled through APIs (Application Programming Interfaces).


## The three-layer architecture ​

Modern web applications typically follow a three-layer architecture:

- Frontend (Presentation Layer) - what users see and interact with (built in WeWeb)
- API (Logic Layer) - the "messenger" that sends requests between frontend and database
- Database (Data Layer) - where your data is stored and managed

Let's visualize this with a simple example. When a user views products in your e-commerce app:

```
┌─────────────┐       ┌─────────────┐       ┌─────────────┐
│             │       │             │       │             │
│   FRONTEND  │ ───▶  │     API     │ ───▶  │  DATABASE   │
│   (WeWeb)   │ ◀───  │             │ ◀───  │             │
│             │       │             │       │             │
└─────────────┘       └─────────────┘       └─────────────┘
      ▲                                            
      │                                            
    User
```

`┌─────────────┐       ┌─────────────┐       ┌─────────────┐
│             │       │             │       │             │
│   FRONTEND  │ ───▶  │     API     │ ───▶  │  DATABASE   │
│   (WeWeb)   │ ◀───  │             │ ◀───  │             │
│             │       │             │       │             │
└─────────────┘       └─────────────┘       └─────────────┘
      ▲                                            
      │                                            
    User`
- user opens the products page in your WeWeb app
- WeWeb sends a request to your API endpoint (e.g., GET /api/products)
- API processes the request and queries the database for product data
- database returns the requested data to the API
- API formats the data (typically as JSON) and sends it back to WeWeb
- WeWeb displays the product data to the user

`GET /api/products`

## Why use this architecture? ​

You might wonder: "Why not connect directly from WeWeb to the database?" There are several important reasons to use an API as a middle layer:


### 1. Security ​

Directly exposing your database to the frontend would be a significant security risk:

- credentials protection: API keys and database credentials can be kept secure on the server
- data validation: the API can validate inputs before they reach your database
- access control: the API can enforce permissions and limit what operations users can perform


### 2. Flexibility and scalability ​

- backend changes: you can change your database structure without affecting the frontend
- multiple frontends: the same API can serve web, mobile, and other applications
- performance optimization: APIs can implement caching and other optimizations


### 3. Business logic ​

- consistent rules: business rules can be enforced in one place
- data transformation: APIs can format data specifically for each use case
- process orchestration: APIs can coordinate complex operations across multiple systems


## How APIs interact with databases ​

Let's look at the common database operations and how APIs handle them:


### Creating data (Create) ​

When a user submits a form to create a new record:

- frontend sends data to the API (e.g., POST /api/customers)
- API validates the data and may transform it
- API constructs a database query (e.g., INSERT INTO customers...)
- database executes the query and returns a result
- API sends success/failure response back to the frontend

`POST /api/customers`
`INSERT INTO customers...`
Imagine a user filling out a form to create a new customer account on your website:

Step 1: The user submits the form in your WeWeb app

Step 2: Your app sends this information to your API

```
POST /api/customers
```

`POST /api/customers`
This is like saying "Hey API, please create a new customer with this information":

```
{
  "name": "Jane Smith",
  "email": "jane@example.com",
  "address": "123 Main St"
}
```

`{
  "name": "Jane Smith",
  "email": "jane@example.com",
  "address": "123 Main St"
}`
Step 3: The API checks the information

- is the email valid?
- is all required information provided?
- does this user already exist?

Step 4: The API tells the database to save the information

Step 5: The API sends back confirmation that it worked:

```
{
  "id": 42,              <- The database assigned ID 42 to this new customer
  "name": "Jane Smith",
  "email": "jane@example.com",
  "address": "123 Main St",
  "created_at": "2023-06-15T10:30:00Z"  <- Timestamp of when it was created
}
```

`{
  "id": 42,              <- The database assigned ID 42 to this new customer
  "name": "Jane Smith",
  "email": "jane@example.com",
  "address": "123 Main St",
  "created_at": "2023-06-15T10:30:00Z"  <- Timestamp of when it was created
}`

### Reading data (Read) ​

When a user wants to view data:

- frontend requests data from the API (e.g., GET /api/products)
- API determines what data the user is allowed to see
- API constructs a database query (e.g., SELECT * FROM products...)
- database executes the query and returns the data
- API formats the data and sends it back to the frontend

`GET /api/products`
`SELECT * FROM products...`
Imagine a user browsing the electronics category on your e-commerce site:

Step 1: The user clicks on "Electronics" category in your WeWeb app

Step 2: Your app asks the API for electronics products

```
GET /api/products?category=electronics
```

`GET /api/products?category=electronics`
This is like saying "Hey API, please give me all products in the electronics category."

Step 3: The API checks if the user is allowed to see these products

- is this a public product or restricted to certain users?
- is the user logged in (if required)?

Step 4: The API asks the database for the matching products

Step 5: The API organizes the data and sends it back:

```
{
  "products": [                <- A list (array) of products
    {
      "id": 101,                  <- First product
      "name": "Smartphone",
      "price": 699.99,
      "category": "electronics"
    },
    {
      "id": 102,                  <- Second product
      "name": "Laptop",
      "price": 1299.99,
      "category": "electronics"
    }
  ],
  "total": 2                   <- Total count of products found
}
```

`{
  "products": [                <- A list (array) of products
    {
      "id": 101,                  <- First product
      "name": "Smartphone",
      "price": 699.99,
      "category": "electronics"
    },
    {
      "id": 102,                  <- Second product
      "name": "Laptop",
      "price": 1299.99,
      "category": "electronics"
    }
  ],
  "total": 2                   <- Total count of products found
}`
Your WeWeb app can now display these products to the user.


### Updating data (Update) ​

When a user edits existing data:

- frontend sends updated data to the API (e.g., PUT /api/orders/123)
- API validates the changes and checks permissions
- API constructs a database query (e.g., UPDATE orders SET...)
- database executes the query and updates the record
- API confirms the update was successful

`PUT /api/orders/123`
`UPDATE orders SET...`
Imagine a store manager updating an order status after shipping a package:

Step 1: The manager clicks "Mark as Shipped" and enters a tracking number

Step 2: Your app sends the updated information to the API

```
PUT /api/orders/123
```

`PUT /api/orders/123`
This is like saying "Hey API, please update order #123 with this new information":

```
{
  "status": "shipped",
  "tracking_number": "1Z999AA10123456784"
}
```

`{
  "status": "shipped",
  "tracking_number": "1Z999AA10123456784"
}`
Step 3: The API checks if this update is allowed

- is this user authorized to update orders?
- is this a valid order status?
- is the order in a state where it can be marked as shipped?

Step 4: The API tells the database to update the order

Step 5: The API confirms the update worked:

```
{
  "id": 123,
  "status": "shipped",                          <- Status is now "shipped"
  "tracking_number": "1Z999AA10123456784",      <- Tracking number is saved
  "updated_at": "2023-06-16T14:25:00Z"          <- When the update happened
}
```

`{
  "id": 123,
  "status": "shipped",                          <- Status is now "shipped"
  "tracking_number": "1Z999AA10123456784",      <- Tracking number is saved
  "updated_at": "2023-06-16T14:25:00Z"          <- When the update happened
}`
Your WeWeb app can now show a success message and display the updated order.


### Deleting data (Delete) ​

When a user deletes data:

- frontend sends a delete request to the API (e.g., DELETE /api/comments/456)
- API checks if the user has permission to delete
- API constructs a database query (e.g., DELETE FROM comments...)
- database executes the query and removes the record
- API confirms the deletion was successful

`DELETE /api/comments/456`
`DELETE FROM comments...`
Imagine a user deleting a comment they posted:

Step 1: The user clicks "Delete" on their comment

Step 2: Your app asks the API to delete the comment

```
DELETE /api/comments/456
```

`DELETE /api/comments/456`
This is like saying "Hey API, please delete comment #456."

Step 3: The API checks if deletion is allowed

- is this the user who created the comment?
- does this user have permission to delete comments?
- does this comment exist?

Step 4: The API tells the database to delete the comment

Step 5: The API confirms the deletion:

```
{
  "success": true,
  "message": "Comment deleted successfully"
}
```

`{
  "success": true,
  "message": "Comment deleted successfully"
}`
Your WeWeb app can now remove the comment from the display and show a confirmation message.


## API types for database interaction ​

While there are several types of APIs used for database interaction (like GraphQL, SOAP, and others), you'll most commonly work with REST APIs in modern web development:


### REST APIs ​

REST (Representational State Transfer) is the most common API architecture you'll encounter when building applications:

- organizes endpoints around resources (nouns like users, products, orders)
- uses standard HTTP methods (GET, POST, PUT, DELETE)
- typically returns JSON data
- stateless (each request contains all necessary information)

Example REST endpoints:

- GET /api/products - get all products
- GET /api/products/101 - get a specific product
- POST /api/products - create a new product
- PUT /api/products/101 - update a product
- DELETE /api/products/101 - delete a product

`GET /api/products`
`GET /api/products/101`
`POST /api/products`
`PUT /api/products/101`
`DELETE /api/products/101`
REST APIs are widely used because they're:

- simple to understand: the API structure follows predictable patterns
- well-supported: nearly all programming languages and frameworks have tools for working with REST
- scalable: they work well for both small and large applications
- built for the web: they use the same HTTP methods that power the internet

TIP

When working in WeWeb, you'll primarily be interacting with REST APIs through the REST API plugin or through other backend plugins like Supabase and Xano that provide REST APIs.


## Working with APIs and databases in WeWeb ​

In WeWeb, you'll use collections to interact with your API, which in turn interacts with your database:

- add a data source plugin: connect to your API through a plugin like REST API, Supabase, or Xano
- create collections: set up collections to fetch data from your API endpoints
- backend vs. frontend operations:backend operations (preferred): let your API handle filtering, sorting, and joiningfrontend operations: fetch data with WeWeb and process it client-side
- backend operations (preferred): let your API handle filtering, sorting, and joining
- frontend operations: fetch data with WeWeb and process it client-side
- performance considerations:make your API endpoints efficient and specific to your needsuse pagination to limit the amount of data transferredconsider caching frequently accessed data
- make your API endpoints efficient and specific to your needs
- use pagination to limit the amount of data transferred
- consider caching frequently accessed data

add a data source plugin: connect to your API through a plugin like REST API, Supabase, or Xano

create collections: set up collections to fetch data from your API endpoints

backend vs. frontend operations:

- backend operations (preferred): let your API handle filtering, sorting, and joining
- frontend operations: fetch data with WeWeb and process it client-side

performance considerations:

- make your API endpoints efficient and specific to your needs
- use pagination to limit the amount of data transferred
- consider caching frequently accessed data


## Best practices ​

Here are some best practices for working with APIs and databases:


### Security ​

- never expose database credentials to the frontend
- always validate and sanitize inputs before using them in database queries
- implement proper authentication and authorization in your API
- use HTTPS for all API communications


### Performance ​

- index fields used in WHERE clauses and joins
- limit the data returned to what's actually needed
- use pagination for large data sets
- consider caching for frequently accessed data


### Design ​

- design your API around business needs, not database structure
- version your API to allow for future changes
- use consistent naming conventions for endpoints and parameters
- document your API thoroughly for future reference


## Troubleshooting common issues ​

When your frontend isn't getting the expected data from your database, the issue is often in the API connection:

- API endpoint issues:check that you're calling the correct URLverify that you're using the correct HTTP method (GET, POST, etc.)ensure you're sending the expected parameters or body data
- check that you're calling the correct URL
- verify that you're using the correct HTTP method (GET, POST, etc.)
- ensure you're sending the expected parameters or body data
- authentication problems:verify that your API key or token is valid and not expiredcheck that you're including the authentication in the correct formatconfirm that the authenticated user has permission for the requested operation
- verify that your API key or token is valid and not expired
- check that you're including the authentication in the correct format
- confirm that the authenticated user has permission for the requested operation
- data format issues:make sure you're sending data in the format the API expectscheck that date formats, number formats, and other data types match expectationsverify that required fields are included and properly formatted
- make sure you're sending data in the format the API expects
- check that date formats, number formats, and other data types match expectations
- verify that required fields are included and properly formatted
- database connection issues:if your API can't connect to the database, check connection strings and credentialsverify that the database server is running and accessiblecheck for database-specific errors in your API logs
- if your API can't connect to the database, check connection strings and credentials
- verify that the database server is running and accessible
- check for database-specific errors in your API logs

API endpoint issues:

- check that you're calling the correct URL
- verify that you're using the correct HTTP method (GET, POST, etc.)
- ensure you're sending the expected parameters or body data

authentication problems:

- verify that your API key or token is valid and not expired
- check that you're including the authentication in the correct format
- confirm that the authenticated user has permission for the requested operation

data format issues:

- make sure you're sending data in the format the API expects
- check that date formats, number formats, and other data types match expectations
- verify that required fields are included and properly formatted

database connection issues:

- if your API can't connect to the database, check connection strings and credentials
- verify that the database server is running and accessible
- check for database-specific errors in your API logs


## Conclusion ​

The connection between APIs and databases is a fundamental concept in modern web development. By understanding how these components work together, you can build more robust, secure, and efficient applications in WeWeb.

Remember that a well-designed API provides a secure and flexible interface to your database, allowing you to build rich frontend experiences while maintaining data integrity and security.

CONTINUE LEARNING

Now that you understand how APIs connect to databases, learn how to implement these concepts in WeWeb:

Intro to Collections →

