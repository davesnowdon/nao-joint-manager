'''
Created on Dec 31, 2012

@author: dns
'''

import sys
import time

from naoqi import ALProxy
from naoqi import ALBroker
from naoqi import ALModule

from JointManager import JointManager
from JointManager import Joint
from JointManager import JOINT_NAMES

ROBOT_IP='192.168.0.43'
ROBOT_PORT=9559

memory = None
motion = None
tts = None



class Reflex():
    def __init__(self, manager):
        self.manager = manager
        rsp = self.manager.get_joint('RShoulderPitch')
        rsp.attach(self)
    
    def update(self, joint):
        print joint.name + ' = ' + str(joint.angle)

def StiffnessOn(proxy):
    # We use the "Body" name to signify the collection of all joints
    pNames = "Body"
    pStiffnessLists = 1.0
    pTimeLists = 1.0
    proxy.stiffnessInterpolation(pNames, pStiffnessLists, pTimeLists)


def make_broker(ip,port):
    return ALBroker("reflex", '0.0.0.0', 0, ip, port)

# Ideas for defining main() from http://www.artima.com/weblogs/viewpost.jsp?thread=4829
def main(argv=None):
    broker = make_broker(ROBOT_IP, ROBOT_PORT)
    
    global memory
    try:
        memory = ALProxy('ALMemory')
    except Exception, e:
        print "Could not create proxy to ALMemory"
        print "Error was: ", e

    
    global motion
    try:
        motion = ALProxy('ALMotion')
    except Exception, e:
        print "Could not create proxy to ALMotion"
        print "Error was: ", e

    global tts
    try:
        tts = ALProxy('ALTextToSpeech')
    except Exception, e:
        print "Could not create proxy to ALTextToSpeech"
        print "Error was: ", e

    manager = JointManager(motion, 0.1, True)
    reflex = Reflex(manager)
    
    manager.start()

    # Set NAO in Stiffness On
    #StiffnessOn(motion)

    
    try:
        while True:
            time.sleep(1)
            
    except KeyboardInterrupt:
        print
        print "Interrupted by user, shutting down"
        manager.stop()
        broker.shutdown()
        sys.exit(0)

if __name__ == "__main__":
    sys.exit(main())