"""
min-max normalization
"""
import numpy as np
import pandas as pd

f = pd.read_csv(r"E:\16SrRNA\1our_data\0布氏田鼠\GLM_data-ASV.csv")
out = open(r"E:\16SrRNA\1our_data\0布氏田鼠\GLM_data-ASV.标准化2.csv","w")
out.writelines("group,genus1,genus2,spearman,PS,GD,diet,CV_mean,shannon_mean,simpson_mean,chao1_mean,sample_size,space,contact\n")

#
gp = f["group"]
ASV0 = f["genus1"]
ASV1 = f["genus2"]
sp = f["spearman"]
ps = f["PS"]
gd = f["GD"]
dt = f["diet"]
cv = f["CV_mean"]
shannon = f["shannon_mean"]
simpson = f["simpson_mean"]
chao = f["chao1_mean"]
sample = f["sample_size"]
space = f["space"]
contact = f["contact"]


#
sp_min = np.min(sp)
ps_min = np.min(ps)
gd_min = np.min(gd)
cv_min = np.min(cv)
shannon_min = np.min(shannon)
simpson_min = np.min(shannon)
chao_min = np.min(chao)
sample_min = np.min(sample)
space_min = np.min(space)

sp_max = np.max(sp)
ps_max = np.max(ps)
gd_max = np.max(gd)
cv_max = np.max(cv)
shannon_max = np.max(shannon)
simpson_max = np.max(shannon)
chao_max = np.max(chao)
sample_max = np.max(sample)
space_max = np.max(space)

# ct = []
# print(len(contact))
# for i in contact:
#     if i == 1:
#         ct = ct + ["no"]
#     else:
#         ct = ct + ["yes"]
#     print(i)

#
ind = 0
for i in range(len(gp)):
    ind += 1
    if contact[i] == 1:
        ct = "no"
    else:
        ct = "yes"
    if (sp[i]-sp_min)/(sp_max-sp_min) >= 0:
        out.writelines("%s,%s,%s,%.4f,%.4f,%.4f,%s,%.4f,%.4f,%.4f,%.4f,%.4f,%.4f,%s\n"%(gp[i],ASV0[i],ASV1[i],(sp[i]-sp_min)/(sp_max-sp_min),(ps[i]-ps_min)/(ps_max-ps_min),(gd[i]-gd_min)/(gd_max-gd_min),dt[i],(cv[i]-cv_min)/(cv_max-cv_min),(shannon[i]-shannon_min)/(shannon_max-shannon_min),(simpson[i]-simpson_min)/(simpson_max-simpson_min),(chao[i]-chao_min)/(chao_max-chao_min),(sample[i]-sample_min)/(sample_max-sample_min),(space[i]-space_min)/(space_max-space_min),ct))

    print(ind,(sp[i]-sp_min)/(sp_max-sp_min))
out.close()