#!/bin/bash
MESSAGE="Auto-commit: $(date)"
REPO_PATH="/Users/jnaiman/is445_bcubcg_fall2024"
cd $REPO_PATH
/usr/bin/git add -A
/usr/bin/git commit -m "$MESSAGE"
/usr/bin/git push
