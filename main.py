from torchtext.data.utils import get_tokenizer
#参数介绍：'basic_english'代表分词方式
#分词方式还有：‘spacy’，‘moses’，‘toktok’，‘revtok’，'subword’
tokenizer=get_tokenizer('basic_english')
sen='i have a word!'
token=tokenizer(sen)
print(token)

