#!/usr/bin/env bash

# First argument is the number of ensemble runs
# Second argument is the first three digits of the decade to be concatenated e.g. for 2150s put 215
# Third argument is the case name with xxx  in place of the ensemble number e.g. fbnc_f45_cstarv_xxx.Ea7f4ecb9dd-Ff76232e0.2023-12-21


export nruns=$1
export decade=$2
export simname=$3

set -eu 

for i in $(seq 1 ${nruns} ) ;
do
    (
     cur="${simname/xxx/${i}}"
     echo $cur
     cd "${cur}/run"
     ncrcat -h ${cur}.elm.h0.${decade}*.nc "${cur}.${decade}0s.nc" || echo skip
    )
done
