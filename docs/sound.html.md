# Sound ​


# Sound ​


## Add plugin ​

To build audio features in your WeWeb app, add the Sound plugin from the Plugins > Extensions menu:

`Plugins`
`Extensions`



## Sound element template ​

When you add the Sound plugin, you will have the option to also add a ready-made sound template element:



While the sound template element is fully customizable, it comes with pre-built workflows and bindings that will get you up and running in no time.


## Access workflow actions ​

Once added to a project, the Sound plugin gives you access to a number of no-code workflow actions to load, play, pause, stop audio files and more.

Simply create a workflow, and search for "sound" to view all the actions available:




## Load sound ​

WARNING

This step is a pre-requisite for every other step. Before you can let users interact with a sound or unload a sound, you will first need to load it.

To load a sound in a WeWeb app, you will need to:

- create a workflow with a "Load sound" action
- give the sound a unique ID
- provide a URL where the audio file can be found



TIP

Make sure you provide the URL to a file with a standard audio extension such as .mp3 or .wav. Otherwise, the sound may not be recognized as such.


## Sound variable ​

Once you load a sound with a unique id, you will be able to access that sound's variable in the data explorer:



That variable includes helpful information including:

- isPlaying – whether the sound is currently being played or not,
- totalTime– how long the sound lasts (in seconds),
- currentTime and currentTimePercent: – the position of where the sound is at the moment (in seconds or percentage)

`isPlaying`
`totalTime`
`currentTime`
`currentTimePercent`
You can react to this information to build your own custom audio player.

In the example below, you can see we bound a progress bar element to the currentTimePercent value of our audio file:

`currentTimePercent`



## Sound options ​

When you load a sound, it will come with default options:



To customize these values, you can either bind the Options to an array of objects or click on Add item to add a key value pair.

`Options`
`Add item`
In the example below, we set the loop value to true:

`loop`
`true`


As a result, the sound was loaded with the proper loop value and, if the user plays the sound, the audio file will be played on repeat.

TIP

If you choose to bind the Options to an array of objects, use the following format:

`Options`
[{"key":"volume","value":0.5}, {"key":"loop","value":true}]

`[{"key":"volume","value":0.5}, {"key":"loop","value":true}]`
The Current value should be an array of objects with a value for key and a value for value as shown in the example below:

`Current value`
`key`
`value`



## Sound metadata ​

When you load a sound, you can add metadata. This can be anything you want.

In the example below, we added three fields: a cover album image, a song title, and an artist name:



As a result, we can bind that information to the audio player on our WeWeb page:



TIP

If you choose to bind the Metadata, the Current value should be an array of objects with a value for key and a value for value as shown in the example below:

`Metadata`
`Current value`
`key`
`value`


Note, the example above uses the following sample code in Javascript mode but you can use the same snippet in Formula mode without the return at the beginning:

`Javascript`
`Formula`
`return`
```
return [
    {"key":"title","value":"Unforgettable"}, {"key":"artist","value":"Nat King Cole"},
    {"key":"artwork","value":[
      {
        src: "https://dummyimage.com/192x192",
        sizes: "192x192",
        type: "image/png",
      },
      {
        src: "https://dummyimage.com/256x256",
        sizes: "256x256",
        type: "image/png",
      }
    ]}
]
```

`return [
    {"key":"title","value":"Unforgettable"}, {"key":"artist","value":"Nat King Cole"},
    {"key":"artwork","value":[
      {
        src: "https://dummyimage.com/192x192",
        sizes: "192x192",
        type: "image/png",
      },
      {
        src: "https://dummyimage.com/256x256",
        sizes: "256x256",
        type: "image/png",
      }
    ]}
]`

## Unload sound ​

To maintain a responsive and efficient user experience, trigger the Unload sound action when a sound is no longer relevant.

`Unload sound`
For example, when transitioning between pages or when switching to a different section of your application.

TIP

Unloading sounds in your WeWeb project is crucial for optimizing performance and memory usage.

By freeing up resources when sounds are no longer needed, you ensure smoother operation and prevent potential slowdowns or crashes, especially in complex applications or for users with limited device resources.

