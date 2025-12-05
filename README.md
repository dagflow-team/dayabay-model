# The model of the Daya Bay Reactor Neutrino experiment

[![python](https://img.shields.io/badge/python-3.11-purple.svg)](https://www.python.org/)
[![pipeline](https://git.jinr.ru/dagflow-team/dayabay-model-official/badges/main/pipeline.svg)](https://git.jinr.ru/dagflow-team/dayabay-model-official/commits/main)
[![coverage report](https://git.jinr.ru/dagflow-team/dayabay-model-official/badges/main/coverage.svg)](https://git.jinr.ru/dagflow-team/dayabay-model-official/-/commits/main)
[![github](https://img.shields.io/badge/github-public-blue?logo=github)](https://github.com/dagflow-team/dayabay-model)
[![gitlab](https://img.shields.io/badge/gitlab-dev-blue?logo=gitlab)](https://git.jinr.ru/dagflow-team/dayabay-model)
[![github-framework](https://img.shields.io/badge/github-framework-blue?logo=github)](https://github.com/dagflow-team/dag-modelling)
[![pypi-release](https://img.shields.io/badge/pypi-release-blue?logo=pypi&logoColor=green)](https://pypi.org/project/dayabay-model)
[![github-data](https://img.shields.io/badge/github-data-green?logo=github)](https://github.com/dayabay-experiment/dayabay-data-official)
[![pypi-data](https://img.shields.io/badge/pypi-data-green?logo=pypi&logoColor=green)](https://pypi.org/project/dayabay-data-official)
[![zenodo](https://img.shields.io/badge/zenodo-data-green?logo=zenodo&logoColor=green)](https://doi.org/10.5281/zenodo.17587229)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)


## Contents 

[TOC]

## Summary

The repository contains the model of the Daya Bay Reactor Neutrino experiment dedicated to work with Full Daya Bay dataset and perform neutrino oscillation analysis based on gadolinium capture data.

The Daya Bay Reactor Neutrino Experiment took data from 2011 to 2020 in China. It obtained a sample of 5.55 million IBD events with the final-state neutron captured on gadolinium (nGd). This sample was collected by eight identically designed antineutrino detectors (AD) observing antineutrino flux from six nuclear power plants located at baselines between 400 m and 2 km. It covers 3158 days of operation.

The model is able to read any format of the Daya Bay dataset and produce a measurement of sin²2θ₁₃ and Δm²₃₂, consistent with the publication.

## Repositories

- Code:
    * Main: development, CI: https://git.jinr.ru/dagflow-team/dayabay-model
    * Mirror: public access, issue tracker: https://github.com/dagflow-team/dayabay-model
    * PYPI: https://pypi.org/project/dayabay-model
- Data:
    * Full Data Release of the Daya Bay Reactor Neutrino Experiment: https://doi.org/10.5281/zenodo.17587229
    * Analysis dataset, PYPI: https://pypi.org/project/dayabay-model
    * Analysis dataset, GitHub: https://github.com/dayabay-experiment/dayabay-data-official

## Overview

### Data model

The released Daya Bay data is available in a variety of file formats (ROOT, hdf5, npz, tsv). All files follow the same conceptual schema and provide a set of key/value pairs. File names indicate the set of keys to expect and in some cases the context of the data (e.g. a particular sub-detector).  Values are arrays. For detailed description of the expected file and key names see: [https://github.com/dayabay-experiment/dayabay-data-official](https://github.com/dayabay-experiment/dayabay-data-official).

### Processing model

The user may process the data with their own software while Daya Bay also provides a reference processing framework and a set of processing components based on the dag-modelling package. This framework processes the data through a lazy evaluated directed acyclic data-flow programming graph with a set of functional nodes. 

### Analysis examples

The typical workflow considers installation of the Daya Bay model via PYPI and using it in the analysis from within python. While minimal working examples may be found in this repository more comprehensive cases of the fits and statistical analysis are provided in a dedicated [dayabay-analysis](https://github.com/dagflow-team/dayabay-analysis) repository.

## Working with the model

### Installation

#### Getting the code

##### From Python Package Index

The package may be installed with `pip` as follows:

```bash
pip install dayabay-model
```

The installation installs the `daybay-data-official` python module as a dependency, which provides the analysis version of the Full Daya Bay dataset.

##### From GitHub

To install the model from the GitHub, first, clone the repository.

```bash
git clone https://github.com/dagflow-team/dayabay-model
cd daybay-model
pip install -e .
```

Second, install the contents of the local module as python package, triggering also dependencies installation, including data. Note, that the argument `-e` uses symbolic links to the python files instead of copying, which makes all the modifications of the model immediately accessible.

#### Simple run

Assuming the environment variables are set, the model ca TODO

1. Run script
  ```bash
  ./extras/mwe/run.py
  ```
  or
  ```bash
  PYTHONPATH=PWD python extras/mwe/run.py
  ```
  Text of script is above
  ```python
  from dayabay_model_official import model_dayabay

  model = model_dayabay()
  print(model.storage["outputs.statistic.full.covmat.chi2cnp"].data)
  ```
  within `python`
  ```bash
  python extras/mwe/run.py
  ```
1. Check output in console, it might be something like below
  ```bash
  INFO: Model version: model_dayabay
  INFO: Source type: npz
  INFO: Data path: data
  INFO: Concatenation mode: detector_period
  INFO: Spectrum correction mode: exponential
  INFO: Spectrum correction location: before integration
  [705.12741983]
  ```
  It shows non-zero value of chi-squared function because by default it loads `real` data. About choosing `real`/`asimov` data read above.

### Minimal working examples

The minimal working examples are located in the folder `extras/mwe` folder. In order to run them clone this repository :
```bash
git clone https://github.com/dagflow-team/dayabay-model-official 
cd dayabay-model-official
````
However, you can just copy examples that are listed below and run them where you want after installation of package and several others steps:


#### Custom path to model data

Sometimes it is useful to load data model from specific directory. For this aim you may want to use `path_data` parameter of `model_dayabay`.

1. Also, you may pass custom path to data, if you put `path_data` parameter to model. For example,
  ```python
  from dayabay_model_official import model_dayabay

  model = model_dayabay(path_data="dayabay-data-official/npz")
  print(model.storage["outputs.statistic.full.pull.chi2cnp"].data)
  ```
  Example can be executed:
  ```bash
  python extras/mwe/run-custom-data-path.py
  ```
  or
  ```bash
  PYTHONPATH=PWD python extras/mwe/run-custom-data-path.py
  ```
2. Example can be executed:
  ```bash
  python extras/mwe/run-custom-data-path.py
  ```
  or
  ```bash
  PYTHONPATH=PWD python extras/mwe/run-custom-data-path.py
  ```
3. **Warning**: before running this example, make sure that you have put data in `dayabay-data-official/npz`. You can do it with `data/` from previous example. Run commands:
  ```bash
  mkdir dayabay-data-official/
  mv data/ dayabay-data-official/npz/
  ```

#### Switch between real and Asimov data

`real` data is loaded to model by default. However, it is possible to switch between `real` and `Asmov` datasets.

Short note:
- `real` means that will be loaded IBD candidates after selection;
- `asimov` means that data will be replaced with mean observation of model under assumption of mean parameters.

1. If you want to switch between Asimov and observed data, you need to switch input in the next way
  ```python
  from dayabay_model_official import model_dayabay

  model = model_dayabay(path_data="dayabay-data-official/npz")

  print("CNP chi-squared (default data):", model.storage["outputs.statistic.full.pull.chi2cnp"].data)

  model.switch_data("real")
  print("CNP chi-squared (real data):", model.storage["outputs.statistic.full.pull.chi2cnp"].data)

  model.switch_data("asimov")
  print("CNP chi-squared (asimov data):", model.storage["outputs.statistic.full.pull.chi2cnp"].data)
  ```
2. Example can be executed: 
  ```bash
  python extras/mwe/run-switch-asimov-real-data.py
  ```
  or
  ```bash
  PYTHONPATH=PWD python extras/mwe/run-switch-asimov-real-data.py
  ```
