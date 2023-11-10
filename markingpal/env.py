import os


def set_env():
    if 'OPENAI_API_KEY' in os.environ:
        return

    home_directory = os.path.expanduser("~")
    env = ".devitopro/env"
    env_fullpath = os.path.join(home_directory, env)

    if not os.path.isfile(env_fullpath):
        msg = f'No {env} file found in home directory.'
        raise FileNotFoundError(msg)

    # Open the .env file
    with open(env_fullpath, 'r') as file:
        for line in file:
            line = line.strip()
            if line.startswith('#') or line == '':
                continue

            key, value = line.strip().split('=', 1)
            os.environ[key] = value

    if 'OPENAI_API_KEY' not in os.environ:
        msg = "OPENAI_API_KEY environment variable is not set."
        raise EnvironmentError(msg)


if __name__ == '__main__':
    set_env()
