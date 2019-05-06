'''
Created on Oct 22, 2015

@author: uidj6043
'''

from MksApi.mkslibapi import MksCommand
from MksJenkins import MksJenkins


class MksCommands(object):
    
    def generateAllIssues(self, session):
        queryName = MksJenkins()
        print("Query Issues: ",queryName.getQueryIssues())
        cmd = MksCommand("im","issues")        
        cmd.add_option("query", queryName.getQueryIssues())
        cmd.add_option("fields", "State,Detected By,Importance,Summary,Created Date,Assigned User,Structure Element")
        res = session.run_cmd(cmd)
        return res
    
    def generateSE(self, session):
        querySe = MksJenkins()
        print("Query SE: ",querySe.getQuerySE())
        cmd = MksCommand("im","issues") 
        cmd.add_option("query", querySe.getQuerySE()) 
        cmd.add_option("fields","Title.fva,Project,Default Assigned User for Issue.fva,Default Responsible Person for Realization Order.fva,Responsible Person.fva,Responsible for Requirements.fva")
        res = session.run_cmd(cmd)
        return res
    

       
     
        
        
    