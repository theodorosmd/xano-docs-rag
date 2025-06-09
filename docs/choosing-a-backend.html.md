# Choosing a backend for Your WeWeb App ​


# Choosing a backend for Your WeWeb App ​

WeWeb is primarily a frontend builder, so it needs to connect to external backend services to store and manage data. Before diving into working with data, it's important to understand the backend options available to you.

NEW TO BACKENDS?

If you're new to web development and don't understand what a backend is or how APIs and databases work together, start with our APIs and Databases primer. It covers the fundamentals of how a frontend connects to data storage through APIs.


## Understanding backend services ​

A backend service provides several essential functions for your application:

- data storage - Databases to store your application data
- business logic - Processing and manipulating data
- authentication - Managing user accounts and access
- API endpoints - Interfaces for your frontend to request data

In WeWeb, you connect to these services through data source plugins, which provide a seamless interface between your application and the backend service.


## Common backend options ​

WeWeb supports several backend services through its plugin system. Let's explore the most popular options:


### REST API ​

Best for: Connecting to any existing API and quick prototyping

The REST API plugin is the most flexible option, allowing you to connect to virtually any API:

- pros: Works with any REST API, great for custom backends, simple to use
- cons: Less integrated experience, may require more manual configuration
- use case: When you already have an existing API or need to connect to third-party services that WeWeb doesn't have a plugin for

Learn more about the REST API plugin →


### Supabase ​

Best for: Applications needing a relational database with SQL capabilities

Supabase provides a complete backend solution with PostgreSQL database and authentication:

- pros: Powerful SQL database capabilities, built-in authentication, realtime capabilities
- cons: Requires SQL knowledge, more developer-oriented
- use case: Projects where you need relational data and have team members comfortable with SQL

Learn more about the Supabase plugin →


### Xano ​

Best for: Powerful no-code backend development with scalable infrastructure

Xano is a sophisticated no-code backend builder with enterprise-grade capabilities:

- pros: Visual API builder, powerful business logic capabilities, highly scalable, no SQL knowledge required
- cons: Subscription-based pricing may be higher for some use cases
- use case: Complex applications where you need powerful backend logic but prefer a visual interface over writing code

Learn more about the Xano plugin →


### Airtable ​

Best for: Simple applications or quick prototypes

Airtable is a spreadsheet-database hybrid that's easy to use:

- pros: Easy to set up, familiar spreadsheet interface, visual data management
- cons: Limited scaling capabilities, API rate limits
- use case: Simple applications, prototypes, or projects where visual data management is important

Learn more about the Airtable plugin →


## Choosing the right backend ​

When selecting a backend for your WeWeb project, consider these factors:


### 1. Project complexity ​

- simple projects (personal websites, landing pages, basic forms) - Airtable or a simple REST API
- medium complexity (business apps, member portals) - Xano or Supabase
- complex applications (multi-user systems, marketplaces) - Both Xano and Supabase are capable; the choice depends more on your team's skills and preferences


### 2. Technical experience ​

- no coding experience - Airtable for simple needs, Xano for more complex requirements
- comfortable with SQL - Supabase gives you direct database access
- prefer visual development - Xano offers powerful capabilities without requiring SQL knowledge
- development team available - Any option, depending on your team's preferences


### 3. Data structure needs ​

- simple data storage - Airtable
- relational data with SQL control - Supabase
- complex data operations without SQL - Xano
- custom data requirements - Either Xano or Supabase, depending on your team's skills


### 4. Authentication requirements ​

If your app needs user accounts and authentication:

- simple auth - All options support basic authentication
- advanced auth with visual setup - Xano Auth
- advanced auth with more direct control - Supabase Auth or Auth0


### 5. Scalability considerations ​

- small user base (dozens/hundreds) - Any option
- medium to large scale (thousands to millions) - Both Xano and Supabase can handle significant scale, with different pricing models


### 6. Budget and pricing model ​

- hobby project or startup - Supabase offers a generous free tier to start
- business with predictable needs - Xano's pricing is subscription-based
- variable usage patterns - Supabase's usage-based pricing may be advantageous


## Setting up your first backend ​

Let's take a quick look at how to get started with two popular options:


### Quick start with Supabase ​

- create a Supabase account at supabase.com
- set up a new project
- create tables for your data
- in WeWeb, add the Supabase plugin
- connect to your Supabase project
- create collections to fetch your data


### Quick start with Xano ​

- create a Xano account at xano.com
- create a new workspace
- set up your database tables
- create API endpoints
- in WeWeb, add the Xano plugin
- connect to your Xano workspace
- create collections to fetch your data


## Backend security considerations ​

Regardless of which backend you choose, always consider these security aspects:

- authentication - Ensure proper user authentication before allowing data access
- authorization - Implement proper access controls (Row-Level Security in Supabase or Access Control in Xano)
- data validation - Validate data on both frontend and backend


## Making the decision ​

Still not sure which backend to choose? Here's a simple decision flow:

- if you're building a simple prototype or are new to web development → Airtable
- if you prefer a no-code solution with visual development → Xano
- if you're comfortable with SQL and want direct database control → Supabase
- if you have existing APIs → REST API

Remember that both Xano and Supabase are capable of handling complex, scalable applications. The choice often comes down to your team's technical expertise, workflow preferences, and budget considerations.

UNLIMITED POSSIBILITIES

The backend options discussed here are recommendations based on WeWeb's existing data source plugins. It's important to note that you can use virtually any backend system with WeWeb as long as it provides an API.

The REST API plugin serves as a universal connector, allowing you to integrate with custom or proprietary backends, traditional server architectures, or any other service that exposes API endpoints. This flexibility means you're never limited to just the backends that have dedicated plugins.

CONTINUE LEARNING

Now that you understand the different backend options, learn how to work with data from your chosen backend:

Working with data →

