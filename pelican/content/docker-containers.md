Title: Docker containers
Date: 2017-04-19 14:11
Category: Computers

First time I heard about [docker](https://www.docker.com/) containers I thought: "Well this is a great idea!".
When I tried to install them, however, I gave up on the idea.
The biggest problem for me was the time it takes to get the containeers up and running.
For someone whose job is to deploy software this is a great help but for everybody else
the overhead is not be worth the benefit.

This excuse stopped to make sense when I tried to configure [Travis-CI](https://travis-ci.org/) for [yambopy](https://github.com/henriquemiranda/yambopy).
Travis-CI is a great tool to test software in an automatic way, you should check it out.
Talking from my little personal experience, if you have your
code hosted on github you can get the basic setup of Travis-CI running with a couple of clicks.
To configure the tests and to get them to run is, however, a much more difficult problem.
At some point I will write here about that as well.

Now you might ask what is really the relation between Travis-CI and docker?
The connection became apparent when I tried to setup the environment to run the yambopy test suite in Travis-CI.
I looked how I could run the Travis-CI environment locally, and found this [post](http://stackoverflow.com/questions/21053657/how-to-run-travis-ci-locally) in StackOverflow.

There I realized that the images used by Travis-CI to run the different environments are available in
[Quay.io](https://quay.io/organization/travisci).
I decided then to try to run the container on my local machine and make sure everything works properly. This helped to write the ``travis.yaml`` file needed by Travis-CI. Here is a short description of the steps I took.

First you need to install ``docker`` and ``docker-machine`` on your computer.
In my case since I have a Mac with OSX and macports I just typed:

    :::bash
    sudo port install docker-machine docker-compose docker

Then you need to start the ``docker-machine``:

    :::bash
    docker-machine start

Then download the image you want to use:

    :::bash
    docker run -it quay.io/travisci/travis-python /bin/bash

And login in to it.
This is about it, once you are logged in, you have an operating system inside a docker container.
You can install your software in it and make sure it runs.
Then you can move this container to any other computer and you can be sure it will run there as well.

One important distinction is the difference between images and containers.
Images contain the operating system and are static.
Containers are the virtual systems that use the image plus a series of commands to bring the environment you want.
When you want to run a container in another computer, you just need to download the image in that
computer, and move the container there.
This simple idea, the containers, offer many possibilities.
I will come back to this topic with more details about my personal experience.
