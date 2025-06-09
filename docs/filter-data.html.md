# Filtering data ​


# Filtering data ​


## Filters for performance ​

When you are dealing with large amounts of data that risk overloading a user’s browser, it is best practice to apply filters on the backend.

What does that mean?

It means that, instead of loading all the data in the user’s browser, you only load the data they might need or, even better, the data they need right now.


## Airbnb example ​

Take Airbnb. With millions of listings and millions of users accessing the site at any given time, it would make no sense whatsoever to load all the listings in all the users’ browsers.

In fact, it would be downright impossible. If Airbnb did that, all their users’ browsers would crash because they would be able to handle that amount of data.

That's not the customer experience you're looking for.

Instead, when you go to Airbnb’s website, you are invited to make a search.

When you click on the search button, your browser will tell Airbnb’s servers to fetch the data you need based on your search criteria.

Then, Airbnb’s backend will send back the filtered data to your browser which will display a list of items that match the conditions of your search.


## Backend filtering in WeWeb ​

Here’s how you can you tell a REST API backend to return filtered data based on a user's selection and/or search:

