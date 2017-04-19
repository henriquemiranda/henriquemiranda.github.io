Title: Docker containers
Date: 2017-04-19 14:11
Category: Computers
Status: Draft

First time I heard about docker containers I thought: "Well this sounds like a great idea!".
Then I though how to install it on my computer and quickly gave up on the idea of even trying.
The biggest problem with this type of tools is that it takes a long time to get them up and running.
For someone whose job is to deploy software this can be of great help but for the common human being,
the overhead of learning a new tool might not be worth the time spent.

Now in my case all this stoped make sense when I tried to configure Travis-CI on yambopy.
Travis-CI is a great tool to test software in an automatic way. Talking from personal experience,
if you have your code hosted on github you can get the basic setup of Travis-CI running with a couple of clicks.
The configuration, however, is a totally different beast to tackle. At some point I will write here about
that as well.
Now you might ask what is really the relation between Travis-CI and docker? The connection became apparent to me
when I wanted to setup the environment to test software in Travis-CI and I asked the internet if I could run
the environment of Travis-CI locally, and already (as is most of the times the case) someone wondered
the same thing in this [post](http://stackoverflow.com/questions/21053657/how-to-run-travis-ci-locally) in StackOverflow.

There it says that, there is available in [Quay.io](https://quay.io/organization/travisci) the image that is
used by docker to run the different environments.
I decided then to give it a go. In the end it took me some time to understand how it works, but totally worth it.
I leave here a short description of the steps.

First you need to install ``docker`` and ``docker-machine`` on your computer.
In my case since I have a Mac with OSX and macports I just typed:

.. code-bash :: bash

    sudo port install docker-machine docker-compose docker


Then you need to start the ``docker-machine``:

.. code-bash :: bash

    docker-machine start

Then next step was to download the image we want to use:

.. code-bash :: bash

    docker run -it quay.io/travisci/travis-python /bin/bash

And login to it.
This is about it, once you are logged in, you have an operating system inside a container.
You can install your software in it and make sure it runs. Then you can move this container
to any other computer and you can be sure it will run there as well.

One important thing to know is the difference between images and containers.
Images contain the operating system and are static.
Containers are the virtual systems that use the image plus all the software you installed in them.
When you want to run a contrainer in another computer, you just need to download the image in that 
computer, and move the container there.
This simple concept offers many possibilities. For example, if you want to run your application on
the Amazon clusters.
