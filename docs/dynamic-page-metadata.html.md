# Metadata for dynamic pages ​


# Metadata for dynamic pages ​


## Use case ​

When creating dynamic pages in WeWeb, such as www.myapp.com/article/1, all pages share the same metadata configured in the Editor:

`www.myapp.com/article/1`


However, depending on your use case, you may need different metadata (title, description, keywords, and thumbnails) for each page based on the URL parameter (e.g. for example a unique blog article slug, product id, or event id).

In the videos below, we'll show you how to deploy dynamic metadata for your dynamic collection pages in a way that follows best-in-class SEO standards.

WARNING

This is an advanced technical workaround for cases where you don't want to use static collections. Since this isn't WeWeb's primary use case, we don't provide official support for this implementation.


## Benefits and pre-requisites ​


## WeWeb setup ​


## Backend setup ​

TIP

In the video above, we are using Xano as an example but similar logic applies no matter what backend you are working with.

What's important is that you have an API endpoint that returns page metadata in the following format:

```
{
  "title": "Festival",
  "description": "Test Our annual festival is back, promising an array of activities for every age and interest. From thrilling amusement rides and live performances to a marketplace brimming with handcrafted goods, there's joy and discovery around every corner. Learn from artisans during workshops, indulge in diverse culinary delights, and immerse yourself in the festive atmosphere that celebrates our community's spirit.",
  "image": "https://xeo6-2sgh-ehgj.n7.xano.io/vault/UUJkO96O/eQbZuT4a7I7Iks60ScIyEXlKZ-s/u16buw../hanny-naibaho-aWXVxy8BSzc-unsplash.jpg",
  "keywords": "festival music live"
}
```

`{
  "title": "Festival",
  "description": "Test Our annual festival is back, promising an array of activities for every age and interest. From thrilling amusement rides and live performances to a marketplace brimming with handcrafted goods, there's joy and discovery around every corner. Learn from artisans during workshops, indulge in diverse culinary delights, and immerse yourself in the festive atmosphere that celebrates our community's spirit.",
  "image": "https://xeo6-2sgh-ehgj.n7.xano.io/vault/UUJkO96O/eQbZuT4a7I7Iks60ScIyEXlKZ-s/u16buw../hanny-naibaho-aWXVxy8BSzc-unsplash.jpg",
  "keywords": "festival music live"
}`

## Cloudflare setup ​


## GitHub setup ​

Here's the link to the GitHub repository you'll need to fork as described in the video below:

WARNING

Since we first recorded the video above, we updated the worker to support dynamic metadata on multiple pages, not just one.

This changes how you work with the config file of the worker.

In the first version of the worker shown in the video above, the patterns variable of the worker expected an object. Now, it expects an array of objects.

`patterns`
In the example below, we are configuring dynamic metadata for an event page and a team profile page:

```
export const config = {
  domainSource: "https://f69a71f6-9fd8-443b-a040-78beb5d404d4.weweb-preview.io", // Your WeWeb app preview link
  patterns: [
      {
          pattern: "/event/[^/]+",
          metaDataEndpoint: "https://xeo6-2sgh-ehgj.n7.xano.io/api:8wD10mRd/event/{id}/meta"
      },
      {
          pattern: "/team/profile/[^/]+",
          metaDataEndpoint: "https://xeo6-2sgh-ehgj.n7.xano.io/api:LjwxezTv/team/profile/{profile_id}/meta"
      }
      // Remove or add more patterns and their metadata endpoints as needed
  ]
};
```

`export const config = {
  domainSource: "https://f69a71f6-9fd8-443b-a040-78beb5d404d4.weweb-preview.io", // Your WeWeb app preview link
  patterns: [
      {
          pattern: "/event/[^/]+",
          metaDataEndpoint: "https://xeo6-2sgh-ehgj.n7.xano.io/api:8wD10mRd/event/{id}/meta"
      },
      {
          pattern: "/team/profile/[^/]+",
          metaDataEndpoint: "https://xeo6-2sgh-ehgj.n7.xano.io/api:LjwxezTv/team/profile/{profile_id}/meta"
      }
      // Remove or add more patterns and their metadata endpoints as needed
  ]
};`
This means that, even if you are only setting up dynamic metadata on one page, the patterns variable should be an array with one object inside.

`patterns`
In the example below, we are configuring dynamic metadata for only one page:

```
export const config = {
  domainSource: "https://f69a71f6-9fd8-443b-a040-78beb5d404d4.weweb-preview.io", // Your WeWeb app preview link
  patterns: [
      {
          pattern: "/event/[^/]+",
          metaDataEndpoint: "https://xeo6-2sgh-ehgj.n7.xano.io/api:8wD10mRd/event/{id}/meta"
      }
      // Add more patterns and their metadata endpoints as needed
  ]
};
```

`export const config = {
  domainSource: "https://f69a71f6-9fd8-443b-a040-78beb5d404d4.weweb-preview.io", // Your WeWeb app preview link
  patterns: [
      {
          pattern: "/event/[^/]+",
          metaDataEndpoint: "https://xeo6-2sgh-ehgj.n7.xano.io/api:8wD10mRd/event/{id}/meta"
      }
      // Add more patterns and their metadata endpoints as needed
  ]
};`

## Deploy & redirect ​

We're now ready to deploy our Cloudflare worker and redirect it to our custom domain name:


## Final checks ​

Alright, your app should be ready to go now. This tutorial being on the more technical side, don't hesitate to reach out in the WeWeb Community if you get stuck. We'll do our best to help out.

