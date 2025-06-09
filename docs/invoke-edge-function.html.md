# Edge Functions ​


# Edge Functions ​

Edge Functions are mini-apps that run specific tasks when triggered by events in your app.

For example:

- Send a welcome email when a customer signs up.
- Process Stripe payments and update database access levels during subscription purchases.

They run on Supabase's servers, "on the edge," close to your users, ensuring speed, reliability, and security. Key benefits include:

- Secure sensitive data: Store API keys and credentials safely on the server, away from the frontend.
- Connect to external services: Centralize and simplify interactions with third-party tools like Stripe (payments), SendGrid (emails), OpenAI (AI), or Twilio (SMS) and more, while improving performance and reliability.
- Handle heavy tasks: Offload resource-intensive work like image processing, data transformation, PDF generation, or batch operations.
- Automate workflows: Trigger actions based on user activity (e.g., welcome emails), database changes (e.g., low stock alerts), or scheduled tasks (e.g., daily reports).


## Pre-requisites ​

To use Edge Functions in WeWeb, you'll need to create them on your local machine first, then upload them to Supabase. After that, you can invoke them in your WeWeb workflows using the Invoke Edge function action.

`Invoke Edge function`
TIP

You need to create Edge Functions locally because Supabase doesn't provide a web editor for function development. Local development also lets you test your functions and fix any issues before uploading them to Supabase's servers.

Before starting, ensure you have:

- The latest version of the Supabase CLI to create and upload functions from your computer.
- Docker Desktop for a secure, isolated environment.
- A text editor like Visual Studio Code for writing and editing functions.

TIP

Docker Desktop replicates Supabase's server environment locally. Edge Functions must run in the exact same conditions locally as they will on Supabase's servers. Without this isolation, your computer's specific setup could make functions work locally but fail when deployed.


## Process overview ​

Assuming you have all of the above, the process to invoke a Supabase Edge Function in your WeWeb app will go as follows:

- Create a project folder on your computer where you run Supabase locally.
- Create the function and edit it.
- Deploy the function to your Supabase project.
- Invoke the Supabase function in your WeWeb app.

Let's go through this step by step.


### Setup Your Workspace ​

- Create a folder (e.g., my_project) and open it in Visual Studio Code:
- Open the terminal (command window) in VS Code:

Create a folder (e.g., my_project) and open it in Visual Studio Code:

`my_project`


Open the terminal (command window) in VS Code:




## Set up Supabase locally ​

- Type supabase init in the terminal.
- This creates a new Supabase workspace in your folder.
- Say yes when VS Code asks to set up some helpful tools (for Deno, which runs code).

Type supabase init in the terminal.

`supabase init`
This creates a new Supabase workspace in your folder.

Say yes when VS Code asks to set up some helpful tools (for Deno, which runs code).



This creates a bunch of new files in the my_project folder. Some files are for VS Code, and others are for the local Supabase setup.

`my_project`
TIP

Deno is a tool that runs JavaScript code outside of browsers, enabling edge functions to work. It acts as an interpreter, helping functions communicate with servers.


## Create a function ​

Next, to create an Edge function in your project, run the command supabase functions new your-function-name.

`supabase functions new your-function-name`
This creates a new file where you'll write your function.



The index.ts file comes with an Edge function boilerplate that you can use as a starting point to write your own functions.

`index.ts`
TIP

Supabase Edge functions are written in TypeScript. This is what the .ts file extension stands for.

`.ts`
Learn more about how to write Supabase Edge functions.


## Test and deploy ​

- Open Docker Desktop. Run supabase start to test your function locally.WARNINGEnsure Docker Desktop is running. Otherwise, you'll encounter errors like:
- In the terminal, run supabase functions deploy your-function-name to deploy the function and then enter your Supabase project ID (found in project settings).
- Check Supabase dashboard to confirm upload, and that's it!

Open Docker Desktop. Run supabase start to test your function locally.

`supabase start`
WARNING

Ensure Docker Desktop is running. Otherwise, you'll encounter errors like:



In the terminal, run supabase functions deploy your-function-name to deploy the function and then enter your Supabase project ID (found in project settings).

`supabase functions deploy your-function-name`


Check Supabase dashboard to confirm upload, and that's it!




## Invoke the function ​

In WeWeb, you can call Supabase Edge functions by:

- Selecting the Invoke an Edge function action in a workflow.
- Entering the function name (e.g., your-name-function).
- Configuring the request:Method: Choose the appropriate HTTP method (e.g., POST, GET).Authorization headers: Include a valid token to authenticate the request.Body (for POST): Include a JSON object (e.g., { "name": "Joyce" }).
- Method: Choose the appropriate HTTP method (e.g., POST, GET).
- Authorization headers: Include a valid token to authenticate the request.
- Body (for POST): Include a JSON object (e.g., { "name": "Joyce" }).

Selecting the Invoke an Edge function action in a workflow.

`Invoke an Edge function`
Entering the function name (e.g., your-name-function).

`your-name-function`
Configuring the request:

- Method: Choose the appropriate HTTP method (e.g., POST, GET).
- Authorization headers: Include a valid token to authenticate the request.
- Body (for POST): Include a JSON object (e.g., { "name": "Joyce" }).

`Method`
`POST`
`GET`
`Authorization headers`
`Body`
`POST`
`{ "name": "Joyce" }`


When tested, the response will match the format defined in the Supabase Edge function, such as:



TIP

Authorization headers ensure only authorized clients (e.g., your WeWeb app) can access the Supabase Edge Function. They include tokens (e.g., JWT or API keys) to authenticate requests, which is essential for sensitive operations like database access or payments.

TIP

- Use POST for sending data or performing actions that modify data (e.g., creating a record, processing a payment).
- Use GET for retrieving data or performing read-only operations (e.g., fetching a list of items).
- Use PUT or PATCH for updating data, and DELETE for removing data.


## CORS ​

CORS (Cross-Origin Resource Sharing) is a safety feature that checks if your app is allowed to request data from different places. You might see CORS errors when connecting to Supabase edge functions.

To resolve CORS issues, simply add this object to your edge function:

```
// At the top of your edge function file (index.ts):
const corsHeaders = {
  'Access-Control-Allow-Origin': '*',
  'Access-Control-Allow-Headers': 'authorization, content-type'
}
//Inside your edge function's response handler (where you return data to the frontend), modify your response to include these CORS headers:

// This is where you modify the response to include CORS headers
return new Response(JSON.stringify(data), {
    headers: { ...corsHeaders, 'Content-Type': 'application/json' }
})
```

`// At the top of your edge function file (index.ts):
const corsHeaders = {
  'Access-Control-Allow-Origin': '*',
  'Access-Control-Allow-Headers': 'authorization, content-type'
}
//Inside your edge function's response handler (where you return data to the frontend), modify your response to include these CORS headers:

// This is where you modify the response to include CORS headers
return new Response(JSON.stringify(data), {
    headers: { ...corsHeaders, 'Content-Type': 'application/json' }
})`
TIP

CORS headers are set by the server (Edge Function), not the frontend. Use 'Access-Control-Allow-Origin': '*' to allow all domains or specify your app's domain (e.g., https://yourapp.com) for better security. These headers act as a basic security pass, allowing your app to communicate with the Edge Function.

`'Access-Control-Allow-Origin': '*'`
`https://yourapp.com`
TIP

To optimize Edge Functions, consider breaking down tasks into smaller functions.

Example: Instead of trying to process an entire video with one edge function, you could have

- Function 1 to extract video frames
- Function 2 to analyze visual content
- Function 3 to transcribe audio

