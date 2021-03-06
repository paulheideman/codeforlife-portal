#!/bin/bash
# find out where we are
DEPLOY_PATH=`pwd`
cd ..
PROJECT_PATH=`pwd`
cd ${DEPLOY_PATH}

# create virtual env
rm -rf VIRTUALENV
virtualenv VIRTUALENV
source VIRTUALENV/bin/activate

pip install -r requirements.txt

pip install -r ../ocargo/requirements.txt
pip install -r ../portal/requirements.txt

# now change to symlinks,
# this means that local changes affect the running server immediately
# without the need to install requirements again or restart the server
rm -rf VIRTUALENV/lib/python2.7/site-packages/{game,portal}
ln -sv ${PROJECT_PATH}/ocargo/game VIRTUALENV/lib/python2.7/site-packages/game
ln -sv ${PROJECT_PATH}/portal/portal VIRTUALENV/lib/python2.7/site-packages/portal
ln -sv ${PROJECT_PATH}/portal/reports VIRTUALENV/lib/python2.7/site-packages/reports
ln -sv ${PROJECT_PATH}/portal/ratelimit VIRTUALENV/lib/python2.7/site-packages/ratelimit
