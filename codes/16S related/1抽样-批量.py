import random
import os
from Bio import SeqIO

folders = r"D:\仓库\rodent"
out_dirs = r"E:\temp\mammal.resampled"

# 最低长度限制
minlen = 200
maxlen = 1000

size = 50000
for n in os.listdir(folders):
    folder = "%s\%s"%(folders,n)
    out_dir = "%s\%s"%(out_dirs,n)
    if not os.path.exists(out_dir):
        os.mkdir(out_dir)
    ind0 = 0
    for i in os.listdir(folder):
        print(ind0, i)
        if os.path.exists(r"%s\%s_resampled.fa" % (out_dir, i.replace(".fastq", ""))):   # 注意后缀
            print("---already exist---")
        else:
            seq_list = []
            id_list = []
            seqs = SeqIO.parse(r"%s\%s"%(folder,i),"fastq")

            try:    # 有的文件不完整
                for j in seqs:
                    seq = j.seq

                    if maxlen > len(seq) > minlen:
                        seq_list = seq_list + [seq]
                        id_list = id_list + [j.description]
                    else:
                        print("too short")
            except:
                print("warning")

            if len(seq_list) > 50000:
                used = random.sample(range(len(seq_list)),size)
            else:
                used = range(len(seq_list))
            out = open(r"%s\%s_resampled.fa"%(out_dir,i.replace(".fastq","")), "w")     # 注意后缀名称
            for j in used:
                out.writelines(">%s\n%s\n"%(id_list[j],seq_list[j]))
            out.close()

            print(n,i,"--ok--")
            ind0 += 1