#!/bin/sh

export CFXDB_VERSION=$(grep -E '^(__version__)' ./cfxdb/_version.py | cut -d ' ' -f3 | sed -e 's|[u"'\'']||g')
export CFXDB_VCS_REF=`git --git-dir="./.git" rev-list -n 1 v${CFXDB_VERSION} --abbrev-commit`
export BUILD_DATE=`date -u +"%Y-%m-%d"`

echo ""
echo "Build environment configured:"
echo ""
echo "  CFXDB_VERSION = ${CFXDB_VERSION}"
echo "  CFXDB_VCS_REF = ${CFXDB_VCS_REF}"
echo "  BUILD_DATE    = ${BUILD_DATE}"
echo ""
