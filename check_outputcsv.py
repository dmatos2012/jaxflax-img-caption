import pandas as pd
# df = pd.read_csv("wit_dataset/wit_v1.train.all-00000-of-00010.tsv", sep='\t', usecols=[0,1,2,6])
# # print(df.language.unique())
# gk = df.groupby('language')
# # print(gk
# gk = gk.get_group('es')
# print(gk.head)
names = ["file", "folder", "image_url", "lang", "mimetype", "ref_dsc", "size", "status"]
# dtype={'file':'string'} # to avoid confusion
df = pd.read_csv("downloaded_training_report.csv.gz", compression='gzip')
print(df.sample(4))
# print(df['language'])
# print(df['language'])

# print(df.head)



