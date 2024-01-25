#!/usr/bin/env python

# Written by C. Koven, 2018
# Adapted by J. Needham 2021
            
        
import os
from scipy.io import netcdf as nc
import shutil
import tempfile
import numpy as np
            
            
def main(var, pft, fin, val, fout, O, organ):
            
    # work with the file in some random temporary place so that if something goes wrong, then nothing happens to original file and it doesn't make a persistent output file
    tempdir = tempfile.mkdtemp()
    tempfilename = os.path.join(tempdir, 'temp_fates_param_file.nc')
    ncfile_old = None
    outputfname = fout
       
    outputval = float(val)
    pft = int(pft)
   
    shutil.copyfile(fin, tempfilename)
    ncfile = nc.netcdf_file(tempfilename, 'a')                  
    var = ncfile.variables[var]
    

       
    if pft == 0 : 
        var.assignValue(outputval)
    else : 
        ndim = len(var.dimensions)
        if ndim == 1:
            var[pft-1] = outputval
        else : 
            if var.dimensions[0] == 'fates_leafage_class' :
                var[:,pft-1] = outputval
            else : 
                organ = int(organ)
                var[organ-1,pft-1] = outputval

    ncfile.close()
    if type(ncfile_old) != type(None):
        ncfile_old.close()
        #
        #
        # now move file from temporary location to final location
    if O == 1:   
        os.remove(outputfname)
    shutil.move(tempfilename, outputfname)
    shutil.rmtree(tempdir, ignore_errors=True)
            
   # =======================================================================================
   # This is the actual call to main
               
if __name__ == "__main__":
    main()
