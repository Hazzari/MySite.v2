import fabric
import environ

env = environ.Env()
environ.Env.read_env(env_file='dev_aleksan/.env')

USER = env('USER_HOST')
PASSWORD = env('USER_PASSWORD')
HOST = env('HOST')
PORT = env('PORT')


def pull():
    with fabric.Connection(HOST, port=23332) as c:

        c.run('cd work/mysite/dev_aleksan'
              '&& git pull && source venv/bin/activate'
              '&& pip install -r requirements.txt'
              '&& python3 manage.py migrate')

        c.sudo('service gunicorn restart', password=PASSWORD)
        c.sudo('service gunicorn status', password=PASSWORD)

        c.sudo('service nginx restart ', password=PASSWORD)
        c.sudo('service nginx status', password=PASSWORD)


if __name__ == '__main__':
    pull()
