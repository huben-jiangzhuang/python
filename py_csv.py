import csv
fp = open('d://test.csv','w+')
writer = csv.writer(fp)
writer.writerow(('id','name'))
writer.writerow(('1','a'))
writer.writerow(('2','b'))
writer.writerow(('3','c'))