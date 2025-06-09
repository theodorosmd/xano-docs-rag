# Deployments ​


# Deployments ​

In the Deployments tab, you will be able to:

`Deployments`
- publish your app,
- preview a previous version of the Editor,
- rollback to a previous version of the Editor.


## Editor ​

This is where you can see all the automatic and manual backups of your project's Editor:



Let's take a look at all the information and functionalities we have on this screen.


### 1. Pending commits ​

In the example above, there are "7 pending commits". This means that the Editor was backed-up 7 times without the project being published.


### 2. Automatic commits ​

WeWeb generates automatic backups of your project Editor:

- every 24 hours if you're on a Starter plan,
- every hour if you're on a Scale or Enterprise plan, and
- every time you publish your app in staging or in production.


### 3. Manual commits ​

You can create a manual commit of the Editor with a custom message to describe the update by going to the Commit button inside the Editor:

`Commit`



### 4. Publish ​

When you click on the Publish to staging or Publish to production button, WeWeb will publish your app in the current version of the Editor.

`Publish to staging`
`Publish to production`
Afterwards, there will be "No pending commits":




### 5. Preview ​

If you want to rollback to a previous version of the Editor, you can click on Preview to open the Editor in a read-only mode.

`Preview`

### 6. Rollback editor ​

Once you are confident you have identified the version of the Editor you want to restore, you can click on Rollback editor.

`Rollback editor`

## Staging ​

If you're on a Scale or Enterprise plan, this is where you can see the different versions of the application published on the staging environment.

In the example below, you can see:

- we published version 3 of our app,
- on the staging environment, and
- have the option to promote it to production.




## Production ​

This is where you can see the different versions of the application published in production.

If you're on a Scale or Enterprise plan, you will have the option to rollback to a previous version of the app in production:



TIP

If you're on a yearly plan, you will be able to download project files:



Learn more about exporting and self-hosting an app built in WeWeb.


## Error Logging ​

For production applications, it's important to implement error logging to help monitor and debug issues. You can integrate external error logging services like Sentry with your WeWeb application.

While we'll be providing more detailed documentation on error logging in the future, you can refer to this community forum post for an example of how to implement error logging with Sentry in your WeWeb application.

