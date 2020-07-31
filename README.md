# py-announce

py-announce is a Python tool to announce when an up-coming event in a Google calendar is about to occur. 
The intention is to help kids stay on schedule as they return to distance learning.

This script is intented to be run from a Raspberry-pi paired with a Bluetooth speaker that can be heard throughout your home.

## Installation

Download the code from this repo, then go to https://developers.google.com/calendar/quickstart/python to setup your API key and install the necessary packages.
You will also be required to download a credentials.json file from Google into the root of this project.

## Usage

I recommend creating a new calendar for the events that will be announced.  You can get the calendar ID from the
calendar settings in the Google Calendar site.

Once you have installed the credentials you obtained from Google and set the calendar ID do the following:  

1) Create an event in the calendar that will occur in the next 5 minutes.
2) Run the script.  You will be prompted to log-in when it is first run.

Once you confirm the script is working I recommend setting up a cronjob to execute the script every 5 minutes.  


## Contributing
Tweak and change the script as you like.  I'll make updates as I see fit later.  PRs are sometimes welcome.

## License
GNU GENERAL PUBLIC LICENSE