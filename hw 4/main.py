from adults import Adults
from kids import Kids

William_Afton = Adults(name='William', surname='Afton', age=46, status='alive')
Clara_Afton = Adults(name='Clara', surname='Afton', age=31, status='dead')
Michael_Afton = Kids(name='Michael', surname='Afton', age=18, status='alive')
Elizabeth_Afton = Kids(name='Elizabeth', surname='Afton', age=11, status='dead')
print(William_Afton)
print(Clara_Afton)
print(Michael_Afton)
print(Elizabeth_Afton)