import sys
from pyral import Rally, rallyWorkset

options = [arg for arg in sys.argv[1:] if arg.startswith('--')]
args    = [arg for arg in sys.argv[1:] if arg not in options]
server, user, password, apikey, workspace, project = rallyWorkset(options)

rally = Rally(server, user, password, workspace=workspace, project=project)
rally.enableLogging('mypyral.log')

response = rally.get('UserStory', query='FormattedID = id')
print response

for story in response:
    #print story.details()
    for case in story.TestCases:
        print case.Name
        print case.Description
