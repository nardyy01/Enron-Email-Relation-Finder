"# Enron-Email-Relation-Finder" 
**If you download the Enron email set, to run them against this program simply drop the folder containing the emails into my Email folder**

Objective
The goal for this mini project was creating a program that would be able to process a large quantity of emails, pulling out important
information which identified the relationship between receivers and senders of the emails and display them graphically through an HTML page.


Programs | Libraries 
->	Python
	o Re (Regular Expressions Library) *Regex*
	o Json (JS File Formatting and Dumping)
	o Os (Operating System Dependent Functionality for File Manipulation and Searching)
->	Notepad++
	o HTML
	o JS | Json File Storage
	o JQuery
Summarized Walk Through
->	Open a path to located folders and emails to traverse
	o The path specified will be walked using an os.walk call to gather all of the data
->	For each file opened, regex was used to pull the specific information needed
	o The regex expression used targeted From, To, Cc, Bcc, and forwarded emails
->	Data found from the regex was then sorted and stored in Json format
	o From and forwarded emails were linked with their respective recipients 
->	Used JQuery to load Json file into the JS/HTML code and generate a graph
	o JQuery bypassed the need for a webserver (Was unaware of webserver method then)

Conclusion
The mini project was a success overall. I was able to produce the intended result from my data pulling and successfully display a decently organized graph.
