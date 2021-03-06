#!/usr/bin/python
"""
Export neuroimaging results created with FSL feat following NIDM-Results 
specification. The path to feat directory must be passed as first argument.

@author: Camille Maumet <c.m.j.maumet@warwick.ac.uk>
@copyright: University of Warwick 2013-2014
"""

import sys
import os
from fsl_exporter.fsl_exporter import FSLtoNIDMExporter

if __name__ == "__main__":
    # Remove first argument (script name)
    num_args = len(sys.argv)-1
    sys.argv.pop(0)
    args = sys.argv

    usage = "Usage: python nidm-results_fsl.py path/to/feat/dir"

    if num_args != 1:
        raise Exception(usage)

    feat_dir = args[0]
    if not os.path.isdir(feat_dir):
        raise Exception("Unknown directory: "+str(feat_dir))

    fslnidm = FSLtoNIDMExporter(feat_dir=feat_dir, version="0.2.0")
    fslnidm.parse()
    export_dir = fslnidm.export()

    print 'NIDM export available at: '+str(export_dir)
