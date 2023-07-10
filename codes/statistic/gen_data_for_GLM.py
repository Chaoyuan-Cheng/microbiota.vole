import matplotlib.pyplot as plt
import matplotlib
import numpy as np
import scipy.stats as st
import pandas as pd
import os
matplotlib.rcParams.update({'font.size': 12})

#
work_space = r"E:\16SrRNA\1our_data\0布氏田鼠\pairwise_fdr"
f = pd.read_excel(r"C:\Users\40506\OneDrive\OneDrive_SYNC\发表论文\16S布氏田鼠\group.xlsx",sheet_name="group_trait")
out = open(r"E:\16SrRNA\1our_data\0布氏田鼠\GLM_data-ASV-fdr.csv","w")
out.writelines("group,genus1,genus2,spearman,PS,GD,diet,exp,CV_mean,shannon_mean,simpson_mean,chao1_mean,sample_size,contact,space\n")

#
groups = f["group"]
exps = f["exp"]
diets = f["diet"]
CVs = f["CV_mean"]
shannon = f["shannon_mean"]
simpson = f["simpson_mean"]
chao1 = f["chao1_mean"]
spaces = f["space"]
sample_size = f["sample_size"]
contacts = f["contact"]

#
group2trait = {}
for i in range(len(groups)):
    group2trait[groups[i]] = "%s,%s,%s,%s,%s,%s,%s,%s,%s"%(diets[i],exps[i],CVs[i],shannon[i],simpson[i],chao1[i],sample_size[i],contacts[i],spaces[i])

#
groups = list(f["group"])
for dataset in range(len(groups)):
    dataname = groups[dataset]
    print(dataname)
    data = pd.read_csv(r"%s\%s_pairwise.csv"%(work_space,dataname))
    id0 = data["ASV1"]
    id1 = data["ASV2"]
    x0 = data["spearman"]
    y0 = data["prop_similar"]
    gd = data["GD"]

    for j in range(len(x0)):
        out.writelines("%s,%s,%s,%s,%s,%s,%s\n"%(dataname,id0[j],id1[j],x0[j],y0[j],gd[j],group2trait[dataname]))
out.close()