from diagrams import Diagram, Cluster
from diagrams.aws.compute import EC2
from diagrams.aws.database import RDS
from diagrams.aws.network import ELB
import os

os.environ["PATH"] += os.pathsep + 'here put Graphiv path in your computer'

with Diagram("Direction PLF",show=False,direction='TB') as diag:
    ELB_obj=EC2('Chef dep.Plan')
    Directeur=ELB('Directeur PLF')
    RDS_obj=EC2('Chef dep.Report')
    with Cluster('Les ingénieurs de la direction'):
        engineer1=EC2('Ing 1')
        engineer2=EC2('Ing 2')
        engineer3=EC2('Ing 3')
        engineer4=EC2('Ing 4')
        Ing_group=[(engineer1,engineer2,engineer3,engineer4)]

    
    Directeur>>[RDS_obj,ELB_obj]
    RDS_obj>>[engineer1,engineer2]
    ELB_obj>>[engineer3,engineer4]

diag
