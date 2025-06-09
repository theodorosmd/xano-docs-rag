# Component instance ​


# Component instance ​

The thisInstance object streamlines custom JavaScript integration in WeWeb components. It provides direct access to the component's DOM element, essential for third-party libraries and efficient DOM manipulation. It eliminates the need for costly full DOM traversal JavaScript methods such as document.querySelector, instead targeting only the specific component instance. This approach significantly improves performance when working with custom scripts or HTML code in WeWeb components.

`thisInstance`
`document.querySelector`
TIP

WeWeb is a visual development platform - you don't need JavaScript knowledge to create powerful applications. However, WeWeb still gives you the flexibility to add custom code if you want to extend your application's capabilities.


## Why it matters: ​

Traversing the entire DOM is expensive. Many third-party libraries require DOM elements to initialize. Using thisInstance in workflows with the onMounted trigger provides these libraries with the correct elements at the right time, ensuring proper setup

`thisInstance`
`onMounted`
Let’s say we want to add some custom HTML code inside our Selfie component:



We can add the code below. This HTML code sets up a simple camera capture and image download interface:



Now we can access our component workflow 'Init camera' that uses the onMounted trigger. We will use this workflow to initialize the camera:

`onMounted`


TIP

onMounted is a lifecycle event that occurs when a component has been inserted into the DOM (Document Object Model). It signifies that the component has been rendered and is now "mounted" in the page structure. This is an ideal time to perform certain actions:

`onMounted`
- Initializing third-party libraries
- Setting up event listeners
- Making initial API calls
- Manipulating the DOM directly (when necessary)
- Starting animations or timers thisInstance is best used onMounted as it ensures that the component's DOM elements are fully rendered and available. thisInstance provides access to these elements, so using it in onMounted guarantees that the elements you're targeting actually exist.

`thisInstance`
`onMounted`
`thisInstance`
`onMounted`
In our component’s workflow, we can add a Custom JavaScript action:

`Custom JavaScript`


When targeting DOM elements, using document.querySelector() forces a search through the entire document tree. The issue lies with the document object, which represents the whole DOM. This global scope can be inefficient, especially in large or complex web applications.



Binding scripts to the component's scope improves efficiency. Rather than using the global document object, which searches the entire DOM, we use a thisInstance object. This object limits the script's scope to the component's own HTML, ensuring faster and more targeted element selection within the component instance.



The code will work even if you have multiple instances within the same page.


## Conclusion ​

When working with custom JavaScript in component workflows, use thisInstance instead of document to target DOM elements. Here's why:

`thisInstance`
- document.querySelector() searches the entire DOM, which is inefficient.
- thisInstance targets only the current component's HTML.
- This approach is faster and maintains component isolation.
- It works seamlessly with multiple component instances on a page

`document.querySelector()`
`thisInstance`
