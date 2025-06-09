# How to self-host on Cloudflare ​


# How to self-host on Cloudflare ​

This guide will walk you through the steps required to self-host your WeWeb application on Cloudflare.


## Prerequisites ​

- A Cloudflare account (free)
- An Essential seat plan or higher WeWeb seat plan subscription


### Let's start with Cloudflare first: ​

- On Cloudflare's dashboard, click on the Workers & Pages section.



- Make sure you are on the Overview tab. If you already have another Worker in this section, click on the Create button and then go to the Pages tab.
- Go to the second section on the page and click on "Upload assets".



- Give your project a name and then click on Create project.




### WeWeb ​

- Next, go to your project dashboard in WeWeb. Go to the Deployments tab.



TIP

Your project must have been published at least once before you can export the project files.

- Here, you will see Staging and Production environments:



TIP

In this guide, we will export code from the production environment, but you can also export the staging version of your app if you are on the Pro seat plan or higher. If you recently made changes on staging and you want to export the app with those changes, promote the staging version to production first.

- Click on the three dots on the right (⫶) and select Download project files. This will download a zip directory of the project files to your device. This zip archive includes the compiled project (a Vue.js application) with all the files necessary for hosting it on Cloudflare.




### Cloudflare ​

- Upload the zip archive you just downloaded from WeWeb into the Upload your project assets section. Make sure you select Upload zip before you upload.



- Click the "Deploy site" button after all files are successfully uploaded.



Upon deploying, Cloudflare will provide you with some additional information and options:

- Cloudflare site URL
- Option to add a custom domain

You can ignore the other options for now.



10, If you click on "Continue to project", you will be redirected to the Deployments tab of your applications's Worker:



Your application is now live and fully self-hosted on Cloudflare!




## Making changes to the self-hosted application ​

- Make changes in your app in WeWeb.
- Publish the application again.
- Export the code following the steps described earlier.
- Download new zip file for latest version.
- In the Overview of Workers & Pages, go to the Deployments tab and click on Create a new deployment.



- Select your deployment environment
- Upload the new zip archive.
- Click on Save and deploy.



After a successful deployment, your changes will be reflected in the self-hosted application.



TIP

Always test your updated application thoroughly after deployment to ensure all changes are correctly reflected and functioning as expected.

By following these steps, you can easily export your WeWeb project and self-host it on Cloudflare, as well as keep it updated with any changes you make in WeWeb.

