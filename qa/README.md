# How to run custom docker build for suricata-6.0.0-dev
- Uses patched Dockerfile to install cbindgen dependency.
- Uses patched prscript.py and buildbot.cfg for compability with newer versions of buildbot.
- Fixes running pcap builder without using `sudo`.
- Adds ability to specify docker image to use.

1. Build an updated docker image with the beardnecks patch
```bash
cd suricata/qa
git clone git@github.com:beardnecks/suri-docker-qa.git
cd suri-docker-qa
docker build . -t suri-buildbot:beardnecks
```

2. Create/run the container with the prscript/buildbot.cfg patch
```bash
pip install docker # add docker package to your python3 environment

# checkout an updated version of the prscript.py and the buildbot.cfg
git remote add simdugas git@github.com:simdugas/suricata.git
git remote update simdugas
git checkout simdugas/qa-buildbot-update-v2 -- prscript.py docker/buildbot.cfg

# Create the container with your patched image
python prscript.py -C -i suri-buildbot:beardnecks

# Start the container
python prscript.py -s

# Execute a build
python prscript.py -l -d master
```
