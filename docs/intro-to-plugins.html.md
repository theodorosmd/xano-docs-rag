# Intro to plugins ​


# Intro to plugins ​

Plugins are native integrations developed by WeWeb, designed to help you extend your app's functionality by seamlessly connecting to third-party services or adding custom features.

TIP

While plugins are incredibly helpful, they are not mandatory. If a specific plugin for your desired service doesn't exist, you can still connect to it using REST APIs, GraphQL or more. This flexibility ensures that you can integrate with virtually any service, even if it doesn't have a dedicated plugin.

They are available under 3 categories:

- Data sources are used to interact with data through third-party services like Xano, Supabase, a REST API, etc.
- Authentication are used to authenticate users in your app through third-party services like your company's bespoke token-based auth, OpenID, Xano Auth, etc.
- Extensions are used to add custom features to your app like maps, charts, payments, etc.

`Data sources`
`Authentication`
`Extensions`

## How to add a Plugin ​

To add a plugin, go to Plugins, select a plugin category and the plugin you want to add, then click on the Add button:

`Plugins`
`Add`


Notice that, when the Plugins panel is open, you will find:

`Plugins`
- the list of installed plugins (which you can click on to configure or remove),
- the list of all available plugins by category, and when applicable,
- a help text to learn more about the plugin currently selected




## Available Plugins ​

Here is a list of all the available plugins inside WeWeb.


### Data sources ​

The data sources are the plugins that you can use to connect to third party services, and to fetch data from them. You can find them under the Data sources tab.

`Data sources`
Currently available data source plugins include:

- Supabase: to connect to a Supabase database. Documentation is available here.
- REST API: to connect to any REST API. Documentation is available here.
- Xano: to connect to a Xano database. Documentation is available here.
- Airtable: to connect to an Airtable base. Documentation is available here.
- Google Sheets: to connect to a Google Spreadsheet.
- SQL: to connect to a SQL database. Documentation is available here
- JavaScript: to connect to APIs using JavaScript and the Axios library.
- GraphQL: to connect to a GraphQL API.
- SOAP: to connect to a SOAP API.
- RSS Feed: to connect to an RSS Feed.
- Algolia: to connect to an Algolia index. Documentation is available here.
- Strapi: to connect to a Strapi content management system.
- Ghost: to connect to a Ghost content management system.

`Supabase`
`REST API`
`Xano`
`Airtable`
`Google Sheets`
`SQL`
`JavaScript`
`GraphQL`
`SOAP`
`RSS Feed`
`Algolia`
`Strapi`
`Ghost`
TIP

You can connect multiple data sources to the same WeWeb project


### Authentication ​

The authentication plugins are the plugins that you can use to connect to third party services, and to authenticate users in your app. You can find them under the Authentication tab.

`Authentication`
Currently available authentication plugins include:

- Xano Auth: to use Xano as your authentication provider. Documentation is available here.
- WeWeb Auth: to use WeWeb's own authentication built on top of AWS Cognito. Documentation is available here.
- Supabase Auth: to use Supabase as your authentication provider. Documentation is available here.
- Auth0: to use Auth0 as your authentication provider. Documentation is available here.
- Token Based Auth: to connect to any API using a token based authentication system. Documentation is available here.
- OpenID: to use the OpenID protocol to connect to any OpenID provider.

`Xano Auth`
`WeWeb Auth`
`Supabase Auth`
`Auth0`
`Token Based Auth`
`OpenID`
WARNING

You can only have one authentication plugin per app.


### Extensions ​

The extensions are the plugins that you can use to add custom features to your app. You can find them under the Extensions tab.

`Extensions`
Currently available extension plugins include:

- Date: to add date-related elements to your app (like a date picker, a date range picker, etc), and formulas to manipulate dates based on the DayJS library.
- Charts: to add charts to your app. Based on the ChartJS library. Documentation is available here.
- PWA: to enhance your web applications with Progressive Web App features like device motion sensors, notifications, geolocation, native sharing, and vibration capabilities. Documentation is available here.
- Stripe: to add Stripe payments to your app. Documentation is available here.
- Mapbox: to add a Mapbox map to your app. Documentation is available here.
- WeWeb Email: to send emails from your app using our own email service.
- CSV: to export data from your app to a CSV file.
- Google: to add Google-related elements to your app (Google Maps, reCAPTCHAs, etc). Documentation for Google Maps is available here.
- Youtube: to embed Youtube videos in your app.
- Calendly: to embed Calendly calendars in your app.
- Segment: to use Segment as your analytics provider in your app.
- Vimeo: to embed Vimeo videos in your app.
- Typeform: to embed Typeform forms in your app.
- Snipcart: to use Snipcart as your e-commerce provider in your app.
- Dailymotion: to embed Dailymotion videos in your app.
- Twitch: to embed Twitch videos in your app.

`Date`
`Charts`
`PWA`
`Stripe`
`Mapbox`
`WeWeb Email`
`CSV`
`Google`
`Youtube`
`Calendly`
`Segment`
`Vimeo`
`Typeform`
`Snipcart`
`Dailymotion`
`Twitch`

## Plugin configuration ​

To learn how to configure a plugin, please refer to each plugins' documentation (linked in the list above) or to the modal that will appear on the right when you add a plugin:



