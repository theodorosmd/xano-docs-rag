# Frontend vs backend ​


# Frontend vs backend ​

When building modern web applications, it's important to understand the distinction between frontend and backend development. This guide will help you understand these concepts and how they relate to building applications in WeWeb.


## The two sides of web development ​

Web applications consist of two main parts:


### Frontend (Client-Side) ​

The frontend is everything users see and interact with directly:

- What it includes:user interface (UI)visual elementsinteractions and animationsforms and input fields
- user interface (UI)
- visual elements
- interactions and animations
- forms and input fields
- Technologies:HTML (structure)CSS (styling)JavaScript (interactivity)frontend frameworks (React, Vue, etc.)
- HTML (structure)
- CSS (styling)
- JavaScript (interactivity)
- frontend frameworks (React, Vue, etc.)
- Where it runs: in the user's browser on their device

What it includes:

- user interface (UI)
- visual elements
- interactions and animations
- forms and input fields

Technologies:

- HTML (structure)
- CSS (styling)
- JavaScript (interactivity)
- frontend frameworks (React, Vue, etc.)

Where it runs: in the user's browser on their device


### Backend (Server-Side) ​

The backend handles everything that happens behind the scenes:

- What it includes:database managementbusiness logicauthentication and authorizationAPI endpointsserver configuration
- database management
- business logic
- authentication and authorization
- API endpoints
- server configuration
- Technologies:server languages (Node.js, Python, PHP, etc.)databases (PostgreSQL, MySQL, MongoDB, etc.)APIs and middlewareserver infrastructure
- server languages (Node.js, Python, PHP, etc.)
- databases (PostgreSQL, MySQL, MongoDB, etc.)
- APIs and middleware
- server infrastructure
- Where it runs: on remote servers, not visible to users

What it includes:

- database management
- business logic
- authentication and authorization
- API endpoints
- server configuration

Technologies:

- server languages (Node.js, Python, PHP, etc.)
- databases (PostgreSQL, MySQL, MongoDB, etc.)
- APIs and middleware
- server infrastructure

Where it runs: on remote servers, not visible to users


## How frontend and backend work together ​

Frontend and backend communicate with each other to create a complete application:

```
┌─────────────────┐                ┌─────────────────┐
│                 │     HTTP       │                 │
│     FRONTEND    │◄──Requests──►  │     BACKEND     │
│  (User's Browser)│                │  (Remote Server)│
│                 │                │                 │
└─────────────────┘                └─────────────────┘
       │                                   │
       │                                   │
       ▼                                   ▼
  User Interface                       Database
  Interactions                         Business Logic
  Visual Presentation                  Authentication
  Client-side Logic                    Data Processing
```

`┌─────────────────┐                ┌─────────────────┐
│                 │     HTTP       │                 │
│     FRONTEND    │◄──Requests──►  │     BACKEND     │
│  (User's Browser)│                │  (Remote Server)│
│                 │                │                 │
└─────────────────┘                └─────────────────┘
       │                                   │
       │                                   │
       ▼                                   ▼
  User Interface                       Database
  Interactions                         Business Logic
  Visual Presentation                  Authentication
  Client-side Logic                    Data Processing`

### Example of frontend-backend interaction ​

When you use a social media website:

- Frontend:displays the feed of postsshows buttons for liking and commentingprovides forms for creating new posts
- displays the feed of posts
- shows buttons for liking and commenting
- provides forms for creating new posts
- Backend:stores all posts, user data, and relationships in a databaseprocesses authentication when users log inhandles requests to create, like, or comment on postssends the appropriate data to the frontend
- stores all posts, user data, and relationships in a database
- processes authentication when users log in
- handles requests to create, like, or comment on posts
- sends the appropriate data to the frontend
- Communication Flow:when you click "Like" on a post (frontend action)the frontend sends a request to the backend APIthe backend updates the database to record your likethe backend sends confirmation back to the frontendthe frontend updates the UI to show the post is liked
- when you click "Like" on a post (frontend action)
- the frontend sends a request to the backend API
- the backend updates the database to record your like
- the backend sends confirmation back to the frontend
- the frontend updates the UI to show the post is liked

Frontend:

- displays the feed of posts
- shows buttons for liking and commenting
- provides forms for creating new posts

Backend:

- stores all posts, user data, and relationships in a database
- processes authentication when users log in
- handles requests to create, like, or comment on posts
- sends the appropriate data to the frontend

Communication Flow:

- when you click "Like" on a post (frontend action)
- the frontend sends a request to the backend API
- the backend updates the database to record your like
- the backend sends confirmation back to the frontend
- the frontend updates the UI to show the post is liked


## WeWeb as a frontend builder ​

WeWeb is primarily a frontend builder, which means it focuses on creating the user interface and client-side functionality of web applications.


### What WeWeb handles (Frontend) ​

- visual design: building interfaces with a drag-and-drop editor
- UI components: creating and styling elements that users interact with
- page navigation: setting up routes and transitions between pages
- client-side logic: creating workflows for user interactions
- API consumption: connecting to backend services to display and manipulate data


### What WeWeb doesn't handle (Backend) ​

- database creation: WeWeb doesn't create or host databases
- server-side processing: complex calculations and operations that should happen on a server
- authentication systems: while WeWeb can integrate with auth services, it doesn't create them
- scheduled tasks: background jobs or operations that run on a schedule
- complex business logic: advanced operations that should happen on secure servers


### Connecting WeWeb to backend services ​

WeWeb is designed to connect seamlessly with various backend services through plugins and API integrations:

- data source plugins: connect to backend data sources like Supabase, Xano, or custom REST APIs
- authentication plugins: integrate with auth providers like Xano Auth, Auth0, or Supabase Auth
- custom endpoints: connect to any backend service that provides a REST API


## Frontend vs Backend: key differences ​

Understanding these differences helps you make better architectural decisions:


## Frontend limitations to be aware of ​

When building with WeWeb or any frontend tool, it's important to understand these limitations:


### 1. Security constraints ​

Frontend code runs in the user's browser, which means:

- never store sensitive information in frontend variables or collections
- don't trust client-side validation alone for important data
- assume users can see all frontend data and potentially modify it


### 2. Processing limitations ​

Frontend applications are limited by the user's device:

- heavy calculations should be handled by the backend
- large data processing is better done on servers
- browser memory is limited compared to servers


### 3. Persistence challenges ​

Frontend applications reset when browsers close:

- data is temporary unless explicitly saved
- sessions end when browsers are closed
- background operations can't continue when the browser is closed


## Best practices for frontend-backend architecture ​

When building with WeWeb, follow these principles:


### 1. Clear separation of concerns ​

- use WeWeb for what it does best: creating beautiful, interactive UIs
- delegate complex business logic and data processing to backend services
- keep authentication and authorization logic on the backend


### 2. Secure communication ​

- never expose sensitive API keys in your frontend logic
- implement proper authentication for API requests

SECURE API KEYS

Any API keys you input into the configuration of data source plugins are secure and will not be exposed in the network requests.


### 3. Optimized data transfer ​

- only request the data you need from your backend
- implement pagination for large datasets
- use caching where appropriate


### 4. Thoughtful integration ​

- choose the right backend service for your needs (Supabase, Xano, Firebase, etc.)
- document the APIs and data structures used in your application
- consider future scalability when designing your system


## Real-world architecture example ​

Here's an example of how you might structure a WeWeb application with backend services:

```
┌───────────────────────┐         ┌───────────────────────┐
│                       │         │                       │
│      WeWeb App        │ ◄─────► │   Backend Services    │
│   (Frontend Layer)    │         │                       │
│                       │         │                       │
└───────────────────────┘         └───────────────────────┘
         │                                   │
         ▼                                   ▼
┌───────────────────────┐         ┌───────────────────────┐
│ • User Interface      │         │ • Supabase/Xano/      │
│ • Form Validation     │         │   Custom API          │
│ • Page Navigation     │         │ • Authentication      │
│ • Interactive Elements│         │ • Database Management │
│ • Data Display        │         │ • File Storage        │
│ • Simple Calculations │         │ • Email Services      │
│ • User Experience     │         │ • Payment Processing  │
└───────────────────────┘         └───────────────────────┘
```

`┌───────────────────────┐         ┌───────────────────────┐
│                       │         │                       │
│      WeWeb App        │ ◄─────► │   Backend Services    │
│   (Frontend Layer)    │         │                       │
│                       │         │                       │
└───────────────────────┘         └───────────────────────┘
         │                                   │
         ▼                                   ▼
┌───────────────────────┐         ┌───────────────────────┐
│ • User Interface      │         │ • Supabase/Xano/      │
│ • Form Validation     │         │   Custom API          │
│ • Page Navigation     │         │ • Authentication      │
│ • Interactive Elements│         │ • Database Management │
│ • Data Display        │         │ • File Storage        │
│ • Simple Calculations │         │ • Email Services      │
│ • User Experience     │         │ • Payment Processing  │
└───────────────────────┘         └───────────────────────┘`

## Conclusion ​

Understanding the distinction between frontend and backend development is crucial when building web applications with WeWeb. By recognizing what WeWeb excels at (frontend development) and where to integrate with backend services, you can create powerful, scalable applications that provide great user experiences while maintaining proper security and functionality.

WeWeb empowers you to build sophisticated frontend interfaces without writing code, while seamlessly connecting to various backend services to handle data, business logic, and security.

CONTINUE LEARNING

Now that you understand the frontend-backend distinction, learn more about how these systems communicate:

Understanding APIs →

