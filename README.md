# RASPARQ

RASPARQ is a Python script for scraping whole books off tombo.pt. The site provides a viewer, but if you're like me, you find it to be a bit annoying and would rather skim archives in your own preferred image viewer.

RASPARQ will get all images from a particular 'book' that lives behind a url.

## How to use

* Clone the repo
* Install the requirements
* Make sure you have firefox (or change the browser on line 9 of rasparq.py)
* Update the `target_url` on line 6
* run the script
* You might get a popup asking what to do with the file – select save file and do the action for all files, then you end up with individual image files for each page in the book