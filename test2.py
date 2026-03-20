import jieba
import jieba.posseg as pseg
words = pseg.cut("现在她的位置应该在屠宰场门外很远处的一辆指挥车上") #jieba默认模式
for word, flag in words:
    print('%s %s' % (word, flag))