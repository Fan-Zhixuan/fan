import random
a=range(0,10)
b=random.sample(a,2)
b = sorted(b)
with open("val.txt","w") as f:
    for i in a:
        f.write('images/CT8#_image_'+str(i)+'.jpg labels/CT8#_image_'+str(i)+'.png\n')
f.close
# with open("train.txt","w") as f:
#     for i in a:
#         f.write('images/CT7_image_'+str(i)+'.jpg labels/CT7_image_'+str(i)+'.png\n')
# f.close