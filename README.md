# Clan Simulator
## Setup
### Requirements
- #### You need python that you can download from [here](https://www.python.org/downloads/ "here").
- #### The git must be installed. You can install git from this [site](http://git-scm.com/ "site").
- #### You must install *pip*. [There](https://pip.pypa.io/en/stable/installation/ "There") is guide, but if you have python run this in the terminal: ``` py get-pip.py```.

### Setup the project
- #### Clone the repository
<pre>
git clone https://github.com/Gyulaa/Clan-Simulator-in-Browser.gitgit clone https://github.com/Gyulaa/Clan-Simulator-in-Browser.git
</pre>

- #### Navigate to the project directory
<pre>
cd Clan-Simulator-in-Browser
</pre>

- #### Create and activate a virtual environment
<pre>
virtualenv env
env\Scripts\activate
</pre>

- #### Install project dependencies
<pre>
pip install -r requirements.txt
</pre>

- #### Create a superuser for Django admin
<pre>
cd Clan_Simulator
python manage.py createsuperuser
</pre>

- #### Apply database migrations
<pre>
python manage.py migrate
</pre>

- #### Run the development server
<pre>
python manage.py runserver
</pre>

## Usage
- #### Open a web browser and go to `http://localhost:8000` to view the app.
- #### Once the app is running, you can view a list of the members and their properties.
- #### To add a new member, go to the operations tab and click to the *New member* button. Then add the father and the name of the new member.
