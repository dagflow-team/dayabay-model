#!/usr/bin/env python

from dayabay_data_official import get_path_data

from dayabay_model import model_dayabay

model = model_dayabay()
print("χ² CNP (default data):", model.storage["outputs.statistic.full.pull.chi2cnp"].data)

for source_type in ["hdf5", "root", "npz", "tsv"]:
    model = model_dayabay(path_data=get_path_data(source_type))
    print(
        f"χ² CNP ({source_type} data):", model.storage["outputs.statistic.full.pull.chi2cnp"].data
    )
