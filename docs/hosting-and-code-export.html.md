# Export code & self-host ​


# Export code & self-host ​

In this article, you'll learn:

- How to export a project
- How to self-host a project

TIP

Code export and self-hosting is available on the Essential seat plan and higher seat plans.


## Export a project ​

Once the export project feature has been added to your workspace, go to any published project's Settings > Deployments tab.

`Settings`
`Deployments`
Click on the version of the app for which you'd like to export the code:



What if the download button is disabled?

Publish your project at least once to make it clickable.

Once downloaded, you'll find a zip file containing all your project's files (HTML, CSS and JS) ready to host anywhere you want.


## Code export example ​

You can download an example project here with both raw and built files.




## Self-host a project ​

You can self-host WeWeb projects anywhere you like!

Simply download the static files of your app as described above (i.e. the HTML, CSS and JS files of your WeWeb frontend), fire up a server and host the static files of your frontend there.

As an example, we've documented how you might self-host a WeWeb project on Cloudflare.


## Frequently Asked Questions ​

No. The exported code will run on your infrastructure, so none of the hosting plan limits apply.

You can export your code as many times as you want, for as long as you have an active seat plan subscription.

You can host the app on cloud hosting platforms like Amazon Web Services, Google Cloud Platform, Microsoft Azure, Cloudflare or Digital Ocean, as well as on managed hosting services platforms like Netlify.

Or you can self-host on your on-premise infrastructure—basically anything that can run a web server; an internet connection is not mandatory.

Yes. WeWeb is a frontend-only tool. Your backend remains separate and is not affected by exporting or self-hosting your WeWeb project.

When you self-host the exported app, the frontend will continue to make API calls to your backend, wherever it's hosted, just as it did before exporting.

There are two self-hosting scenarios to consider:

A- Exporting your code and hosting it elsewhere (Recommended):

- Some plugins require communication with WeWeb microservices (Airtable, Google, Notion, OpenAI, SmartSuite, SQL, Stripe, SOAP)
- Direct connections to backends (e.g., Supabase, Xano, standard REST/GraphQL APIs) work independently of WeWeb.

B- Using the WeWeb server as a service (Deprecated):

- The plugins listed above may not function properly in this scenario.
- WeWeb no longer supports this option.
- We don't recommend using this method for new projects.MicroservicesWhat causes the plugins to not work in these scenarios is due to how WeWeb uses microservices.

The plugins listed above may not function properly in this scenario.

WeWeb no longer supports this option.

We don't recommend using this method for new projects.

Microservices

What causes the plugins to not work in these scenarios is due to how WeWeb uses microservices.

WeWeb is a front-end app builder that runs in users' browsers. Some backend services (e.g., Xano, Supabase, Rest API) are designed to be accessed directly from browsers, while others (Airtable, Open AI, etc.) are meant for server-to-server communication and require more security.

To make it easier for users to integrate with services such as OpenAI or Airtable (which aren't typically accessed directly from browsers), WeWeb created microservices.

A microservice is a small, specialized server component that handles specific tasks like securely connecting to external services.

These act as intermediaries, allowing WeWeb users to securely connect to these services without exposing sensitive information like API keys in the frontend.



We have two separate servers:

- WeWeb-Plugins: This microservice acts as a proxy for plugins that need to keep API keys secure (like Airtable and OpenAI).
- WeWeb-Preview (or WeWeb-Server): This server runs your app and handles plugin requests in production.WARNINGIn Scenario B (using the deprecated WeWeb-Server), if you host the WeWeb-Server yourself, you won't have access to WeWeb-Plugins. As a result, plugins like Airtable and OpenAI won't work because your server can't securely send requests to these services.

WeWeb-Plugins: This microservice acts as a proxy for plugins that need to keep API keys secure (like Airtable and OpenAI).

WeWeb-Preview (or WeWeb-Server): This server runs your app and handles plugin requests in production.

WARNING

In Scenario B (using the deprecated WeWeb-Server), if you host the WeWeb-Server yourself, you won't have access to WeWeb-Plugins. As a result, plugins like Airtable and OpenAI won't work because your server can't securely send requests to these services.

Plugins using WeWeb microservices, like WeWeb Auth, store and process data in the US (using AWS Cognito). This has an effect on EU data residency compliance as data leaves the EU.

When you export code from WeWeb, you have two options:

Project files:

- This is a Vue.js application ready for deployment.
- The app has been compiled and optimized for production use.
- It includes all necessary components and dependencies.
- Can be immediately deployed to a web server or hosting platform.

Raw project files:

- These are static HTML/CSS/JS files.
- They represent the basic structure and content of your project.
- Useful if you want to run your build process or perform code analysis.
- Can be modified or integrated into custom development workflows.
- They do not contain Vue.js components or framework-specific code.

Raw files that need a build step and built files that are ready to host immediately.

While it's technically possible to edit the exported code from WeWeb, it's not easy or recommended.

The code is structured by a machine for a machine and is not organized like a human developer would organize it.

Editing these files safely requires in-depth knowledge of WeWeb's internal logic. This approach isn't feasible if you're planning to build a project in WeWeb and then maintain it independently outside the platform.

Yes, WeWeb applications can be hosted in networks with no internet access. You can export the code and host it in your network alongside your own backend.

No. Files uploaded to WeWeb's CDN before self-hosting will not be preserved when you self-host.

For self-hosting scenarios, it's best to set up file uploads to your own storage solution from the beginning to ensure continuity when you transition to self-hosting.

Files that are part of your app's structure (like images embedded in the design) will be included in the export.

No, you need to publish your project at least once to enable the export feature.

No, the export includes the entire project.

No, this feature is currently not available.

With WeWeb, you can self-host your project in any standard web server.

The setup of a custom domain is handled through your hosting provider, not WeWeb.

Yes, all of that is possible when you self-host.

Yes, WeWeb's UI components will be included in the exported files.

WeWeb itself doesn't provide version control for exported projects. However, once you have exported your project, you can implement version control yourself using systems like Git.

No. You'll need to use third-party solutions for that.

Yes. You can deploy to multiple domains if you self-host.

