# Segment ​


# Segment ​

Segment is platform that simplifies the management of tracking codes and tags on websites, enabling efficient data collection and integration with analytics and marketing tools.

The Segment plugin in WeWeb allows for easy integration in any WeWeb project, and to trigger tracking events from no-code workflows.

With the Segment plugin, you can:

- Track pageviews of your web app in a fgew clicks,
- Trigger custom events from no-code workflows
- Identify users from no-code workflows


## Add plugin to project ​

To add Segment to your project, go to Plugins > Extensions:

`Plugins`
`Extensions`


Then, you’ll be prompted to enter your project write key:

`write key`


You'll find your write key in your Segment project snippet. Indeed, you need to use a JavaScript source in Segment to use in a WeWeb app:

`write key`


Once saved, the Segment plugin is now added to your project!


## Use plugin in workflows ​

Pageviews are tracked by default, nothing to do on your side.

TIP

Only the first pageview will be triggered in the editor, as the app is not triggering « real » page changes. But when published in staging or production, all page changes will trigger.

To track user interactions, you can use the Track action in workflows:

`Track`


The only required parameter for this action is the event name. You can add as many key/value pairs as you want, which are bindable (you can also bind the whole object).

`event name`


This object will be sent to Segment as the properties object of the event. You can test your events in the editor, and you’ll see them in the Segment debugger:

`properties`


To track user logins and signups, you can use the Identify action in workflows. The only required parameter for this action is the user id, but you can also add as many key/value pairs as you want, which are bindable (you can also bind the whole object).

`Identify`
`user id`
What we would recommend is to login the user using the Login action, and then identify the user using the Identify action, so that you can actually use the current user data to do your bindings:

`Login`
`Identify`


TIP

Once identified, the user will be identified on all pages, and all events will be sent with the user id. No need to use identify on every page. Just use it during the login/signup process.

For the other events, such as alias or screen, the process is the same. You can refer to Segment's docs for more information on these events.

`alias`
`screen`
