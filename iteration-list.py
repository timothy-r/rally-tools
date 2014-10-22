import sys
from pyral import Rally, rallyWorkset

# useage python create-review.py --config=my.cfg StoryId

options = [arg for arg in sys.argv[1:] if arg.startswith('--')]
args    = [arg for arg in sys.argv[1:] if arg not in options]

server, user, password, apikey, workspace, project = rallyWorkset(options)

rally = Rally(server, user, password, workspace=workspace, project=project)
rally.enableLogging('mypyral.log')

# create query
for story in rally.get('UserStory', query='FormattedID = ' + args[0]):

    iteration = story.Iteration

    for sty in rally.get('UserStory', query='Iteration.oid = ' + iteration.oid):
        print "%s %s" % (sty.FormattedID, sty.Name)
        print ""
        print "%s" % (sty.Description)
        print ""

