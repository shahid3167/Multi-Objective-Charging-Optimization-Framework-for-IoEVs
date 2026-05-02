# MOCF-IoEVs

This repository provides the dataset and implementation code for the Multi-Objective Charging Framework for Internet of Electric Vehicles (MOCF-IoEVs).

## Overview
The framework evaluates:
- Individual EV charging scenarios
- Aggregated community-level charging
- Communication performance between EV and EVSE

## IoT-Enabled Cyber-Physical Layer

<p align="center">
<img src="https://github.com/shahid3167/Multi-Objective-Charging-Optimization-Framework-for-IoEVs/blob/main/Results/CPS%20Layer.jpg" width="700" height="500">

<p align="center">
IoT-enabled cyber physical layer of the proposed MOCF-IoEV

## Features

- Multi-objective optimization for EV charging (cost and load balancing)
- Individual household-level charging analysis
- Aggregated community-level charging evaluation
- Communication model for EV–EVSE interaction and delay analysis

## Repository Structure

```
MOCF-IoEVs/
├── src/
│   └── mocf_ioev/
│       ├── __init__.py
│       ├── individual_charging.py
│       ├── aggregated_charging.py
│       ├── communication_model.py
│       └── main.py
├── notebooks/          # Jupyter notebooks for experiments and analysis
├── data/               # Dataset files (to be placed here)
├── results/            # Output results and plots
├── pyproject.toml      # Project configuration and dependencies
├── requirements.txt    # Python dependencies
├── .gitignore          # Files to ignore in version control
├── LICENSE             # License information
└── README.md           # Project documentation
```
## How to Run

To execute the full MOCF-IoEVs framework, open and run:

```python
src/mocf_ioev/main.py
```

This will automatically run:

- Individual charging scenario  
- Aggregated charging scenario  
- Communication model  

## Results

The proposed MOCF-IoEVs framework demonstrates improved performance in both individual and aggregated EV charging scenarios.

Key outcomes include:

- Reduction in peak load compared to baseline charging strategies  
- Lower charging cost through multi-objective optimization  
- Stable performance across different EV penetration levels  
- Communication delay within acceptable smart grid standards  

Detailed results and analysis are provided in the associated research paper.

## Example Output

When running the framework, the following output is displayed:

```
MOCF-IoEVs Framework Running...

Running individual charging scenario...
Running aggregated charging scenario...
Running communication model...
```

This confirms that all components of the framework are executed successfully.

## Data

The dataset required for this framework should be placed in the `data/` folder before running the code.

If the dataset is not included in this repository, please refer to the provided source or contact the author for access.

## Citation

If you use this work, please cite the following manuscript (currently under review):

S. Boubaker, S. Hussain, et al., "An IoT-Enabled Multi-Objective Charging Optimization Framework for IoEVs Based on the ISO-IEC 15118 Standard," 2026.

## Authors

**Sahbi Boubaker**  
Professor, 
Department of Computer and Network Engineering,  
College of Computer Science and Engineering,  
University of Jeddah, Saudi Arabia  
Email: sboubaker@uj.edu.sa  

**Shahid Hussain**  
Assistant Professor,  
Atlantic Technological University (ATU), Galway, Ireland  
Email: shahid.hussain@atu.ie  

For questions, feedback, or collaboration, feel free to contact the authors.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
