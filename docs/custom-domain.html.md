# Add a custom domain ​


# Add a custom domain ​


## What is a domain? ​

A domain is your website's address on the internet - it's what people type into their browser to visit your site.

When you publish a WeWeb app, we provide a default subdomain on the weweb-preview.io domain, served over SSL. For instance, yourapp.weweb-preview.io.

`weweb-preview.io`
`yourapp.weweb-preview.io`
If you want to customize this and use your own domain name, you can do this in the Domains section of the project Settings tab.

`Domains`
`Settings`
TIP

Custom domains are only available if you have a hosting plan, which requires a seat plan.

First, you'll need to go to your Project Settings, click on Domains, then on Connect an existing domain name:

`Settings`
`Domains`
`Connect an existing domain name`

## 1. Choose a subdomain ​

Here, you'll have to type the subdomain and domain name you want to use:



For example, type in www.mydomain.com if you want to host your website on the www subdomain or app.mydomain.com if you want to publish your app on the app subdomain.

`www.mydomain.com`
`www`
`app.mydomain.com`
`app`
WARNING

WeWeb doesn't support naked domain like mydomain.com for the moment. Be sure to use a subdomain. The most common one is www but you could use app or dashboard or any other subdomain that you see fit.

`mydomain.com`
`www`
`app`
`dashboard`
For example, WeWeb serves apps on the support, academy and marketplace subdomains of weweb.io.

`support`
`academy`
`marketplace`
`weweb.io`
TIP

When you purchase a domain name with a registar, you don't need to purchase an SSL certificate. WeWeb will provide one for you and update it automatically on a yearly basis as long as you've added the CNAME record in the DNS (see below).


## 2. Update your DNS records ​

Once you've told WeWeb on what subdomain you want to host your app, you will be provided with information to create two DNS records, both CNAME records:

- the first will tell the DNS where to find the SSL certificate of your app (so it uses https)
- the second will tell the DNS where to find your app

`https`


TIP

Thinking of the DNS (which stands for Domain Name System) as "the phonebook of the Internet" can be helpful because it reminds us the DNS needs to know at what address (IP or URL) it can find information related to our websites.

To update the DNS with these new records, you'll need to find the appropriate section in your domain registar (e.g. Cloudflare, GoDaddy, etc.)

Each registar will have its own way of referring to what WeWeb calls Name and Value. For example, Cloudflare refers to Name and Content while Namecheap refers to Host and Value.

`Name`
`Value`
`Name`
`Content`
`Host`
`Value`
In the end, no matter what your registar calls these fields, the two CNAME records in your DNS should look something like this:



In the example above, you can see we chose to redirect our app users to the www subdomain. If we had chosen to publish our app on app.joycekettering.rocks, you would see app here instead of www.

`www`
`app.joycekettering.rocks`
`app`
`www`
TIP

Some registars will refer to the TTL value in seconds like WeWeb (1800) and others in minutes (30) while others don't give you the option to customize it and simply set it to Auto by default.

`TTL`
`Auto`
All three approaches are fine and will not affect the end-result.


## 3. Wait for DNS propagation ​

Once you've added the CNAME records to the DNS, you'll have to wait.

WARNING

Depending on your registar, it can take up to 48 hours for the new CNAME records to take affect. You can check the progress on the DNS checker website

Once DNS records are fully propagated, you should be able to access your app when you type its address with the subdomain (e.g. www.yourdomain.com) and the Value found in DNS fields in WeWeb should appear in green with a success hint saying Your DNS is setup correctly:

`www.yourdomain.com`
`Value found in DNS`
`Your DNS is setup correctly`



## 4. Redirect root domain (optional) ​

If you chose to publish your WeWeb app on the www subdomain, you will most likely want to setup a redirection from your root domain to that subdomain so that users who type in yourdomain.com are redirected to the www.yourdomain.com.

`www`
`yourdomain.com`
`www.yourdomain.com`
To do this, you will need to create an alias record on the DNS. You can do this:

- in your domain registar or, if your domain registar doesn't support root domain redirection,
- through a third-party Delivery Network System like Cloudflare.

For option 1, we recommend you refer to your domain registar's documentation to check if they have the ability to provide naked domain redirects for https. Many don't because their redirect server can't provide SSL service.

`https`
For such cases, we recommend using CloudFlare to handle your DNS settings and setup a permanent 301 redirection from your root domain to the subdomain of your app (e.g. www or app).

`www`
`app`
At the time of writing, Cloudflare allows you to do this on a free plan. We have detailed the process in the Namecheap section. While the process to update nameservers will vary from one registar to another, the logic will be the same.

TIP

In most cases, if you published your WeWeb app to a subdomain other than www (e.g. app or academy), it's because you already have a website using the www subdomain. If that's the case, think twice before redirecting your root domain to another subdomain.

`www`
`app`
`academy`
`www`
Users who type in a root domain name usually expect to land on the www subdomain. Sending them to one of your apps and not your main website could be very confusing.

`www`

## Cloudflare ​


### DNS records ​

To create the two required CNAME records in Cloudflare:

- on the Website tab of your dashboard, select the project you want to configure
- select DNS > Records in the side menu
- click on Add record
- create two CNAME records using the values provided in WeWeb

`Website`
`DNS`
`Records`
`Add record`


WARNING

Make sure the Proxy status is disabled and says DNS only on both records.

`Proxy status`
`DNS only`
It can take up to 48 hours for the new CNAME records to take affect. You can check the progress on the DNS checker website

Once DNS records are fully propagated, your website should be live on your domain.


### Root domain redirection ​

If you chose to publish your WeWeb app on the www subdomain, you will most likely want to setup a redirection from your root domain (e.g. yourdomain.com) to that subdomain (i.e. www.yourdomain.com).

`www`
`yourdomain.com`
`www.yourdomain.com`
There are two steps to do this in Cloudflare while still supporting the https SSL certificate:

`https`
- create an alias for the root domain, and
- create a page rule to redirect traffic on the root domain to the https page on the subdomain

`https`

#### Alias record ​

To create a root domain alias in Cloudflare, add a new CNAME record with the Proxy status enabled that makes the root domain an alias of your www subdomain:

`Proxy status`
`www`


WARNING

For this record, make sure the Proxy status is Proxied.

`Proxy status`
`Proxied`

#### Page rule ​

To create a root domain redirection page rule in Cloudflare:

- make sure you're in the right project
- go to Rules > Page Rules
- type in the root domain with a /* wildcard at the end to include all the pages on the domain (e.g. yourdomain.com/*)
- choose the Forwarding URL setting with a 301 - Permanent redirect to ensure the redirection is permanent
- type in the URL where users should be redirected. This time, make sure it: starts with https:// at the beginning and the subdomain you want to redirect to (usually https://www.), andends with /$1 so the redirection URL is dynamic (i.e. so that if someone types in yourdomain.com/dashboard, they are redirected to the dashboard page, not just the homepage of your app)
- starts with https:// at the beginning and the subdomain you want to redirect to (usually https://www.), and
- ends with /$1 so the redirection URL is dynamic (i.e. so that if someone types in yourdomain.com/dashboard, they are redirected to the dashboard page, not just the homepage of your app)
- don't forget to save and deploy the page rule

`Rules`
`Page Rules`
`/*`
`yourdomain.com/*`
`Forwarding URL`
`301 - Permanent redirect`
- starts with https:// at the beginning and the subdomain you want to redirect to (usually https://www.), and
- ends with /$1 so the redirection URL is dynamic (i.e. so that if someone types in yourdomain.com/dashboard, they are redirected to the dashboard page, not just the homepage of your app)

`https://`
`https://www.`
`/$1`
`yourdomain.com/dashboard`
`dashboard`


Once you save the page rule, it should look something like this (make sure the Action option is enabled):

`Action`


TIP

In most cases, if you published your WeWeb app to a subdomain other than www (e.g. app or academy), it's because you already have a website using the www subdomain. If that's the case, think twice before redirecting your root domain to another subdomain.

`www`
`app`
`academy`
`www`
Users who type in a root domain name usually expect to land on the www subdomain. Sending them to one of your apps and not your main website could be very confusing.

`www`

## Namecheap ​


### DNS Records ​

To add the two required CNAME records in Namecheap go to Domain List > Manage:

`Domain List`
`Manage`


In the Advanced DNS menu, click on Add new record and copy/paste the information from your WeWeb project. It should look something like this:

`Advanced DNS`
`Add new record`


- Both records should be of Type CNAME
- Replace Host by the Name value in WeWeb
- Replace Value by the Data value in WeWeb
- You can leave the TTL value as Automatic

`Type`
`CNAME`
`Host`
`Name`
`Value`
`Data`
`TTL`
`Automatic`
Once you've saved the changes, it can take up to 48 hours for the new CNAME records to take affect. You can check the progress on the DNS checker website. Once DNS records are fully propagated, your website should be live on your domain.


### Root domain redirection ​

If you chose to publish your WeWeb app on the www subdomain, you will most likely want to setup a redirection from your root domain (e.g. yourdomain.com) to that subdomain (i.e. www.domain.com).

`www`
`yourdomain.com`
`www.domain.com`
TIP

In most cases, if you published your WeWeb app to a subdomain other than www (e.g. app or academy), it's because you already have a website using the www subdomain. If that's the case, think twice before redirecting your root domain to another subdomain.

`www`
`app`
`academy`
`www`
Users who type in a root domain name usually expect to land on the www subdomain. Sending them to one of your apps and not your main website could be very confusing.

`www`
At the time of writing, Namecheap does not support naked domain redirects for https because their redirect server can't provide SSL service. You can, however, use Cloudflare on a free plan to handle your DNS settings and setup a permanent 301 redirection from your root domain to the www subdomain.

`https`
`www`
In your Cloudflare account, when you add a site, you are invited to:

- type in the domain name of the website, and
- choose a plan.



Assuming your domain name was not purchased on or transferred to Cloudflare, you will then be invited to replace the default nameservers of your domain registar (in this case Namecheap) with Cloudflare nameservers:



In Namecheap, you can do this by going to your Domain list and clicking on Manage, then choosing the Custom DNS option in the Nameservers section of the page:

`Domain list`
`Manage`
`Custom DNS`
`Nameservers`


WARNING

Once you've updated the nameservers in your domain registar, you can click on the Check nameservers button in Cloudflare to speed up the process but updating the nameservers can take a few hours regardless:

`Check nameservers`


Be patient. Cloudflare will send you an email and update the project dashboard once its done:



Once this process is complete, you should be able to see your DNS records in Cloudflare.

However, you'll still want to:

- ensure the two CNAME records provided by WeWeb are properly setup in Cloudflare
- create a new CNAME record to alias the root domain
- create a page rule to redirect users from your root domain to the www subdomain

`www`
Please refer to our step-by-step Cloudflare guide to ensure your DNS records are setup properly and create a redirection page rule.


## GoDaddy ​

In your GoDaddy dashboard, go to My Products where you will find your list of domain names.

`My Products`
Click on DNS for the domain you want to add to WeWeb:

`DNS`


On the DNS management page, click on Add:

`DNS management`
`Add`


Add 2 records like the following images:



- Both records should be of Type CNAME
- Replace Host by the Name value displayed in WeWeb
- Replace Points to by the Data value displayed in WeWeb

`Type`
`CNAME`
`Host`
`Name`
`Points`
`Data`

## OVH ​

On your dashboard, go to Domain names, then click on the domain you want to link to WeWeb:



👉 Click on DNS Zone:



👉 Click on Add an entry to add two entries like the following images:



- Both records should be of Type CNAME
- Replace Sub-domain by the Name value displayed in WeWeb
- Replace Target to by the Data value displayed in WeWeb

`Type`
`CNAME`
`Sub-domain`
`Name`
`Target`
`Data`

## Google ​

Go to My domains in your Google domains dashboard, then click Manage next to the domain you want to add to WeWeb:

`Manage`


Click on DNS and scroll to Custom resource records:

`DNS`
`Custom resource records`


Add 2 records like the following image:



- Both records should be of Type CNAME
- Replace Name (@) by the Name value displayed in WeWeb
- Replace Data (Domain name) to by the Data value displayed in WeWeb

`Type`
`CNAME`
`Name (@)`
`Name`
`Data (Domain name)`
`Data`

## Gandi ​

Go to Domain in your Gandi dashboard, and click on the domain you want to connect to WeWeb:



Click on DNS Records > Add:

`DNS Records`
`Add`


Add 2 records like the following images:



- Both records should be of Type CNAME
- Replace Name by the Name value displayed in WeWeb
- Replace Hostname to by the Data value displayed in WeWeb

`Type`
`CNAME`
`Name`
`Name`
`Hostname`
`Data`
