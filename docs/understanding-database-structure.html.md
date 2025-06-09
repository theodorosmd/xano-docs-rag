# Understanding database structure ​


# Understanding database structure ​

The way you organize your data is one of the most important decisions you'll make when building an application. A well-designed database structure makes your app easier to build, faster to use, and simpler to maintain over time.


## Why data structure matters ​

Think of your database like a filing system:

- poor organization: papers scattered everywhere, making it hard to find anything
- good organization: everything sorted in labeled folders, making information easy to retrieve

A well-structured database:

- makes your app faster and more responsive
- reduces errors and inconsistencies
- makes it easier to build new features
- helps your application scale as it grows

TIP

Even though WeWeb is a frontend tool and not a database tool, it is critical you understand the core concepts of structuring a database, as will help you make better decisions about how to organize and access your data.


## Core concepts in database structure ​


### Tables (Collections) ​

The basic building blocks of any database are tables (also called collections). Each table stores a specific type of data.

Imagine tables as spreadsheets, where each spreadsheet contains information about one specific type of thing. For example, a "Users" spreadsheet would contain only user information, while a "Products" spreadsheet would contain only product information.

Common examples of tables include:

- users
- products
- orders
- comments
- categories

Each table should represent one type of entity or concept. For example, don't mix product information and order information in the same table.


### Records (Rows or Documents) ​

Each item in a table is called a record (or row, or document). For example, in a "Users" table, each record represents one user.

If you picture a table as a spreadsheet, each row would be a single record. For instance, in your Users table, you might have:

- row 1: John Smith (user #1)
- row 2: Jane Doe (user #2)
- row 3: Bob Johnson (user #3)

Each row represents one complete entity (one user, one product, one order, etc.).


### Fields (Columns or Properties) ​

The specific pieces of information stored about each record are called fields (or columns, or properties).

Continuing with our spreadsheet analogy, if rows are records, columns are fields. Each column contains one specific type of information about all records. For example, a user record might have fields (columns) for:

- name
- email
- password (encrypted)
- date registered
- role

So your spreadsheet might look like:

WARNING

Only include fields that actually belong to that entity. Don't add fields from related entities - use relationships instead (more on this below).


## Primary keys: the foundation of relationships ​

Every table should have a primary key - a unique identifier for each record. This is like the ID number on a driver's license - it ensures you can always find the exact record you're looking for.

In the table example above, the "ID" column is the primary key. Each value must be unique - no two users can have the same ID number. This uniqueness is what allows databases to create relationships between tables.

Common types of primary keys:

- auto-incrementing IDs: simple numbers that increase with each new record (1, 2, 3...)
- UUIDs: longer, randomly generated unique IDs (e.g., "550e8400-e29b-41d4-a716-446655440000")

TIP

Most database systems will create primary keys automatically. Just make sure your tables have them!


## Relationship types: connecting your data ​

The real power of modern databases comes from creating relationships between different tables. There are three main types of relationships:


### One-to-one relationships ​

In a one-to-one relationship, one record in Table A is connected to exactly one record in Table B.

For example, imagine a Users table and a User_Details table:

- each user in the Users table has exactly one corresponding record in the User_Details table
- each record in the User_Details table belongs to exactly one user

You could visualize it like this:

Users table:

User_Details table:

Notice that the User_Details table has a user_id field that references the primary key in the Users table.

`user_id`
Examples of one-to-one relationships:

- a user has one detailed profile
- a product has one detailed description
- a country has one capital city

One-to-one relationships are relatively rare. Often, if you have a true one-to-one relationship, that information could be in the same table unless:

- you want to separate rarely-used information to improve performance
- some information is optional while other information is required


### One-to-many relationships ​

In a one-to-many relationship, one record in Table A can be connected to multiple records in Table B, but each record in Table B belongs to only one record in Table A.

For example, imagine a Users table and a Posts table:

- one user can create many posts
- each post is created by exactly one user

You could visualize it like this:

Users table:

Posts table:

Notice how the Posts table has a user_id field that references the primary key in the Users table. This is how we know which user created each post.

`user_id`
Examples of one-to-many relationships:

- one user can write many posts
- one product can have many reviews
- one order can contain many products

This is the most common type of relationship in most applications.


### Many-to-many relationships ​

In a many-to-many relationship, one record in Table A can be connected to multiple records in Table B, and vice versa.

For example, imagine a Students table and a Courses table:

- one student can take many courses
- one course can have many students

To implement this, we need a third table (called a junction table):

Students table:

Courses table:

Enrollments table (junction table):

The Enrollments table has foreign keys to both Students and Courses, creating the many-to-many relationship.

Examples of many-to-many relationships:

- students and classes (one student takes many classes, one class has many students)
- products and tags (one product can have many tags, one tag can be applied to many products)
- users and roles (one user can have multiple roles, one role can be assigned to many users)

Many-to-many relationships typically require a "junction table" (sometimes called a "pivot table") to connect the records.


## Foreign keys: creating relationships ​

To create these relationships, we use what's called a "foreign key" - a field that stores the primary key of a record in another table.

In the examples above, the user_id field in the Posts table is a foreign key that references the primary key (user_id) in the Users table. This connection allows us to know which user created each post.

`user_id`
`user_id`
Other examples of foreign keys:

- in an "Orders" table, you might have a "user_id" field that references the primary key from the "Users" table
- in a "Products" table, you might have a "category_id" field that references the primary key from the "Categories" table

Foreign keys are what make joins possible - they're the "connectors" between related tables. When you perform a join operation, the database matches records based on these keys.


## Normalization: organizing for efficiency ​

"Normalization" is the process of organizing your database to:

- reduce redundancy (avoid storing the same data in multiple places)
- ensure data integrity (make it harder to create inconsistencies)


### Why normalize data? ​

Imagine you have an e-commerce application and store customer information in your orders table:

Unnormalized Orders table:

Problems with this approach:

- if John Smith updates his address, you have to update it across all his orders
- data is duplicated, wasting storage space
- inconsistencies can easily occur (different spellings, formats, etc.)


### Normalizing the data ​

A better approach would be:

Customers table:

Products table:

Orders table:

Order_Items table:

Now:

- customer information is stored once in the Customers table
- orders only store a reference (foreign key) to the customer
- updating a customer's address only requires changing one record


## Real-world database structure example ​

Let's look at a practical example for an e-commerce application:


### Users table ​

- id (primary key)
- email
- password (encrypted)
- name
- created_at

`id`
`email`
`password`
`name`
`created_at`

### Products table ​

- id (primary key)
- name
- description
- price
- image_url
- inventory_count
- category_id (foreign key to Categories)

`id`
`name`
`description`
`price`
`image_url`
`inventory_count`
`category_id`

### Categories table ​

- id (primary key)
- name
- description

`id`
`name`
`description`

### Orders table ​

- id (primary key)
- user_id (foreign key to Users)
- order_date
- status
- shipping_address
- total_amount

`id`
`user_id`
`order_date`
`status`
`shipping_address`
`total_amount`

### OrderItems table (junction table for Orders and Products) ​

- id (primary key)
- order_id (foreign key to Orders)
- product_id (foreign key to Products)
- quantity
- price_at_time_of_order

`id`
`order_id`
`product_id`
`quantity`
`price_at_time_of_order`
UNDERSTANDING JUNCTION TABLES

A junction table (also called a bridge table, join table, or pivot table) is a special type of table used to connect two other tables in a many-to-many relationship.

Junction tables are necessary because databases can't directly create many-to-many relationships between tables. Instead, we create two one-to-many relationships with the junction table in the middle.

For example, the OrderItems table above connects:

- one order to many order items (one-to-many)
- one product to many order items (one-to-many)

This effectively creates a many-to-many relationship between orders and products (one order can contain many products, and one product can appear in many orders).

Junction tables typically contain:

- a primary key of their own
- foreign keys to both tables they're connecting
- sometimes additional information about the relationship (like quantity or price in this case)

This structure allows for efficient queries like:

- show all orders for a specific user
- list all products in a specific category
- calculate total sales by product or category
- show all items in a specific order

Here's how you might retrieve all products in a specific category:

- look up the category ID for "Electronics" in the Categories table
- find all products in the Products table where category_id matches

Or to show all items in a specific order:

- look up the order details in the Orders table
- find all items in the OrderItems table where order_id matches
- for each item, get the product details from the Products table


## Common database structure patterns ​

Here are some common patterns you'll encounter when designing database structures:


### Hierarchical data ​

For representing categories, organization charts, or folders:

A common approach is to use a "parent_id" field that references the same table:

```
Categories:
- id: 1, name: "Electronics", parent_id: null
- id: 2, name: "Computers", parent_id: 1
- id: 3, name: "Laptops", parent_id: 2
```

`Categories:
- id: 1, name: "Electronics", parent_id: null
- id: 2, name: "Computers", parent_id: 1
- id: 3, name: "Laptops", parent_id: 2`
This creates a tree structure where:

- electronics is a top-level category (parent_id is null)
- computers is a subcategory of electronics
- laptops is a subcategory of computers


### Tagging systems ​

For flexibly categorizing items:

Typically implemented with:

- tags table (id, name)
- items table (id, name, description, etc.)
- itemTags junction table (item_id, tag_id)

Example:

- tags table: #electronics, #sale, #new-arrival
- products table: laptop, smartphone, headphones
- productTags junction table: laptop has tags: #electronics, #new-arrivalsmartphone has tags: #electronics, #saleheadphones has tags: #electronics, #sale, #new-arrival
- laptop has tags: #electronics, #new-arrival
- smartphone has tags: #electronics, #sale
- headphones has tags: #electronics, #sale, #new-arrival

- laptop has tags: #electronics, #new-arrival
- smartphone has tags: #electronics, #sale
- headphones has tags: #electronics, #sale, #new-arrival

This flexible structure allows products to have any combination of tags.


### User permissions ​

For controlling access to features:

Common tables:

- users (id, name, email, etc.)
- roles (id, name, description)
- permissions (id, name, description)
- userRoles (user_id, role_id)
- rolePermissions (role_id, permission_id)

This structure allows:

- users to have multiple roles
- roles to have multiple permissions
- efficiently checking if a user has permission to perform an action


## Planning your database for use in WeWeb ​

When building applications in WeWeb, you'll often use external databases or APIs. Here's how to approach planning your data structure:

- identify your entities: what are the main "things" your app deals with? (users, products, orders, etc.)
- define relationships: how do these entities relate to each other? (one-to-one, one-to-many, many-to-many)
- choose your data sources: will you use Supabase, Xano, a REST API, or something else?
- create your schema: set up your tables, fields, and relationships in your chosen data source

identify your entities: what are the main "things" your app deals with? (users, products, orders, etc.)

define relationships: how do these entities relate to each other? (one-to-one, one-to-many, many-to-many)

choose your data sources: will you use Supabase, Xano, a REST API, or something else?

create your schema: set up your tables, fields, and relationships in your chosen data source

GET FAMILIAR WITH YOUR BACKEND TOOL

Before you jump straight into creating your schema, get familiar with the backend tool you decide to use, as it may have unique features that will impact how you ultimtaly structure your schema.

For example, Xano has something called 'Add-ons' to make perfoming simple joins more conveniant.

- connect to WeWeb: use collections to fetch the data when needed

TIP

Start simple and expand as needed. It's easier to add complexity to a well-structured foundation than to fix a poorly designed database later.


## Thinking about joins when planning ​

When designing your database structure, think ahead about the joins you'll need:


### Common join scenarios ​

- user-specific data: joining user records with their content (posts, orders, etc.)plan for a user_id foreign key in related tablesexample: "Show me all orders placed by this user"
- plan for a user_id foreign key in related tables
- example: "Show me all orders placed by this user"
- detail views: showing a main record with related informationconsider which one-to-many relationships you'll need to displayexample: "Show me this order and all its line items"
- consider which one-to-many relationships you'll need to display
- example: "Show me this order and all its line items"
- reporting and analytics: aggregating data across multiple tablesmay require more complex relationships and carefully planned keysexample: "Show me total sales by product category by month"
- may require more complex relationships and carefully planned keys
- example: "Show me total sales by product category by month"
- search functionality: finding information across different types of recordsthink about which tables need to be searchable togetherexample: "Find all products matching 'wireless headphones'"
- think about which tables need to be searchable together
- example: "Find all products matching 'wireless headphones'"

user-specific data: joining user records with their content (posts, orders, etc.)

- plan for a user_id foreign key in related tables
- example: "Show me all orders placed by this user"

`user_id`
detail views: showing a main record with related information

- consider which one-to-many relationships you'll need to display
- example: "Show me this order and all its line items"

reporting and analytics: aggregating data across multiple tables

- may require more complex relationships and carefully planned keys
- example: "Show me total sales by product category by month"

search functionality: finding information across different types of records

- think about which tables need to be searchable together
- example: "Find all products matching 'wireless headphones'"


### Join performance considerations ​

- index foreign keys: make sure all fields used in joins are indexed for performancethis makes lookups much faster, especially with large tables
- this makes lookups much faster, especially with large tables
- limit join depth: try to avoid joining more than 3-4 tables in a single querymore complex joins can significantly slow down queries
- more complex joins can significantly slow down queries
- consider data volume: tables with thousands of records need more careful planning than small tablesplan for scale from the beginning if you expect significant growth
- plan for scale from the beginning if you expect significant growth

index foreign keys: make sure all fields used in joins are indexed for performance

- this makes lookups much faster, especially with large tables

limit join depth: try to avoid joining more than 3-4 tables in a single query

- more complex joins can significantly slow down queries

consider data volume: tables with thousands of records need more careful planning than small tables

- plan for scale from the beginning if you expect significant growth

BACKEND-SPECIFIC IMPLICATIONS

How you actually perform joins and optimize their performance will vary significantly depending on your chosen backend tool. The vast majortiy of modern database/backend tool are all built on the same principles, but each have their own unique ways as to how you use them.

It's important to be aware of these join scenarios as general concepts when planning your data structure, but always consult the documentation for your specific backend tool to understand the best practices for that platform.


## Conclusion ​

Taking the time to plan your database structure carefully will save you countless hours later. A well-designed database makes your application easier to build, more efficient to run, and simpler to maintain and extend.

Remember these key principles:

- each table should represent one type of entity
- use relationships to connect related data
- plan for the types of joins you'll need
- keep your structure normalized to avoid redundancy

With a solid foundation in database structure, you'll be able to build more powerful and efficient applications in WeWeb.

CONTINUE LEARNING

Now that you understand the basics of structuring a database, the next key step is to learn about what will act as the gatekeeper of your database – APIs:

Understanding APIs→

