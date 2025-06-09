# Frequently Asked Questions ​


# Frequently Asked Questions ​

In this article, we aim to answer questions we get most often. If there's anything we haven't covered that you'd like answered, don't hesitate to start a conversation in the community.


## Backend ​


### Can WeWeb build my backend? ​

Yes. Thanks to our native integration with Supabase, you can now manage your backend from WeWeb.


### Does WeWeb work with other no-code backend tools? ​

Absolutely. We built WeWeb with the idea that it would seamlessly integrate with other popular and up and coming no-code tools. We regularly add new native integrations with other tools.

Don't hesitate to upvote or suggest new integrations.


## Scaling & Performance ​


### What are WeWeb's limits? ​

WeWeb allows you to design pixel-perfect UIs and add complex frontend logic. You can program visually while we write clean standard code under the hood. Therefore, anything you can do in a regular programming language (PHP, Javascript, etc.) you can do in WeWeb.

While we provide many features out of the box to help you build faster, you can also add custom code and import your own Vue.js components.


### What if I need more capacity outside my plan? ​

We've structured our plans to be optimized for the products we see most often. However, should you need more capacity outside of any plan, whether it be file storage, projects, team seats or custom development, you can contact sales.


## Data ownership, code export, and self-hosting ​


### Who owns my data? ​

You own your data. This also include any data that your users might upload unless your agreement with them specifies otherwise.


### Can I export my app and host it on-premise? ​

Yes! You can export and self-host the code of projects on a yearly subscription plan.


### Can I see the code that my WeWeb frontend is being hosted on? ​

Yes, you can see the code generated in your console and export the code of projects on a yearly subscription plan. However, you won’t be able to access the code of your project in your editor and live edit it.


### How and where is WeWeb hosted? ​

All our infrastructure runs on AWS, in Northern Virginia. Every project built with WeWeb is deployed on AWS Cloudfront (CDN).


### Can I import my HTML & CSS to WeWeb? ​

You can add custom code at project, page, and element level in WeWeb. You can also import custom Vue.js components in your projects, directly from your Github account. However, you will not be able to import a full web-app into WeWeb from code or other no-code tools.


### Can I migrate my frontend from another FaaS (Frontend as a Service) provider? ​

We currently do not have a way to import or migrate a frontend from another provider. This is largely because the infrastructure and format can drastically differ.


## API ​


### Can I make an external API request in WeWeb? ​

Yes. You can access and process an external API endpoint with WeWeb. You'll need to add the REST API plugin and either create a data collection (to get data) or a workflow (to interact with that data).


## Marketplace ​


### Will the Marketplace have templates that I can use to start my frontend with? ​

Yes, we are very excited to begin releasing templates for our users to use for their projects. We have many useful and exciting templates on our roadmap. We are also planning to open the Marketplace to our users so that they can build their own templates and offer them to other users.


### Can I develop an extension or template and sell it on the WeWeb Marketplace? ​

Very soon! A handful of users are alpha testing the Marketplace and have started developing and selling extensions and templates to other users.


## Pricing ​


### How much will WeWeb cost and how do I upgrade? ​

Pricing depends on which plan you choose. For detailed information on the cost of each plan and what is included, please visit https://weweb.io/pricing. In order to upgrade, please visit the Billing page in your WeWeb dashboard and select "Upgrade"


### What is the Basic & Advanced Roles & Permissions? ​

The Basic Roles & Permissions means that every authenticated user will have access to the same pages and app functionalities. The Advanced Roles & Permissions means that you can have different user groups with different permissions, so you could have an Admin role separate from Premium roles for example.


## Account ​


### Can I put a hold on or pause my account? ​

If you need to put a hold on things by canceling your subscription and wish to come back later, WeWeb can preserve your data for up to 90 days from the end of your subscription. You must contact support to do so. After you cancel, you will not be able to access your workspace. When you are ready to come back, you must contact support again and re-initiate payment on your subscription to access your workspace. After the 90 day grace period your data and workspace could be lost and you may have to start over from scratch.


### Can I get a refund on my paid plan? ​

WeWeb does not allow refunds of any kind on its monthly paid plans. You can choose to cancel or downgrade your Workspace and/or Project subscriptions at any time.


#### To downgrade a Workspace plan: ​

- Select your workspace
- Go to the Members tab of your workspace
- Click on downgrade to message us your request. We will process it promptly.

`Members`



#### To downgrade a Project plan: ​

- Go to the Plans tab of the project
- Click on downgrade to message us your request. We will process it promptly.

`Plans`



## Compliance ​


### Can I satisfy GDPR Compliance while using WeWeb as my frontend? ​

Yes. WeWeb and its underlying infrastructure provider (AWS) provide the necessary tools and safeguards to support GDPR compliance.

However, it is crucial to recognize that a significant portion of the responsibility lies with the application itself. By adhering to the key GDPR requirements and fulfilling their respective obligations, application builders can create robust and privacy-conscious solutions using a tool like WeWeb.


### Can I satisfy HIPAA Compliance while using WeWeb as my frontend? ​

Yes. If you use a HIPAA-compliant backend and call it through our REST API plugin, in dynamic mode, your data will not transit through our product, making the whole project HIPAA compliant.


### Will my data transit through your infrastructure? ​

It depends on the Data Source and Collection Mode you choose.

When using data source plugins in dynamic mode, the data never goes through our servers, except if you explicitly choose to make a server-side request or in the case of the Airtable plugin. This is because of the way Airtable handles API keys and manages authorizations.

If you use data source plugins in static mode, then we will pre-render static pages with your data and deploy them on AWS cloudfront CDN. In that configuration your data will be hosted on our infrastructure.


## SEO ​


### How does WeWeb compare to other tools for SEO? ​

It depends on the tool! Historically, static website builders like Webflow and builders with server-side rendering (SSR) like WordPress had an SEO advantage over tools like WeWeb, Bubble, and others that generate dynamic content in JavaScript.

This happens because when search engine bots first visit a JavaScript application, they initially see only the base HTML file before any JavaScript runs. In dynamic applications like WeWeb, this base file is nearly empty since all content is added later by JavaScript running in the browser. By contrast, static/SSR sites deliver complete HTML with all content already included.

However, in recent years, search engines have significantly evolved to better handle JavaScript content, as more websites are built with modern JS frameworks like React or Vue. While the initial indexing might take a few extra days compared to static sites, search engine bots now effectively crawl and index JavaScript-based content during subsequent visits.

Here are Google’s thoughts on the topic:




## Is WeWeb suitable for large marketplaces? ​

Yes. While dynamic JavaScript applications have some SEO tradeoffs, many major marketplaces successfully use similar JavaScript-based architectures. The key is understanding that search indexing may take longer initially, but this is rarely a significant barrier for marketplace success which often depends more on:

- Product/service quality
- User experience
- Marketing strategy
- Network effects
- Direct traffic


### What can I do to help my WeWeb pages rank well in search engines? ​

There are many things you can do on your WeWeb apps that will improve its Lighthouse scores and, most importantly, the user’s experience (both of which influence SEO rankings).

- Follow SEO best practices when building:

- Add titles & metadata to all your pages
- Add alt text on all your images
- Use headings for titles
- Use elements with the correct HTML tags (e.g. buttons, select, etc.)

- Don’t load too much data on the page:

- Compress images
- Keep your pages short and simple
- Avoid superfluous nested containers
- Add backend filters on big sets of data
- Fetch collections only when you need them
- Use multi-page sections to avoid reloading data the user has already loaded
- Minimize unecessary custom scripts


## Agencies ​


### Does WeWeb work with Agencies? ​

Absolutely! We have a plan specifically tailored towards dev shops, freelancers and agencies. WeWeb partners are referenced here.


### Can I collaborate with others on a project in WeWeb? ​

Yes. Development can work better if a team is involved. Depending on which package you're subscribed to, you can grant access to other teammates to your instance and work simultaneously on a project together.


## Custom Development ​


### Can I create a custom plan with WeWeb? ​

Yes. This can be done by contacting us and inquiring about our custom enterprise setup.


### Can I hire a WeWeb expert to help develop my custom frontend? ​

Yes. WeWeb partners are referenced here.

