import sys
from pyral import Rally, rallyWorkset

options = [arg for arg in sys.argv[1:] if arg.startswith('--')]
args    = [arg for arg in sys.argv[1:] if arg not in options]
server, user, password, apikey, workspace, project = rallyWorkset(options)

rally = Rally(server, user, password, workspace=workspace, project=project)
rally.enableLogging('mypyral.log')

workspaces = rally.getWorkspaces()
for wksp in workspaces:
    print "%s %s" % (wksp.oid, wksp.Name)
    projects = rally.getProjects(workspace=wksp.Name)
    for proj in projects:
        print "    %12.12s  %s" % (proj.oid, proj.Name)
