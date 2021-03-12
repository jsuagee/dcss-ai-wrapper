class DefaultConfig:
    socketpath = '/var/tmp/crawl_socket'
    agent_name = 'aiagent'
    crawl_socketpath = 'crawl/crawl-ref/source/rcs/' + agent_name + ':test.sock'


class WebserverConfig:
    server_uri = 'ws://127.0.0.1:8080/socket'
    server_ip = '127.0.0.1'
    server_port = '8080'
    agent_name = 'midca'
    agent_password = 'midca'

    # game_id is the type of game to play on the server
    #   'dcss-web-trunk'   - play trunk no seed
    #   'seeded-web-trunk' - play a seeded version of the game
    #   'tut-web-trunk'    - play a tutorial
    game_id = 'dcss-web-trunk'

    seed = 4675233756386659716

    tutorial_number = 1

    # TODO - actually use this somewhere
    start_new_game_on_death = True


class CharacterCreationConfig:
    species = 'Human'  # species name must match exactly to the string in the dcss menu after the dash, i.e. a hill orc is "Hill Orc"
    background = "Enchanter"  # background name must match exactly to the string in the dcss menu after the dash
    starting_weapon = "hand axe"  # starting_weapon name must match exactly to the string in the dcss menu after the dash


class AIConfig:
    # any class that is in agent.py and is a subclass of Agent may be set as the ai_python_class
    #
    ai_python_class = 'FastDownwardPlanningAgent'

