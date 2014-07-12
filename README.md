# Kanri
Kanri is a custom-built management system for CoderDojo @ Curtin. Chances are it's useless to you, but y'know...open-source is good.

## Installing
To install, you'll need:

- Python, most likely 2.7
- The modules specified in `requirements.txt` (more on that later).

## Installing the modules
To install the necessary modules, run `pip install -r requirements.txt`.
That's it!

## Setting up the environment
To reduce complication, I've enlisted the help of environment variables to do some of the configuration:
- `KANRI_SECRET_KEY`: a random string used as a seed for a lot of secret stuff in Kanri. Make it up, keep it secret.
- `KANRI_AUSPOST_KEY`: an Australia Post API key, you can register for one online, it's free.

## Configurating the database
Kanri's Django configuration file is configured to use SQLite, with the exception of when it detects it's running on Heroku, in which case it'll
use Heroku's Postgres stack.

## Have fun!