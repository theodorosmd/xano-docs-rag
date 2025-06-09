# Google Tag Manager ​


# Google Tag Manager ​

Google Tag Manager is a platform that simplifies the management of tracking codes and tags on websites. It's helpful to collect data and integrate with analytics and marketing tools.

With the Google Tag Manager plugin, you can:

- track page views of your web-app in a few clicks, and
- trigger custom tracking events from no-code workflows.


## Add plugin to project ​

To add Google Tag Manager to your WeWeb app, go to Plugins > Extensions:

`Plugins`
`Extensions`


Then, you’ll be prompted to enter your Tag Manager Container IDs:



You can enter one container ID per environment if you want to use different Google Tag Manager containers for you app while in the editor, on your staging app or on the production app.

Only the production container ID is mandatory. If you don’t set IDs for the editor and for staging, they will use the production ID.

To find your Google Tag Manager ID, search for it in the upper-right corner while on the Tag Manager page:



Once saved, the Google Tag Manager plugin is now added to your project!


## Track pageviews ​

Once you've configured the Google Tag Manager plugin, pageviews will be tracked by default, nothing to do on your side.

TIP

Only the first pageview will be triggered in the editor, as the app is not triggering "real" page changes. But when published in staging or production, all page changes will trigger.


## Track custom events ​

To track other user interactions, you can use the Push Event action in workflows:

`Push Event`


In the action, you’ll be able to add as many key/values pairs as you want, which are bindable (you can also bind the whole object).

This object will be added in the Google Tag Manager’s dataLayer that you’ll be able to use as a trigger and variables in the Tag Manager instance:





TIP

The dataLayer is an array which is added to the window objects inside your project. What Google Tag Manager does is to listen to any object added to this array (what WeWeb's plugin action does).

`window`
You can learn more about the dataLayer:

- in Google's developer documentation, and
- through this Analytics mania tutorial

