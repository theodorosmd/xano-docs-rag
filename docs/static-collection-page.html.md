# Static collection pages ​


# Static collection pages ​

A static collection page is a page, which is bound to a collection, will duplicate itself for all of the items in the collection.

But, for each item, it'll keep the same design. It's useful to create a page that will display all the items of a collection.


## Use case ​

Let's say you have a collection of products.

On your homepage, you'll display all of the products of this collection, but then redirect each of them to a page with more information about each product.

You will then create a static collection page, and bind it to the products collection.

This page will then duplicate itself for each product, and display the product's information.

WARNING

To create a static collection page, you need to have a collection setup in your app, with the static mode.

`static`
TIP

Static collection pages are statically generated when you push the app to production. This means that they will be generated only once, and then they will be served directly from the CDN. This is why they are so fast and good for SEO.


## Create a static collection page ​

Some explanations:

- You have to bind a static collection to the page. This is the collection that will be used to duplicate the page for each item in the collection.
- You have to bind the page path, which is a field in the collection, to the page path. This is the field that will be used to generate the URL of the page. For example, if you have a collection of products, and you want to create a page for each product, you can bind the page path field to the product name field. This way, the URL of the page will be https://your-app.com/product-name.

`static`
`page path`
`page path`
`product name`
`https://your-app.com/product-name`
Then, on every element or workflow in this page, you'll be able to access the data of the item that is currently displayed:

(here, we show you how to bind a title, and we've done the same for the domain and the image, hence the final result)


## Link to a static collection page ​

First of all, you can link to a static collection page from any collection list that uses the same collection.

Indeed, WeWeb will automatically know to which instance of the static collection page to redirect to, based on the element in the collection list the user clicked on.

Let's see how to do it:

