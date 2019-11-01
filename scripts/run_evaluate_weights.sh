#!/usr/bin/env bash
#
# Evaluate and save to file
set -e

usage="Usage: $0 GOLD SYSTEM WEIGHTS"

if [ "$#" -ne 3 ]; then
    echo $usage
    exit 1
fi

gold=$1; shift # prepared gold standard annotations (.combined.tsv)
weights=$1; shift # prepared type weights (.tsv)
sys=$1; shift # prepared system annotations (.combined.tsv)

out=`echo $sys | sed 's/.combined.tsv/.evaluation/'`
./nel evaluate \
      -m 'strong_typed_mention_match' \
      -f 'tab' \
      -g $gold \
      --type-weights $weights \
      $sys \
      > $out
