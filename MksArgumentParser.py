'''
Created on Oct 22, 2015

@author: uidj6043
'''

class MksArgumentParser(object):
    
    def parseArguments(self,parser):
        parser.add_argument('--mks_user')
        parser.add_argument('--mks_pass')

        parser.add_argument('--mks_host Ana')
        parser.add_argument('--im_port', type=int)
    
        args = parser.parse_args() 
        '''this is a comment
		used for a test in git training
		'''
        return args