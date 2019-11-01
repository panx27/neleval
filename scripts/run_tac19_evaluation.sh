#!/usr/bin/env bash
set -e

usage="Usage: $0 GOLD SYSTEMS_DIR OUT_DIR NUM_JOBS TYPE_HIERARCHY [-x EXCLUDED_SPANS]"

if [ "$#" -lt 5 ]; then
    echo $usage
    exit 1
fi

gtab=$1; shift # gold standard link annotations (tab-separated)
sysdir=$1; shift # directory containing output from systems
outdir=$1; shift # directory to which results are written
jobs=$1; shift # number of jobs for parallel mode
hierarchy=$1; shift # type hierarchy JSON file

SCR=`dirname $0`

# CONVERT TYPE HIERARCHY TO TYPE WEIGHTS
echo "INFO Converting type hierarchy to type weights.."
weights=$outdir/type_weights.tsv
./nel weights-for-hierarchy $hierarchy > $weights

# CONVERT GOLD TO EVALUATION FORMAT
echo "INFO Converting gold to evaluation format.."
# XXX: "combined" is a misnomer in tac15. Should be neleval? But existing scripts depend on this extension.
gold=$outdir/gold.combined.tsv
options=$@
./nel prepare-tac15 $gtab $options > $gold

# convert systems to evaluation format
echo "INFO converting systems to evaluation format.."
ls $sysdir/* \
	| xargs -I{} -n 1 -P $jobs bash -c "f={}; ./nel prepare-tac15 \$f $options > $outdir/\$(basename \$f).combined.tsv"



# EVALUATE
echo "INFO Evaluating systems.."
ls $outdir/*.combined.tsv \
    | grep -v "gold\.combined\.tsv$" \
    | xargs -n 1 -P $jobs $SCR/run_evaluate_weights.sh $gold $weights

# PREPARE SUMMARY REPORT
echo "INFO Preparing summary report.."
$SCR/run_tac19_report.sh $outdir
