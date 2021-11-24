#with open('human_text.txt', errors='ignore') as file:
 #   human_lines = file.readlines()

#print(human_lines[0])

#with open('robot_text.txt', errors='ignore') as file:
 #   robot_lines = file.readlines()

#print(robot_lines[0])
import re
import random
data_path = "human_text.txt"
data_path2 = "robot_text.txt"


with open(data_path, 'r', encoding='utf-8') as f:
  lines = f.read().split('\n')
with open(data_path2, 'r', encoding='utf-8') as f:
  lines2 = f.read().split('\n')
lines = [re.sub(r"\[\w+\]",'hi',line) for line in lines]
lines = [" ".join(re.findall(r"\w+",line)) for line in lines]
lines2 = [re.sub(r"\[\w+\]",'',line) for line in lines2]
lines2 = [" ".join(re.findall(r"\w+",line)) for line in lines2]

# grouping lines by response pair
pairs = list(zip(lines,lines2))

print(len(pairs))