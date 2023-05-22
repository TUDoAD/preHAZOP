# Automated HAZOP analysis & risk analysis
The concept of this automated HAZOP analysis & risk analysis tool is based on preHAZOP (see preHAZOP [^1]). 

Optimization points of automated preHAZOP:

- Based on pressure zones
- Analysis with a relational SQL database
- Process medium is considered

<p align="center">

  <img src="https://github.com/TUDoAD/Abschlussarbeiten_Oeing/blob/main/Yang/pictures/Automated%20HAZOP%20analysis.png">

</p>

$${\color{blue}Figure \space 1: Automated \space HAZOP \space Analysis \space Flow \space Sheet}$$

## Authors:
![TU-Do](https://github.com/TUDoAD/preHAZOP/blob/main/figures/TUDO_AD_logo.png)

Ruolan Yang, Jonas Oeing

TU Dortmund University, [Laboratory of Equipment Design](https://ad.bci.tu-dortmund.de/cms/en/laboratory/)

***
## Install:

- Install Python (anaconda) from https://www.anaconda.com/products/individual (Python 3.9.15)

- Install MySQL from https://dev.mysql.com/downloads/, for windows [^2]: 
    1. select *MySQL Installer for Windows*.
    2. select first *Windows (x86, 32-bit), MSI Installer 2.4M* to *Download*. 
    3. select *No thanks, just start my download*.
    4. select Setup Type: *Custom*.
    5. select Products: MySQL Server; MySQL Workbench; MySQL Shell (select the latest version).
    6. Next -> Excute -> Next
    7. Accont and Roles: select your password.
    8. Next -> Finish
    9. Go to MySQL Workbench, Connect to MySQL Server, you need to enter your password.
    10. You can now work with the SQL database :)

- Load the following python libraries:
  - NetworkX (vers. 2.8.8) [^3]
  - Matplotlib (vers. 3.6.2) [^4]
  - mysql.connector (vers. 8.0.31) [^5]
  - Other libraries are included with Python

***

### *Pressure Zone detection*

The code of the automated pressure zone detection (python application) can be found there:  https://github.com/TUDoAD/preHAZOP/blob/main/preHAZOP_ExtensionPack/Pressure%20Zone%20Detection/Code_PressureZoneDetection.py

***

### *SQL Databases Extension Pack* 

The SQL Databases for preHAZOP scenarios and substance data can be accessed using the following link: https://github.com/TUDoAD/preHAZOP/tree/main/preHAZOP_ExtensionPack/Databases/SQLs

***
References:

[^1]: Oeing, J; Holtermann, T. Welscher, W.; Severins, C.; Vogel, M.; Kockmann, N., preHAZOP: Graph-based Safety Analysis for Early Integration into Automated Engineering Workflows, https://doi.org/10.1002/cite.202200222 , accessed on 22.05.2023

[^2]: MySQL Guide, online documentation, https://www.youtube.com/watch?v=gvRXjsrpCHw, accessed on 22.04.2023

[^3]: NetworkX, online documentation, https://networkx.org/, accessed on 22.04.2023

[^4]: matplotlib, https://matplotlib.org/, accessed on 22.04.2023

[^5]: MySQL Connectors, https://www.mysql.com/products/connector/, accessed on 22.04.2023