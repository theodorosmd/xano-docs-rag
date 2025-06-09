# Navigation ​


# Navigation ​

Navigation is a system that enables users to move between different pages and sections of a website or application. You can think of it as the way users move around your web app - whether it's clicking a menu item to visit the Products page, using the back button to return to a previous page, or selecting a product to view its details. This is how users find and interact with different parts of your application.


## Understanding URL paths ​

URL paths are the addresses of your pages - what users see in their browser's address bar. Think of them as street addresses for your website - they help users find exactly where they want to go.


### Simple URLs ​

When you create a page in WeWeb, it automatically gets a simple URL. These URLs are straightforward and static, meaning they don't change.

For example, in the URL https://yourdomain.com/products:

`https://yourdomain.com/products`
- yourdomain.com is your domain (your website's main address)
- /products is the path to your specific page

`yourdomain.com`
`/products`
Some examples of simple URLs:

Path may only contain 'a-z', '0-9', '_', '-' and '/', and can only start and end with 'a-z' or '0-9'.


### Dynamic URLs ​

Sometimes you need URLs that can change based on what content you're showing. These are called dynamic URLs, and they use parameters to change parts of the URL.

For example, in https://yourdomain.com/products/category/smartphones:

`https://yourdomain.com/products/category/smartphones`
- /products/category is your base path (static part)
- /smartphones is a category parameter (dynamic part)

`/products/category`
`/smartphones`

## Setting up dynamic URLs ​

- Select your page from the Pages panel
- Click on "URL paths" in the page settings
- In the URL paths panel, you'll see: English unique path: This is where you set up your URL structureParameters: These are the parts of your URL that can change
- English unique path: This is where you set up your URL structure
- Parameters: These are the parts of your URL that can change

- English unique path: This is where you set up your URL structure
- Parameters: These are the parts of your URL that can change



TIP

A dynamic product page URL might look like:

- Template: products/category/{{param}}
- Real URL: products/category/smartphones
- Another URL: products/category/beauty
- Parameters always use double curly braces: {{parameterName}}
- Choose clear parameter names that describe their purpose
- You can test your dynamic URLs using the default values in the editor

Template: products/category/{{param}}

`products/category/{{param}}`
Real URL: products/category/smartphones

`products/category/smartphones`
Another URL: products/category/beauty

`products/category/beauty`
Parameters always use double curly braces: {{parameterName}}

`{{parameterName}}`
Choose clear parameter names that describe their purpose

You can test your dynamic URLs using the default values in the editor

"English unique path" is the URL structure for accessing content in English, letting you define custom routes for each language.

For example, if you were building a multi-language site, you might have:

- English path: /products/category/{{param}}
- French path: /produits/categorie/{{param}}
- Spanish path: /productos/categoria/{{param}}

`/products/category/{{param}}`
`/produits/categorie/{{param}}`
`/productos/categoria/{{param}}`
WARNING

A page might work when previewing it in the editor in French, but will fail when visitors try to access it in English if you haven't created the English content version. Learn more about page languages:

TIP

✅ Dynamic URLs are better for:

- Product pages that change based on category or brand
- Blog posts with different articles
- User profiles
- Search results pages


### Retrieve URL parameter value ​

Once you have defined URL parameters in your page settings, you can access them through WeWeb's Variables tab in the Formula editor. These parameters automatically update based on the URL, allowing you to fetch data for specific items, show or hide content based on the current value, filter collections and control component visibility.



For example, if your URL is /products/category/{{param}}, you can use the parameter to fetch and display only products from that category:

`/products/category/{{param}}`


TIP

- URL paths are only available on the page where you create them
- The Home page cannot have URL paths. To handle URLs like mydomain.com/1:

- Create a regular page (e.g., "Main") with URL path {{id}}
- Add workflow "On page load" to Home
- Use Navigate to action to redirect to Main page

`{{id}}`
`Navigate to`
Example:

- User visits: mydomain.com (Home)
- Auto-redirects to: mydomain.com/1 (Main page)
- Users can now access mydomain.com/2, mydomain.com/3, etc.


## Navigation Methods ​

TIP

Consider using Multi-page sections for improved navigation performance

When navigating between pages, consider implementing multi-page sections to improve the performance of page transitions. Multi-page sections allow you to preload content from other pages, resulting in smoother transitions and faster loading times. This is especially beneficial for frequently accessed pages or when you want to create a seamless user experience.

You can learn more about multi-page sections in their dedicated documentation.

Now that you understand how URLs work in WeWeb, let's look at the three ways to navigate between pages:


### Link ​

The most common way to navigate is using the Link to property. This creates regular links that users can click on, just like standard website links. It's perfect for navigation menus, buttons, and any clickable elements.

`Link to`
For example, if you have a products page with URL parameters set up (/products/category/{{param}}), you can create links to specific categories:

`/products/category/{{param}}`
- Select any element you want to make clickable
- In the Settings tab, find the Link section
- Choose the target page
- Add any URL parameters needed:

`Link`


Assuming you are using the URL path in an API request to fetch a collection, you will get different results:




#### Link properties ​

`param`
TIP

- Disable the Preserve collection on navigation property so the collection can be "reset" when you navigate. Otherwise, your collection might show stale data from the previous page.
- You do not need to reset URL paths. This is all done by WeWeb automatically.

`Preserve collection on navigation`

### Navigate to workflow action ​

Sometimes you need navigation to happen automatically, like after a form submission or when certain conditions are met. This is where the Navigate to action comes in.

Instead of waiting for a user to click, the Navigate to workflow action can be triggered by:

`Navigate to`
- Form submissions
- API responses
- Button clicks with additional logic
- Workflow completions




#### Properties ​

`param`
ACTIONS AFTER NAVIGATION

Any workflow actions placed after a Navigate to action that takes the user away from the current page will not execute. When navigation occurs to a different page, the current workflow is interrupted and stopped.

`Navigate to`
If you need to perform actions after navigation, consider:

- Placing those actions before the Navigate to action
- Using the destination page's On page load trigger to execute actions after navigation
- Opening the navigation in a new tab if you need the current workflow to continue

`Navigate to`
`On page load`

### Navigate to the previous page ​

Allows users to go back to their previous page, similar to clicking the browser's back button. This is useful for:

- "Back" buttons after form submissions
- "Return to previous page" links
- Cancel buttons that return users to where they came from



You can set a default redirect page (like Home) that users will go to if there's no previous page in their history.

TIP

A workflow is a series of actions that happen in response to a trigger. You can learn more about workflow actions here.

TIP

Link to vs Navigate to

Link to

`Link to`
- Creates HTML <a> tags in the published app - better for SEO and accessibility
- Use for navigation menus and clickable elements
- Adds "Active link" state to the target element

`<a>`
Navigate to

`Navigate to`
- Uses JavaScript navigation - less optimal for SEO and accessibility
- More flexible for workflow automation and programmatic navigation

WARNING

Avoid setting both Link to property and Navigate to action on the same element - this can cause navigation conflicts in the editor.

`Link to`
`Navigate to`

## Binding The Link Property ​

In order to bind the Link property, you must create an object with the appropriate key value pairs.

`Link`
TIP

To see the UID of elements, sections, and pages, you must first enable Show dev information in the Development settings of the editor. To do so:

`Show dev information`
`Development`
- Open the More menu and press Development
- Press Show dev information

`More`
`Development`
`Show dev information`

### Linking to Page ​

If you wish to link to a page, the following keys and values can be passed:

`internal`
`{{your_page_id}}`
`{{your_section_id}}`
`true`
`false`
`{'param_1': 'value_1'}`
`{'query_1': 'value_1'}`
`true`
`false`
`{{hex_color}}`
Here is an example of what a link would look like when using the standard UI vs binding its value:


### Linking to External URL ​

If you wish to link to an external URL, the following keys and values can be passed:

`external`
`{{url_to_link_to}}`
`true`
`false`

### Linking to File Download ​

If you wish to link to a file download, the following keys and values can be passed:

`file`

### Linking to Email ​

If you wish to link to an email, the following keys and values can be passed:

`mail`
`{{email_to_link_to}}`

### Linking to Phone Number ​

If you wish to link to a phone number, the following keys and values can be passed:

`mail`
`{{phone_number_to_link_to}}`

## Queries ​

URLs in WeWeb can have two types of parameters:

- Path parameters: /products/category/{{param}}
- Query parameters: /products?category=electronics

`/products/category/{{param}}`
`/products?category=electronics`
Query variables automatically capture and store URL query parameters. When you navigate to a page with query parameters, the corresponding query variables update to match the values in the URL.

Here's how they work:

- Create a query variable (e.g., searchTerm)
- Add it to the Queries property during navigation:

`searchTerm`
`Queries`
- Name: "searchTerm"
- Value: "smartphones"

The URL will update (e.g., yourpage?searchTerm=smartphones) and the query variable searchTerm automatically updates to "smartphones".

`yourpage?searchTerm=smartphones`
You can use these variables anywhere in your app without writing any code!

To modify the query programatically, you can also use the Change variable value workflow action.

TIP

You might need query parameters for reset password flows. For example:

- User clicks reset password link: myapp.com/reset-password?token=abc123
- The token query parameter is automatically captured by a query variable
- Your app can then use this variable to validate the reset password request

`myapp.com/reset-password?token=abc123`
Query parameters are also perfect for sort and filter features, just like YouTube's video timestamp sharing (e.g., youtube.com/watch?v=123&t=150). Users can share links/filtered views by simply copying the URL (e.g., products?sort=price_desc&category=phones). The & symbol in URLs is used to separate multiple query parameters.

`youtube.com/watch?v=123&t=150`
`products?sort=price_desc&category=phones`
`&`

## SPA Navigation ​

A Single Page Application (SPA) works like a desktop app in your browser - instead of loading entire new pages when you click around, it just updates the parts that need to change.


### Same page navigation ​

When navigating to the same page in WeWeb:

- Editor: Page will reload for preview purposes
- Published app: No page reload, content updates smoothly

To navigate to the same page to avoid page reloads in the published app, simply select the current page on navigation:



Now, in the published app, this is what will happen:



TIP

Navigating to the same page will trigger a page reload in the editor, but not in the published app, which is great for SPA navigation.

WARNING

Balance SPA navigation with dedicated pages

While SPA navigation can provide a smooth transition and improved user experience, it's important to create dedicated pages for distinct sections of your application. Sections like account settings and sign-in pages should generally be implemented as separate pages rather than all within a single page. Building too much on a single page can lead to difficulties in maintaining and scaling the page as more and more is built on the page.

Use SPA-style same-page navigation for smaller UI updates and transitions, but rely on dedicated pages for major functional areas of your application.


## wwParams ​

When navigating in the editor, you might notice wwParam appearing in your URLs. Don't worry - this is normal and only happens in the editor, not your published site. Here's why:

`wwParam `
The WeWeb editor has two separate windows running at the same time:

- The editor window, where you see all your tools and settings
- A preview window (iframe) - where you see how your app looks

These windows need different kinds of information:

- The editor needs to know about your project settings, tools, etc.
- The preview needs to show your actual app


### Why wwParams exists ​

When you navigate in your app using parameters (like /products/shoes):

`/products/shoes`
- The editor needs to know about this navigation
- The preview needs to show the right content
- Both windows need to stay in sync

wwParams is WeWeb's solution to keep these two windows synchronized. It ensures that when you change pages or parameters in one window, the other window updates automatically to match.

`wwParams`
In your published site, wwParams isn't needed because there's only one window. It's just a tool to help during development.

`wwParams`
WARNING

OAuth Testing

When implementing OAuth or any authentication with URL redirects, make sure to add both your published URL and editor URL to your OAuth provider's allowed redirect URLs. This ensures the authentication service works in both environments.


## Current page data ​

The CurrentPage object helps you access information about the page you're currently on. You can use it in formulas and workflows to get details about your page.

`CurrentPage`



### Common properties ​

`CurrentPage.name`
`CurrentPage.id`
`CurrentPage.path`
`CurrentPage.lang`

### Status properties ​


### Additional properties ​

- paths: contains URL path information
- langs: available language versions
- meta: page meta information
- title: page title information
- sections: page sections
- pageUserGroups: access control groups

`paths`
`langs`
`meta`
`title`
`sections`
`pageUserGroups`
TIP

This is useful for:

- Display different content based on page name (e.g., "Welcome to " + CurrentPage.name)
- Create dynamic navigation text (e.g., If(CurrentPage.name = "Cart", then "Back" else "Cart")
- Handle multiple languages (e.g., If(CurrentPage.lang = "en" then "Buy" else "Acheter")
- Show/hide elements on specific pages (e.g., If CurrentPage.name != "Contact")
- Create dynamic text combining page data (e.g., CurrentPage.name + " - " + CurrentPage.path)

`"Welcome to " + CurrentPage.name`
`If(CurrentPage.name = "Cart", then "Back" else "Cart"`
`If(CurrentPage.lang = "en" then "Buy" else "Acheter"`
`If CurrentPage.name != "Contact"`
`CurrentPage.name + " - " + CurrentPage.path`

## Frequently Asked Questions ​

Use the Link to property instead of the Navigate to workflow action. The Link to property creates HTML <a> tags in your published app, which support native browser behaviors like right-clicking to open in a new tab, showing link previews on hover, and being recognized by screen readers.

`Link to`
`Navigate to`
`Link to`
`<a>`
The Navigate to workflow action uses JavaScript navigation instead, which doesn't support these native browser features.

`Navigate to`
You have two main options for passing data between pages during navigation:

- URL Parameters: For data that should be visible in the URLSet up URL parameters in your page settings (e.g., /products/{{productId}})Pass values when navigating using the Parameters propertyAccess these values on the destination page via URL parameters in the Variables panel
- Set up URL parameters in your page settings (e.g., /products/{{productId}})
- Pass values when navigating using the Parameters property
- Access these values on the destination page via URL parameters in the Variables panel
- Query Parameters: For optional data or filteringCreate query variables in your destination pageAdd queries when navigating (e.g., ?sort=price_asc&filter=inStock)Access these values on the destination page via Query variables
- Create query variables in your destination page
- Add queries when navigating (e.g., ?sort=price_asc&filter=inStock)
- Access these values on the destination page via Query variables

URL Parameters: For data that should be visible in the URL

- Set up URL parameters in your page settings (e.g., /products/{{productId}})
- Pass values when navigating using the Parameters property
- Access these values on the destination page via URL parameters in the Variables panel

`/products/{{productId}}`
Query Parameters: For optional data or filtering

- Create query variables in your destination page
- Add queries when navigating (e.g., ?sort=price_asc&filter=inStock)
- Access these values on the destination page via Query variables

`?sort=price_asc&filter=inStock`
For larger data sets or sensitive information, consider using browser storage:

- Page Storage: Persists only during the current session
- Local Storage: Persists between sessions until explicitly cleared

To create a back button:

- Add a button element to your page
- Add a workflow with the "On click" trigger
- Add the "Navigate to previous page" action
- Optionally, set a default page (like Home) that users will go to if there's no previous page in their history

This works similarly to clicking the browser's back button but gives you more control over the user experience.

The wwParam parameter is WeWeb's solution for keeping the editor environment and preview window synchronized. It only appears in the editor and never in your published application.

`wwParam`
It exists because:

- The editor has two separate windows (editor tools and preview) that need to stay in sync
- When you navigate with parameters, both windows need to know about the change
- wwParams helps pass this information between the editor and preview

`wwParams`
Your users will never see these parameters in the published application, so you don't need to worry about them affecting your URL structure or SEO.

For smooth, SPA-style navigation to the same page:

- Use either the Link to property or Navigate to workflow action
- Select the current page as the destination
- Set any needed parameters or queries

`Link to`
`Navigate to`
While the editor will still reload the page for preview purposes, your published application will update the URL and content without a full page reload, creating a smoother user experience.

This approach is ideal for filtering collections, tab-like interfaces, or any scenario where you want to update the URL without interrupting the user experience.

