# Deployment

## Development

There are two options for running this app: either locally or on a container.

### Container

This one is easy: `docker-compose up (-d) (--build)`

You will need to install docker, docker-compose. This supports hot-reloading (though it may crash and not restart on an error). Before running, make sure required environment variables are set.

## Required Environment Variables

Two environment files are required. These are included in the .gitignore, and will not be pushed upstream with any changes you make.

A [sengrid](https://sendgrid.com/) account is required. Don't worry, it's totally free.

In `db-local.env`:

```.env
POSTGRES_DB=<postgres database name>
POSTGRES_USER=<username>
POSTGRES_PASSWORD=<admin password>
POSTGRES_HOST=db
```

In `app.env`:

```.env
SECRET=<secret of at least 24chars>
SENDGRID_API_KEY=<sendgrid api key>
DOMAIN=<set as localhost if running locally with docker compose>

DJANGO_SUPERUSER_USERNAME=<your personal email account>
DJANGO_SUPERUSER_PASSWORD=<sample password>
... all other environment variables as defined below.
```

## Local Deployment

You shouldn't do this. Using docker compose is sgnificantly easier. If you really want to, see setup below and then run `python manage.py runserver` and the server will run on port 8000.

## Setup

Needs: Python 3.X, virtualenv

- `git clone https://github.com/hackupc/registration && cd registration`
- `virtualenv env --python=python3`
- `source ./env/bin/activate`
- `pip install -r requirements.txt`
- (Optional) If using Postgres, set up the necessary environment variables for its usage before this step
- `python manage.py migrate`
- `python manage.py createsuperuser` (creates super user to manage all the app)

## Available enviroment variables

- **SG_KEY**: SendGrid API Key. Mandatory if you want to use SendGrid as your email backend. You can manage them [here](https://app.sendgrid.com/settings/api_keys).  Note that if you don't add it the system will write all emails in the filesystem for preview.
You can replace the email backend easily. See more [here](https://djangopackages.org/grids/g/email/).
- **PROD_MODE**(optional): Disables Django debug mode.
- **SECRET**(optional): Sets web application secret. You can generate a random secret with python running: `os.urandom(24)`
- **DATABASE_SECURE**(optional): Whether or not to use SSL to connect to the database. Defaults to `true`.
- **DOMAIN**(optional): Domain where app will be running. Default: localhost:8000
- **SL_TOKEN**(optional): Slack token to invite hackers automatically on confirmation. You can obtain it [here](https://api.slack.com/custom-integrations/legacy-tokens)
- **SL_TEAM**(optional): Slack team name (xxx on xxx.slack.com)
- **DROPBOX_OAUTH2_TOKEN**(optional): Enables DropBox as file upload server instead of local computer. (See "Set up Dropbox storage for uploaded files" below)
- **SL_BOT_ID**(optional): Slack bot ID to send messages from.
- **SL_BOT_TOKEN**(optional): Slack bot token to send messages.
- **SL_BOT_CHANNEL**(optional): General channel to refer from the bot messages.
- **SL_BOT_DIRECTOR1**(optional): User ID of one of the directors.
- **SL_BOT_DIRECTOR2**(optional): User ID of the other director.
- **MLH_CLIENT_SECRET**(optional): Enables MyMLH as a sign up option. Format is `client_id@client_secret` (See "Set up MyMLH" below)
- **CAS_SERVER**(optional): Enables login for other platforms

-----
# Legacy Documentation

We didn't write this app, so in case something breaks these docs are being kept around in case they're needed

### Local environment

- Set up (see above)
- `python manage.py runserver`
- Set cron for cas service:
```
0   0  * * * cd /home/user/project_folder/ && manage.py clearsessions
*/5 *  * * * cd /home/user/project_folder/ && manage.py cas_clean_tickets
5   0  * * * cd /home/user/project_folder/ && manage.py cas_clean_sessions
```
- Sit back, relax and enjoy. That's it!

### Local Production Environment

> Do not do this. Use docker compose please. Nginx is also no longer needed in the updated version.

Inspired on this [tutorial](https://www.digitalocean.com/community/tutorials/how-to-set-up-django-with-postgres-nginx-and-gunicorn-on-ubuntu-16-04) to understand and set it up as in our server.

- Set up (see above)
- Create server.sh from template: `cp server.sh.template server.sh`
- `chmod +x server.sh`
- Edit variables to match your environment and add extra if required (see environment variables available above)
- Create restart.sh from template: `cp restart.sh.template restart.sh`
- `chmod +x restart.sh`
- Edit variables to match your environment and add extra if required (see environment variables available above)
- Run `restart.sh`. This will update the database, dependecies and static files.
- Set up Systemd (read next section)

#### Set up gunicorn service in Systemd
Needs: Systemd.

- Edit this file `/etc/systemd/system/backend.service`
- Add this content
```
[Unit]
Description=backend daemon
After=network.target

[Service]
User=user
Group=www-data
WorkingDirectory=/home/user/project_folder
ExecStart=/home/user/project_folder/server.sh >>/home/user/project_folder/out.log 2>>/home/user/project_folder/error.log

[Install]
WantedBy=multi-user.target

```

- Replace `user` for your linux user.
- Replace `project_folder` by the name of the folder where the project is located
- Create and enable service: `sudo systemctl start backend && sudo systemctl enable backend`


#### Set up Postgres

Needs: PostgreSQL installed

- Enter PSQL console: `sudo -u postgres psql`
- Create database: `CREATE DATABASE backend;`
- Create user for database: `CREATE USER backenduser WITH PASSWORD 'password';` (make sure to include a strong password)
- Prepare user for Django

```sql
ALTER ROLE backenduser SET client_encoding TO 'utf8';
ALTER ROLE backenduser SET default_transaction_isolation TO 'read committed';
ALTER ROLE backenduser SET timezone TO 'UTC';
```

- Grant all priviledges to your user for the created database: `GRANT ALL PRIVILEGES ON DATABASE myproject TO myprojectuser;`
- Exit PSQL console: `\q`

Other SQL engines may be used, we recommend PostgreSQL for it's robustness. To use other please check [this documentation](https://docs.djangoproject.com/en/1.11/ref/databases/) for more information on SQL engines in Django.

##### Automatic Dropbox backup

Hackers data is really important. To ensure that you don't lose any data we encourage you to set up automatic backups. One option that is free and reliable is using the PostgresSQLDropboxBackup script.

Find the script and usage instructions [here](https://github.com/casassg/PostgreSQL-Dropbox-Backup)

#### Set up Dropbox storage for uploaded files

This will need to be used for Heroku or some Docker deployments. File uploads sometimes don't work properly on containerized systems.

1. Create a [new Dropbox app](https://www.dropbox.com/developers/apps)
2. Generate Access token [here](https://blogs.dropbox.com/developers/2014/05/generate-an-access-token-for-your-own-account/)
3. Set token as environment variable **DROPBOX_OAUTH2_TOKEN**

#### Set up MyMLH

MyMLH is a centralized login system used by MLH.  It makes it easier for hackers to sign up for more events without re-entering their data every time around.

This integration allows hackers to have part of their application completed using their information from MLH.

As of the moment, MyMLH can only be used to sign up. This decision is due to the fact that MyMLH can have accounts with emails not verified. This can be a security concern as someone could create an account with someone else's email and it would totally invalidate our verification email system.
In that direction the approach taken is to extract fields and use them for the application during the sign up process.

1. Create a [new MyMLH app](https://my.mlh.io/oauth/applications/new).
2. Add `https://DOMAIN//user/callback/mlh/` as a Redirect URI. Replace `DOMAIN` for the domain used to deploy your system. Ex: `http://registration.gerard.space/user/callback/mlh/`.
3. Set **MLH_CLIENT_SECRET** using the strings in `Application ID` and `Secret` fields, concatenated with a `@`. Ex: `application_id@secret`.

Note that to test locally you will need to add a line where `DOMAIN` is `localhost:8000`.

#### Set up nginx

Needs: Nginx

- `sudo vim /etc/nginx/sites-available/default`
- Add site:

```
server {
    listen 80;
    listen [::]:80;

    server_name my.hackupc.com;


    location = /favicon.ico { access_log off; log_not_found off; }
    location /static/ {
        alias /home/user/project_folder/staticfiles/;
    }

    location /files/ {
        alias /home/user/project_folder/files/;
    }

    location / {
        include proxy_params;
        proxy_pass http://unix:/home/user/project_folder/backend.sock;
        client_max_body_size 5MB;
    }


}
```

#### Deploy new version

- `git pull`
- `./restart.sh`
- `sudo service backend restart`



## Management

### Automated expiration

- Create management.sh from template: `cp management.sh.template management.sh`
- `chmod +x management.sh`
- Edit variables to match your environment and add extra if required (see environment variables available above)
- Add to crontab: `crontab -e`
```
*/5 * * * * cd /home/user/project_folder/ && ./management.sh > /home/user/project_folder/management.log 2> /home/user/project_folder/management_err.log
```

### User roles

- **is_volunteer_accepted**: Allows user to check-in hackers with QR and list view
- **is_organizer**: Allows user to vote, see voting ranking and check-in hackers.
- **is_director**: Allows user to send invites to hackers as well as send reimbursement. Also can review dubious applications.
- **is_admin**: Allows user to enter Django Admin interface
- **can_review_dubious**: User can review and mark as safe applications that seem weird.
- **can_review_blacklist**: User can review and mark as blacklist applications that their user seem to be in the blacklist.

### Important SQL queries

Here are several queries that may be useful during the hackathon application process.

1. `source ./env/bin/activate`
2. `python manage.py dbshell`
3. Run SQL query
4. Extract results

#### Missing applications emails

Emails from users that have registered but have not completed the application.

```sql
SELECT u.email
FROM user_user u
WHERE NOT is_director AND NOT is_volunteer AND NOT is_organizer
AND u.id NOT IN
(SELECT a.user_id FROM applications_application a);
```

## Use in your hackathon

You can use this for your own hackathon. How?

- Fork this repo
- Update [app/hackathon_variables.py](app/hackathon_variables.py)
- Get SendGrid API Key (Sign up to [GitHub Student Pack](https://education.github.com/pack) to get 15K mails a months for being an student)
- Deploy into your server or in Heroku (see above)!

## Personalization

### Style

- Colors and presentation: [app/static/css/main.css](app/static/css/main.css).
- Navbar & content/disposition: [app/templates/base.html](app/templates/base.html)
- Email base template: [app/templates/base_email.html](app/templates/base_email.html)
- Update favicon [app/static/](app/static/)


### Content

#### Update emails:

You can update emails related to
- Applications (application invite, event ticket, last reminder) at [applications/templates/mails/](applications/templates/mails/)
- Reimbursements (reimbursement email, reject receipt) at [reimbursement/templates/mails/](reimbursement/templates/mails/)
- User registration (email verification, password reset) at [user/templates/mails/](user/templates/mails/)

#### Update hackathon variables
Check all available variables at [app/hackathon_variables.py.template](app/hackathon_variables.py.template).
You can set the ones that you prefer at [app/hackathon_variables.py](app/hackathon_variables.py)

#### Update registration form
You can change the form, titles, texts in [applications/forms.py](applications/forms.py)

#### Update application model
If you need extra labels for your hackathon, you can change the model and add your own fields.

   - Update model with specific fields: [applications/models.py](applications/models.py)
   - `python manage.py makemigrations`
   - `python manage.py migrate`