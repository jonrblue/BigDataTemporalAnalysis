# BigDataTemporalAnalysis

This project contains various python scripts to run our temporal detection program and other data/resources esstienal to the program.

basic_profiling.py: This is the script running basic datamart profiler. Due to unidentified installation failure of datamart_profiler on hpc, after discussion with professor, we move the process involving datamart onto our local mainchine. Unfortunately it means we need to have the dataset on our local machine as well. Thus, we need to install datamart_profiler on our local machine first(pip install). Then we could run the scripts directly in bash or any shell: python3 basic_profiling.py path_to_dataset. The output for all 100 datasets are stored in basic_profiling_out.


enhanced_profiling.py: This is the script of running improved version of datamart profiler. We could still run the scripts directly in bash or any shell: python3 enhanced_profiling.py path_to_dataset. It generates similiar output format like basic_profiling.py.

converter.py:
downloader.py

main.py:

main_plots.py:

main_re.py
