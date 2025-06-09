# Working with data in WeWeb ​


# Working with data in WeWeb ​

After choosing a backend for your application, the next step is to connect your app to that data source and display information from it. This guide will cover the basics of fetching and displaying data in WeWeb.

PLAN YOUR DATA STRUCTURE

Before diving into working with data in WeWeb, it's important to have a well-structured database. If you're not familiar with database design principles, check out our guide on Understanding Database Structure. A properly organized database will make your WeWeb app development much easier and more efficient.


## The basics of working with data ​

Working with external data in WeWeb involves four key steps:

- setting up a data source plugin
- creating a collection
- fetching data from your source
- displaying that data with repeating items

Let's explore each step:


## Step 1: Setting up a data source plugin ​

Before you can fetch external data, you need to add a data source plugin:

- click on Plugins in the top navigation
- select Data Sources
- choose a data source
- click Add and follow the setup instructions

`Plugins`
`Data Sources`
`Add`

## Step 2: Creating a collection ​

Collections are how WeWeb organizes and manages external data. Here's how to create one:

The basic steps are:

- go to the Data tab in the left sidebar
- click + New under Collections
- give your collection a name
- select your data source
- configure how to fetch the data
- fetch the data to test it

`Data`
`+ New`

## Step 3: Understanding your collection data ​

After fetching data, you'll see your collection in the Data panel:

Key properties of a collection include:

- data - the array of items fetched from your source
- isFetching - a boolean that indicates if data is currently being loaded
- Length - the number of items in your collection

Learn more about collections →


## Step 4: Displaying data with repeating items ​

The most common way to display collection data is through repeating items:

Here's the process:

- design a single item (like a product card) that will represent each piece of data
- place it in a container (like a flexbox)
- select the container and enable Repeat Items
- bind the Items property to your collection's data

`Repeat Items`
`Items`
BINDING TO LISTS

When binding the repeating of items, you must bind to a list (array). Make sure to bind to the collection's data property, which contains the array of items.

`data`

## Step 5: Styling your repeated items ​

After setting up the repeating items, the next step is to style how they're arranged:

Common arrangement options include:

- lists (vertical flexbox)
- grids (grid container)
- carousels (horizontal flexbox)
- tables (table element)


## Step 6: Binding data to your elements ​

The final step is to bind the elements inside your repeating items to the corresponding data fields:

Inside each repeating item, you can access the current item's data directly in your bindings. This allows you to:

- bind text elements to show item properties
- bind image sources to item URLs
- bind styling properties based on item values

Learn more about binding the repeating of items →


## Simple tips for success ​

- create a loading indicator - bind an element's visibility to the collection's isFetching property to show when data is loading
- create an empty state - bind an element's visibility to the collection's Length === 0 to show when no data is available
- name your elements clearly - use names that match your data fields to make binding easier

create a loading indicator - bind an element's visibility to the collection's isFetching property to show when data is loading

`isFetching`
create an empty state - bind an element's visibility to the collection's Length === 0 to show when no data is available

`Length === 0`
name your elements clearly - use names that match your data fields to make binding easier

CONTINUE LEARNING

Now that you've learned how to work with data in your application, the next step is to ensure you properly implement authentication and security:

Authentication and security →

