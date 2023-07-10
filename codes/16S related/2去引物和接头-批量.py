"""
去引物和接头
去除过短序列
注意修改序列长度阈值
"""

import os
import pandas as pd

#len_f = pd.read_excel(r"E:\16SrRNA\2wild_species\len_summary.xlsx",sheet_name="标准")

folders = r"E:\BACK_UP_RT\2课题-part2\16S.mammal.2022\seqs\all"

out_dirs = r"E:\BACK_UP_RT\2课题-part2\16S.mammal.2022\seqs\all_去接头"

cmd = r"E:\biosoftware\vsearch-2.21.1-win-x86_64\bin\vsearch"

start = 10
end = 10
# #
# studys = len_f["study"]
# minis = len_f["最短"]
#
# #
# study2len = {}
# for i in range(len(studys)):
#     study2len[studys[i]] = int(minis[i])

#
for j in os.listdir(folders):
    folder = "%s\%s"%(folders,j)
    out_dir = "%s\%s"%(out_dirs,j)
    os.mkdir(out_dir)
    #mini = study2len[j]
    mini = 200

    for i in os.listdir(folder):
        print(i)
        #os.system(r"%s --fastx_filter %s\%s --fastq_stripleft %s --fastq_stripright %s --fastq_maxee_rate 0.01 --fastaout %s/%s.fa --fastq_minlen 200"%(cmd,folder,i,start,end,out_dir,i.replace("fastq","")))
        ## 改名字
       # os.system(r"%s --fastx_filter %s\%s --fastq_stripleft %s --fastq_stripright %s --fastq_maxee_rate 0.01 --fastaout %s/%s.fa --fastq_minlen 200 --relabel Liu_MR_%s."%(cmd,folder,i,start,end,out_dir,i.replace(".fastq",""),i.replace(".fastq","")))
        # 不改名字
        os.system(r"%s --fastx_filter %s\%s --fastq_stripleft %s --fastq_stripright %s --fastaout %s/%s --fastq_minlen %s"%(cmd,folder,i,start,end,out_dir,i.replace(".fastq",""),mini))
        print(j,i)