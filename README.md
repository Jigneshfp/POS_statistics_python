# Post-demonetization digital transaction data analysis 
![alt text](http://blog.unibulmerchantservices.com/wp-content/uploads/2011/09/POS-Terminal-Risk-Management-Rules-You-Need-to-Know.jpg)

### Summary
This is a small exploratory data analysis and data visualization project on digital transaction using PoS( Point of sale) terminals before and after demonetisation in india.
Digital payments using debit and credit cards at Point of Sale (Pos) terminals has accelerated very quickly after demonetisation and goverment's effort to push for digital payments. Post-demonetisation, banks have been able to install large number of PoS terminals. As a result, we have observed sharp growth in digital payments. Here I will explore how the picture of digital payment has changed after demonetisation. 

### Objectives of this project
* To clean multiple data files (total 24 files but very small in size !) which I have downloaded from https://rbi.org.in/Scripts/ATMView.aspx.
* To merge cleaned data together which is fragmented in total 24 data files. 
* To do exploratory data analysis using data visualization.

### How to replicate/run this analysis:
* Clone down this repository on your machine 
* Extract all files into your working directory
* Make sure to keep all 24 data files (all excel files) which are in **data** folder and code file **POS_digital.ipynb** into same directory
* Run **POS_digital.ipynb** in jupyter notebook (ensure the working directory is set to the above directory)

### Refelction on the project
Originally I wanted to scrape data directly from the [RBI website](https://rbi.org.in/Scripts/ATMView.aspx) and do the data analysis so that I don't have to download data files for this project separately. However, adding web scraping had dramatically slowed down execution time of running the entire script. I wanted to make sure it runs little faster and for that I downloaded all files beforehand.
