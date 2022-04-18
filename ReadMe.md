# Phising Website Detector

This application was developed based on a DECISION TREE MODEL to detect if a URL is a phising website or not by inputing the following values:

* PrefixSuffix- (categorical - signed numeric) : { -1,1 }
* SubDomains (categorical - signed numeric) : { -1,0,1 }
* HTTPS (categorical - signed numeric) : { -1,1,0 }
* DomainRegLen (categorical - signed numeric) : { -1,1 }
* RequestURL (categorical - signed numeric) : { 1,-1 }
* AnchorURL (categorical - signed numeric) : { -1,0,1 }
* LinkslnScriptTags (categorical - signed numeric) : { -1,0,1 }
* WebsiteTraffic (categorical - signed numeric) : { -1,0,1 }
* ServerFormHandler (categorical - signed numeric) : { -1,0,1 }

To run the App, you need to have python installed in your computer and use it to load the app.py file.

