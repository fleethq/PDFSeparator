
import os
from shutil import copyfile

COUNTS = {
	'Single': 0,
	'First': 0,
	'Last': 0,
	'Middle': 0
}
def load_directory():
	return os.listdir(os.path.join(os.getcwd(), 'input'))

def iterate_and_rename(ls):
	validCount = 0
	for filename in ls:
		if (filename.lower().find('single') != -1):
			# move file		
			os.rename(os.path.join(os.getcwd(), 'input', filename), os.path.join(os.getcwd(), 'input', 'Single{:09d}.jpg'.format(COUNTS['Single'])))
			COUNTS['Single'] += 1
		elif (filename.lower().find('first') != -1):
			os.rename(os.path.join(os.getcwd(), 'input', filename), os.path.join(os.getcwd(), 'input', 'First{:09d}.jpg'.format(COUNTS['First'])))
			COUNTS['First'] += 1
		elif (filename.lower().find('last') != -1):
			os.rename(os.path.join(os.getcwd(), 'input', filename), os.path.join(os.getcwd(), 'input', 'Last{:09d}.jpg'.format(COUNTS['Last'])))
			COUNTS['Last'] += 1
		elif (filename.lower().find('middle') != -1):
			os.rename(os.path.join(os.getcwd(), 'input', filename), os.path.join(os.getcwd(), 'input', 'Middle{:09d}.jpg'.format(COUNTS['Middle'])))
			COUNTS['Middle'] += 1
		else:
			validCount += 1
			print ("Validation Error. Invalid Label Category", filename)
	if (validCount > 1):
		raise ValueError("It appears that more than 1 document is mislabeled. Only 1 should be (Transaction Page)")


if __name__=="__main__":
	ls = load_directory()
	iterate_and_rename(ls)