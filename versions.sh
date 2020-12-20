#!/bin/sh

export BUILD_DATE=`date -u +"%Y-%m-%d"`
# export CFXDB_VCS_REF=`git --git-dir="./.git" rev-list -n 1 v${CFXDB_VERSION} --abbrev-commit`
export CFXDB_VCS_REF=`git rev-parse --short HEAD`
export CFXDB_BUILD_ID=$(date --utc +%Y%m%d)-$(git rev-parse --short HEAD)
export CFXDB_VERSION=$(grep -E '^(__version__)' ./cfxdb/_version.py | cut -d ' ' -f3 | sed -e 's|[u"'\'']||g')


echo ""
echo "Build environment configured:"
echo ""
echo "  BUILD_DATE     = ${BUILD_DATE}"
echo "  CFXDB_VCS_REF  = ${CFXDB_VCS_REF}"
echo "  CFXDB_BUILD_ID = ${CFXDB_BUILD_ID}"
echo "  CFXDB_VERSION  = ${CFXDB_VERSION}"
echo ""
