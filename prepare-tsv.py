import csv
import os
import re

values = {
	
}
def load_directory():
	return os.listdir(os.path.join(os.getcwd(), 'input'))

def get_label(name):
	output = re.sub(r'\d+', '', name)
	return output.replace('.jpg', '')

def prepare_tsv(ls):
	for filename in ls:
		label = get_label(filename)
		if (label == "_Transaction"):
			continue
		values['input\\' + filename] = label

def print_output():
	with open('labeled-images.tsv', 'w', newline='') as out:
		writer = csv.writer(out, delimiter='\t')
		for key, val in values.items():
			writer.writerow([key, val])

if __name__ == "__main__":
	ls = load_directory()
	prepare_tsv(ls)

	print_output()