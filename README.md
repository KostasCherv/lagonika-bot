# A Python bot to notify about new deals
Scraping content of https://www.lagonika.gr and send email in case of a new deal added.

### Used
* Python 
* BeautifulSoup4
* Smtplib
* Dotenv
* Schedule

### Mandatory Environment Variables
* RECIPIENTS - comma separated emails
* GOOGLE_EMAIL - google account to use as email sender
* GOOGLE_PASSWORD - google app password
* INTERVAL_SECONDS - interval to check for new items

## Heroku deployment
1. Create new heroku app
   
	```heroku create```

2. push the branch on heroku
   
	```git push heroku main```

3. ensure a dyno running for worker by executing
   
	```heroku ps:scale worker=1```