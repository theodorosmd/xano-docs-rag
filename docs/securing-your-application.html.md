# Authentication and security ​


# Authentication and security ​

As you build your application, you'll need to consider how to secure it and protect your data. This guide will introduce the fundamental concepts of security in WeWeb applications, including authentication, restricting page access, and understanding frontend visibility.


## Understanding authentication ​

Authentication is the process of verifying a user's identity—making sure they are who they claim to be. In WeWeb, you'll use an authentication plugin to:

- allow users to sign up and log in
- verify user identities
- restrict access to certain content
- personalize experiences based on user data

Before implementing security features, you'll need to add an authentication plugin through the Plugins menu:

- click on Plugins in the top navigation
- select Authentication
- choose an authentication provider (Supabase, Xano, etc.)
- configure the plugin according to your backend setup

`Plugins`
`Authentication`

## Creating private pages ​

One of the simplest ways to control content access is to make pages private—accessible only to authenticated users or users with specific roles. However, it's important to understand that private pages are primarily a UX feature rather than a complete security measure.


### Setting page access ​

To restrict page access:

- select a page in the Pages panel
- look for the Private access setting under Page properties
- choose from these options: public - accessible to everyoneauthenticated users - requires loginuser groups - requires specific roles
- public - accessible to everyone
- authenticated users - requires login
- user groups - requires specific roles

`Private access`
- public - accessible to everyone
- authenticated users - requires login
- user groups - requires specific roles



ALWAYS SECURE YOUR BACKEND

While private pages create a better user experience by preventing unauthorized navigation to restricted content, they do not provide complete security. You must still secure your backend APIs and data sources, as technically savvy users could attempt to bypass frontend restrictions.


### Working with user groups ​

If your application has different types of users (like admins, editors, or subscribers), you can create user groups based on roles:

- set up roles in your backend (Supabase, Xano, etc.)
- configure the roles connection in your authentication plugin
- create user groups in WeWeb based on these roles
- restrict page access to specific groups

WARNING

When using multiple roles for a user group, users must have ALL the defined roles to be considered members of that group. For example, if a group requires both "Customer" and "Premium" roles, users must have both roles assigned.

Learn more about private pages and user groups →


## Conditional display vs. rendering ​

WeWeb offers two different ways to control what users see based on conditions like authentication status, user roles, or other variables:


### Conditional display ​

The standard approach uses CSS's display property to hide elements:

`display`
- select an element
- in the Styling panel, find the display property
- bind it to a condition (e.g., if(user.role = 'admin', true, false))

`display`
`if(user.role = 'admin', true, false)`
This approach is simple but has limitations:

- the element is still loaded in the browser, just hidden visually
- the data within the element is still accessible in the browser's developer tools
- this is a UI convenience, not a security measure


### Conditional rendering ​

For better performance and security, use conditional rendering:

- select an element
- go to the Settings panel
- find the Conditional Rendering option
- set a condition for when the element should be rendered



The key advantage is that conditionally rendered elements are not included in the DOM at all until the condition is met—making your app more efficient and slightly more secure.

WHAT IS THE DOM?

The DOM (Document Object Model) is simply the browser's element tree - a structured representation of all elements on your webpage. When something is "in the DOM," it exists in this tree and takes up browser resources, even if it's hidden from view. When something is "not in the DOM," it doesn't exist in the browser's element tree at all until the condition is met to add it.

Learn more about conditional rendering vs display →


## Frontend security fundamentals ​

It's crucial to understand that frontend security has inherent limitations:


### All frontend data is accessible ​

A fundamental rule of web security: any data that's loaded into the browser can be viewed by users with technical knowledge, regardless of how you handle its display:

- Even if the data isn't shown: Data loaded into your application but not displayed in any UI element is still accessible through browser developer tools
- Even with conditional rendering: While conditional rendering prevents elements from being added to the DOM, any data used in the element itself will still be available in memory or network responses if it was fetched from your backend
- Even if you filter data client-side: If you load a complete dataset from your backend and only perform filtering in WeWeb, all of that data is still accessible in the browser

Even if the data isn't shown: Data loaded into your application but not displayed in any UI element is still accessible through browser developer tools

Even with conditional rendering: While conditional rendering prevents elements from being added to the DOM, any data used in the element itself will still be available in memory or network responses if it was fetched from your backend

Even if you filter data client-side: If you load a complete dataset from your backend and only perform filtering in WeWeb, all of that data is still accessible in the browser

Users with technical knowledge can access this data through:

- Browser developer tools to inspect network responses
- JavaScript console to examine application variables and state
- Network monitoring to see all data transferred to the browser


### Best practices for frontend security ​

To properly secure your application:

- Never rely solely on frontend restrictionshiding buttons doesn't prevent API callsfrontend validations can be bypassedprivate pages only prevent navigation but don't secure data
- hiding buttons doesn't prevent API calls
- frontend validations can be bypassed
- private pages only prevent navigation but don't secure data
- Always secure your backendimplement proper authentication and authorization on your API endpointsvalidate permissions on every data requestuse row-level security or role based access in your database when available
- implement proper authentication and authorization on your API endpoints
- validate permissions on every data request
- use row-level security or role based access in your database when available

Never rely solely on frontend restrictions

- hiding buttons doesn't prevent API calls
- frontend validations can be bypassed
- private pages only prevent navigation but don't secure data

Always secure your backend

- implement proper authentication and authorization on your API endpoints
- validate permissions on every data request
- use row-level security or role based access in your database when available

AUTHENTICATION DOCUMENTATION

For detailed instructions on setting up proper authentication and authorization:

- Supabase authentication documentation
- Xano authentication documentation

If you're using a different authentication system, refer to its documentation for implementing secure backend practices.

- Limit what data you fetchonly fetch data the current user should have access tofilter sensitive data on the backend before sending it to the browsernever load sensitive data "just in case" it might be needed
- only fetch data the current user should have access to
- filter sensitive data on the backend before sending it to the browser
- never load sensitive data "just in case" it might be needed
- Use JWT tokens or similar mechanismsauthenticate API requests with secure tokensset appropriate token expiration timesimplement proper token refresh mechanisms
- authenticate API requests with secure tokens
- set appropriate token expiration times
- implement proper token refresh mechanisms

Limit what data you fetch

- only fetch data the current user should have access to
- filter sensitive data on the backend before sending it to the browser
- never load sensitive data "just in case" it might be needed

Use JWT tokens or similar mechanisms

- authenticate API requests with secure tokens
- set appropriate token expiration times
- implement proper token refresh mechanisms

BUILT-IN SECURITY

WeWeb's authentication plugins for Supabase, Xano, and other backends automatically handle JWT tokens, token expiration, and refreshing behind the scenes. However, implementing proper row-level security and role-based access controls still requires configuration in your backend. Refer to your backend provider's documentation for these security implementations.


## Implementing security in WeWeb ​

Let's look at some practical examples of how to implement security in your WeWeb application:


### Example 1: Secure data fetching ​

When fetching user-specific data:

AVOID THIS (insecure):

- Collection: Get all orders, then filter in WeWeb for current user

DO THIS INSTEAD (secure):

- Collection: Call a backend endpoint that only returns the current user's orders based on their authentication token


### Example 2: Role-based UI elements ​

For displaying elements based on user roles:

For a delete button that only admins should see:

- Conditional Rendering: user.role = 'admin'

`user.role = 'admin'`
Important reminder: Also secure the delete API endpoint on your backend!


### Example 3: Private content sections ​

For sections with sensitive information:

To limit visibility of a dashboard component to premium users:

- Conditional Rendering: user.subscriptionTier = 'premium'

`user.subscriptionTier = 'premium'`
Important reminder: The backend API providing the premium data must also verify the user's subscription status before returning data


## Understanding data security in bindings ​

When working with WeWeb's binding system, it's important to understand its security implications:

Every piece of data available in the binding menu is accessible to users through browser developer tools, with only one exception: the authenticated user data from authentication plugins.

- collection data: All data fetched through collections is visible in network requests
- variables: All variables created in WeWeb are accessible in the browser's memory
- page data: All page parameters and state information is visible
- local storage: All data stored in browser storage is accessible

You should always consider this when deciding what data to fetch and store in your application. If something truly needs to be kept confidential, it should never be sent to the browser in the first place.

REMEMEBER: The only secure data is user authentication information:


## Common security pitfalls ​

Be careful to avoid these common security mistakes:

- checking roles only in the UI: Always verify permissions on both frontend and backend
- storing sensitive data in browser storage: Avoid storing passwords or sensitive information in local storage or session storage
- loading all data at once: This can expose information users shouldn't see
- hardcoding API keys: Never include secret keys or credentials in your frontend code
- relying solely on private pages: Remember that private pages only control navigation, not data access


## Conclusion ​

Security is a multi-layered concern that requires attention on both frontend and backend. While WeWeb provides tools like private pages and conditional rendering to create appropriate user experiences, true security must be implemented on your backend systems.

Remember this key principle: The browser is in the user's control, not yours. Anything that reaches the browser can potentially be accessed by users with technical knowledge, so always secure your data at the source.

CONTINUE LEARNING

Now that you've learned how to secure your application, the final step is to publish it so others can use it:

Publishing your application →

