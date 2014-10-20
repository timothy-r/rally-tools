import sys
from pyral import Rally, rallyWorkset

options = [arg for arg in sys.argv[1:] if arg.startswith('--')]
args    = [arg for arg in sys.argv[1:] if arg not in options]
server, user, password, apikey, workspace, project = rallyWorkset(options)

rally = Rally(server, user, password, workspace=workspace, project=project)
rally.enableLogging('mypyral.log')

story_id = 23700352473
response = rally.get('UserStory', query='oid=23700352473')
print response

'''story_titles = [story.Name for story in response]

for title in story_titles:
        print title
        '''
