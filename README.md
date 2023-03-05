
**Table of Contents**

[TOCM]

[TOC]

## Setup
### Requirements
- #### You need python that you can download from [here](https://www.python.org/downloads/ "here").
- #### The git must be installed. You can install git from this [site](http://git-scm.com/ "site").
- #### You must install *pip*. [There](https://pip.pypa.io/en/stable/installation/ "There") is guide, but if you have python run this in the terminal: ``` py get-pip.py```.

### Setup the project
- #### Clone the repository
``` git
git clone https://github.com/Gyulaa/Clan-Simulator-in-Browser.gitgit clone https://github.com/Gyulaa/Clan-Simulator-in-Browser.git```

- #### Navigate to the project directory
``` terminal
cd Clan-Simulator-in-Browser```

- #### Create and activate a virtual environment
``` terminal
virtualenv env
env\Scripts\activate```

- #### Install project dependencies
``` terminal
pip install -r requirements.txt```

- #### Create a superuser for Django admin
``` terminal
cd Clan_Simulator
python manage.py createsuperuser```

- #### Apply database migrations
``` terminal
python manage.py migrate```

- #### Run the development server
``` terminal 
python manage.py runserver```

## Usage
- #### Open a web browser and go to `http://localhost:8000` to view the app.
- #### Once the app is running, you can view a list of the members and their properties.
- #### To add a new member, go to the operations tab and click to the *New member* button. Then add the father and the name of the new member.
