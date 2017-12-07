# Whiteboard
Whiteboard for my office/classroom...uses a Flask server and AJAX calls with a sqlite db to serve information.


## Purpose
I have this set up in my classroom so students/faculty know where I can be found. Automation is incoporated using technologies like IFTTT with an Android phone to utilize both GPS data and SSID for our WAPs to narrow down location without the constant user-completed updates.


## Function
The Flask server has two endpoints: one as the index - displaying the information - and one as the route for handling the incoming POST request with a Twilio phone number. When the message is sent with the correct keyword(s), the server responds by sending a confirmation message to the user and updating the db. AJAX is used on the index to dynamically update the page's content.
