# Supabase ​


# Supabase ​

Supabase is an open-source backend-as-a-service platform that simplifies app development with integrated tools like a real-time PostgreSQL database, user authentication, file storage, and serverless functions. As an open-source alternative to Firebase, it enables you to build secure, scalable applications without managing complex backend infrastructure.


## Plugin configuration ​

The Supabase plugin connects WeWeb directly to your Supabase project, enabling you to manage your tables, API endpoints, database functions, secrets and integrations right from within the WeWeb interface.

To add the plugin in WeWeb:

- Navigate to Back-end > Add Supabase:

`Back-end`
`Add Supabase`


- Once you've added it, you will have the option to connect to your project in Guided or Custom mode for self-hosted Supabase projects:

`Guided`
`Custom`


- Grant the necessary permissions to Supabase.



- Back in WeWeb, you will see that your account is connected and that you will be able to select your existing Supabase project or create a new one:



WARNING

If you receive the error below when trying to create your Supabase project, it likely means you have reached the limit of the number of projects you can create in your Supabase workspace and need to free up space.

- Upon clicking on "Continue" to confirm the setup, we can see additional plugin information, such as the configuration, and realtime collections:



TIP

Realtime tables allow you to see changes to data immediately when they happen, without needing to refresh the page. By default, Supabase disables realtime on tables for performance reasons.

This means:

- You need to turn on realtime both in Supabase first, then in WeWeb
- When realtime is on, any changes to your data (like updates, new entries, or deletions) show up instantly for users

If we click on the Backend panel, the tables from our database:

`Backend`


In this guide, we will be working with the properties and properties_images tables.

`properties`
`properties_images`

## Fetching data ​

We can create a collection in WeWeb using Supabase as a data source. This will essentially allow us to get data from specific tables and store them in a collection, which is just a place to store data.

- Go to Data > New
- Choose Supabase as a Source
- Select which database table you want to pull data from:

`Data`
`New`
`Source`



### Guided mode ​

Guided mode will be enabled by default, which is a mode that pre-configures the collection to pull in data from every available table column without requiring manual selection.

`Guided mode`
In the example below, we decided to exclude the data from the created_at, created_by and updated_ columns in our properties table:

`created_at`
`created_by`
`updated_`
`properties`


As a result, our collection will look like this:




### Advanced mode ​

Advanced mode lets you get information from multiple connected tables at once, rather than just one table at a time.

TIP

In web development, this relational retrieval of informations is termed a 'join'.

You can join tables when they have fields that relate to one another, allowing you to retrieve records that have the relation from the joined tables.

For example, think of your property listings like this:

- The properties table stores the basic details of each property with the columns:

`properties`
- id, address, bathrooms, bedrooms, description, price, square_feet, title

`id`
`address`
`bathrooms`
`bedrooms`
`description`
`price`
`square_feet`
`title`
- The property_images table stores multiple images for each property:

`property_images`
- id, image_url, property_id
- Each image is linked to its property using property_id
- image_url is where the actual image link is stored

`id`
`image_url`
`property_id`
`property using property_id`
`image_url`
The relationship works because each row in property_images has a property_id that matches an id in the properties table, allowing you to know which images belong to which property.

`property_images`
`property_id`
A collection can show data from two connected tables. To do this, use this format: name_of_second_table:id(which_columns_you_want)

`name_of_second_table:id(which_columns_you_want)`
In our properties example, if we wanted to get the related images of a property we would write: property_images:id(image_url)

`property_images:id(image_url)`


This tells WeWeb to:

- Look at the property_images table
- Connect it to the main properties table
- Show only the image_url column from property_images

`property_images`
`properties`
`image_url`
`property_images`
So for each property, you'll see its own details plus its related images, all in one collection:

TIP

In the example above, we used a one-to-many database relationship. One property can have many images, but you can also accomplish one-to-one relationships, that is, one property can have one main image from the property_images table. Suppose you have a column in the properties table called main_image which points to the property_images table. We can get its value by writing main_image: main_image(image_url):

`property_images`
`properties`
`main_image`
`property_images`
`main_image: main_image(image_url)`



## Row-Level Security ​

Row-Level Security (RLS) is a security mechanism that controls who can access or modify which rows in a table. Without RLS, anyone with database access can view, update, or delete all rows.

Imagine a school database with a students table. Without RLS, everyone could see all students' records. But with RLS:

- A student can only see their own grades.
- A teacher can see only their students' grades.
- The principal can see everyone’s grades.

By default, Supabase allows full access to all data so you can quickly set up and test your apps without restrictions. However, once you enable RLS on a table, Supabase blocks all access until you create explicit policies defining who can read or modify data.

- Enable RLS for your table



- Define policies for the table:



In the example below, we have the following policies:

- Enable insert for authenticated users only INSERT
- Enable read access for all users SELECT
- Enable delete for property owners DELETE
- Enable update for property owners UPDATE

`Enable insert for authenticated users only INSERT`
`Enable read access for all users SELECT`
`Enable delete for property owners DELETE`
`Enable update for property owners UPDATE`


WARNING

If RLS is enabled for a table but no policies are defined, WeWeb will not be able to fetch data for your collection. To ensure proper access, always create the necessary policies.


## Filtering, Pagination & Sorting ​

When working with large amounts of data in Supabase, you might need backend filtering, pagination and sorting. WeWeb handles this at the collection level. You don't need to set these up in Supabase - simply select your collection and go to the Query configuration section.

`Query configuration`
This means even with, for example, 50,000 records or more, you can efficiently control how your data is loaded and displayed.

In the example below, we are getting only five records because the pagination limit is 5!



