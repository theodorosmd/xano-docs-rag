# Auth0 ​


# Auth0 ​


## Plugin configuration ​

To connect your Auth0 account to WeWeb, you’ll need 3 pieces of information:

- Your Auth0 Domain
- Your Auth0 Token
- A default application name

`Domain`
`Token`



### 1. Your Auth0 domain ​

- in Auth0, go to Applications > APIs
- copy the URL for your API audience
- paste it in WeWeb.

`Applications`
`APIs`

### 2. Your Auth0 token ​

- back on the Applications > APIs screen in Auth0
- click on Auth0 Management API > API explorer
- create a test application (if you don't have one already)
- copy the token and paste it in WeWeb

`Applications`
`APIs`
`Auth0 Management API`
`API explorer`



### 3. Default application name ​

By default, this will be the name of your WeWeb project but you can change it if you want to refer to a Single Page Application you created previously in your Auth0 workspace:




## Define redirections ​

In order for the signup, login, and sign out flows to work properly, you'll need to define pages where users are directed:

- after they signed in – for example a personalized dashboard
- after they log out or when they try to access a private page without being logged in – for example a login or a home page



WARNING

The Page to redirect after the user signed-in should be a public page. If you wish to redirect authenticated users to a private page, you should create and select an empty public page with a workflow triggered On page load that redirects them to the page of your choice.

`Page to redirect after the user signed-in`
`On page load`
This may seem strange but it's how third-party authentication works on the web: the browser needs to get a cookie from the auth provider, and read it before fetching the user and redirecting them to the chosen page. If you redirect to a private page, you'll get an error because the browser won't have had time to read the cookie and fetch the user before arriving on the private page. It needs a short stop on a public page first.


## Auth0 configuration ​

Once you have configured the Auth0 plugin in WeWeb, Auth0 will automatically create 2 applications which are both equally important to add authentication to your WeWeb project:

- a Machine to Machine application, named API Explorer Application
- a Single Page Application, named whatever you defined in the default application name above

`API Explorer Application`


TIP

If you don't have a Single Page Application in Auth0, we will create one for you automatically but if you already have one or more, we'll leave them.

`Single Page Application`

### Machine to Machine ​

Machine to Machine is a private application that allows Auth0 to communicate with the public application you publish. It's what allows your app to get the list of all available roles in Auth0 for example.

`Machine to Machine`
Make sure to give the Machine to Machine application permission to interact with your app:



WARNING

If you don't have a Machine to Machine application in Auth0, you will not have a token and will therefore not be able to setup the Auth0 plugin in WeWeb.

`Machine to Machine`

### Single Page Application ​

Single Page Application is a public application that allows the WeWeb app you published (or are consulting in preview mode inside the WeWeb Editor) to communicate with Auth0. For example, it's what allows users to signup, login, or get their info when they're logged.

`Single Page Application`
There are a few things you need to configure in the Settings of your Auth0 SPA to ensure users can signup, login, and sign out.

`Settings`
- Application Login URI: this should be the URL of a dedicated login page on your published application.
- Allowed Callback URLs: this should include the URLs where users are redirected after logging in (e.g. in preview mode and on the live app).
- Allowed Logout URLs: this should include the URLs where users are redirected after logging out (e.g. in preview mode and on the live app).
- Allowed Web Origins: this should include the domain name of your published app and https://editor.weweb.io so that you can test your user flows inside the WeWeb Editor.

`Application Login URI`
`Allowed Callback URLs`
`Allowed Logout URLs`
`Allowed Web Origins`
`https://editor.weweb.io`
TIP

We recommend including several URLs in each "Allowed" field:

- the relevant URLs inside the WeWeb Editor so you can test the Auth0 plugin while you're building, and
- the relevant URLs of your published app, so everything works live.


## Signup & login flows ​

You can allow new users to sign up or login to your app by triggering a workflow with one of the Auth0 Login actions with the Sign in or Sign up option enabled.

`Login`
`Sign in`
`Sign up`
In the example below, when a user clicks on a button on our page, an Auth0 popup will open and they will be invited to fill out their information to sign up to our app:



There's no other action required in the workflow. After signing up or logging in, the user will be redirected to the page defined in the Auth0 plugin configuration:



TIP

Don't hesitate to check your list of users in Auth0 to ensure your signup and login flows are working correctly. In the screenshot below, we can see our list of users and when they last logged in:




## Roles & permissions ​

In some cases, you'll want to restrict access to pages of your web-app based on roles & permissions.

In order to do this, there are a few steps to take:

- define roles in Auth0 (those will be automatically added to WeWeb via the plugin)
- create user groups in WeWeb and define what role or roles a user needs to be part of that group
- define what user groups are allowed to visit the page you want to gate


### 1. User roles in Auth0 ​

To define user groups in WeWeb, you first need to create user roles in Auth0 > User Management > Roles > Create Role

`Auth0`
`User Management`
`Roles`
`Create Role`


Then, you can assign roles to users in User Management > Users > Assign Roles

`User Management`
`Users`
`Assign Roles`


Once you have user roles in Auth0, you'll be able to see them in WeWeb:




### 2. User groups in WeWeb ​

Assuming you've added user roles in Auth0, you'll be able to create user groups in WeWeb and define what role(s) users need to have to be part of each group:



WARNING

When you add several roles to a user group, a user needs to have BOTH these roles. It's an AND statement, not OR.


## Restrict page access ​

By default, when you add a new empty page in your WeWeb app, everybody can access it, even users who have not signed in.

You can limit access to your WeWeb app at page level:

- go to the page settings > Private access
- restrict access to Authenticated users
- if applicable, select which authenticated user group(s) can access the page

`Private access`
`Authenticated users`



## Personalize UX ​

You can personalize the popup displayed to users when they signup or login in the Branding section of your Auth0 account:

`Branding`


