# catfacts

An example sms flask client that can be deplyed to heroku.

Built for my talk at Open Source Bridge 2015


## How to deploy

1. First, clone this repo locally
2. Ensure you have the heroku toolbelt installed: https://devcenter.heroku.com/articles/getting-started-with-python#set-up
3. run the following command:

  $ heroku create

4. run:

  $ git push heroku master

5. Build tables on heroku mysql instance

6. run:

  $ heroku ps:scale web=1

7. Copy the URL generated, and enter the URL with the SECRET_KEY appended into Twilio's management console for SMS. 
8. Text the number for your response!
