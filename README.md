nao-joint-manager
=================

Set of python classes to provide events on changes to NAO joint positions

Usage
=====
Create a proxy for ALMotion, for example

    motion = ALProxy('ALMotion', '127.0.0.1', 9559)

Create an instance of JointManager specifying the motion proxy, update interval (in seconds) and whether to use sensor values or not

    manager = JointManager(motion, 0.1, True)
    
You can then ask the Joint Manager for a specific joint

    joint = manager.get_joint('RShoulderPitch')
    
You can get the current joint name using joint.name and the angle using joint.angle
    
Ask the joint to notify you when the joint angle changes

    joint.attach(observer)

The observer object needs to have a method update accepting the modified joint as a parameter

```python    
class Observer():

	# ...
    
    def update(self, joint):
        print joint.name + ' = ' + str(joint.angle)
        
    # ...
```