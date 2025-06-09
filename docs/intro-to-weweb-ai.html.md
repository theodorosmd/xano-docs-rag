# WeWeb AI ​


# WeWeb AI ​

WeWeb AI is an intelligent assistant that serves as the focal point of your building process. Through natural conversation, you can create every aspect of your web application - from UI elements to complex workflows, formulas, and even custom-coded components.

WARNING

WeWeb AI is currently in beta. While it significantly accelerates development, you may encounter occasional limitations or behaviors that need refinement. Our team is actively working to improve the AI's capabilities, enhance its understanding of complex requirements, and expand its feature set. We recommend testing AI-generated elements thoroughly and welcome your feedback to help us enhance the platform.


## How to start prompting ​

Effective prompting is key to getting the most out of WeWeb AI. To access WeWeb AI, simply click on the AI button in the top right corner of the editor. This switches the right panel from Edit mode to AI mode, where you can start a conversation.


### Crafting effective prompts ​

When working with WeWeb AI, consider these best practices:

- Be specific and detailed - The more specific your request, the better the result. Include information about layout, styling, functionality, and data.
- Provide context - If you have images or data points you want the AI to reference, pass them in as context.
- Mention design preferences - If you have specific styling preferences, mention them. Otherwise, WeWeb AI will make design choices that align with common patterns.

Be specific and detailed - The more specific your request, the better the result. Include information about layout, styling, functionality, and data.

Provide context - If you have images or data points you want the AI to reference, pass them in as context.

Mention design preferences - If you have specific styling preferences, mention them. Otherwise, WeWeb AI will make design choices that align with common patterns.


### Understanding generated workflows ​

When WeWeb AI creates workflows for your request, it initially generates them with a single Custom JavaScript action that contains all the logic. This approach allows the AI to implement complex functionality quickly.

`Custom JavaScript`
After the workflow is generated, you can:

- Use it as-is with the JavaScript implementation
- Click the Convert to no-code with WeWeb AI button to have the AI transform the JavaScript into individual no-code actions

`Convert to no-code with WeWeb AI`

## What can WeWeb AI do? ​


### Page building & UI elements ​

Simply prompt WeWeb AI for what you want on the page, and it will generate a complete UI with interactive elements. The AI automatically:

- Creates responsive layouts with proper styling
- Adds hover states and interactive elements
- Sets up variables and binds them where necessary
- Creates workflows for the functionality you describe

You can iterate on generations by:

- Clicking on specific elements to provide context for changes
- Making general requests without selecting elements for broader changes

For example, you can ask "Add a status filter select to this task list" and the AI will not only create the UI element but also set up the filtering functionality.


### Formulas and workflows with context ​

When you have a formula window or workflow open, WeWeb AI automatically understands:

- The current formula or workflow you're working with
- All data available in your project
- The context where the formula or workflow will be used

With formulas, this allows you to create complex, contextualized calculations through natural language requests.

With workflows, the AI has full context of:

- The workflow structure
- Available actions and conditions
- Data sources and collections in your project

This enables you to build sophisticated logic through simple conversation.

Learn more about passing formula and workflow context to AI →


### Custom component generation ​

When you need functionality that doesn't exist in WeWeb's native elements, WeWeb AI can generate custom-coded components:

- Request a specific component (e.g., "Create a dual range slider component")
- The AI generates the component with appropriate properties and settings
- Drag the component onto your page like any other element
- Continue to iterate on the component with the AI

Custom components include both styling options and settings, giving you powerful functionality with the simplicity of no-code.

Learn more about generating custom-coded components →


### Backend integration ​

With WeWeb 3.0's new Backend panel, WeWeb AI can integrate directly with your backend:

- Connect to your backend (currently Supabase, with more providers coming)
- AI can generate appropriate database tables and structures
- Create collections linked to your backend data
- Populate mock data for testing
- Adjust your UI to work with backend data instead of variables

The AI automatically adapts filtering, search, and other functionality to work with your collections.

