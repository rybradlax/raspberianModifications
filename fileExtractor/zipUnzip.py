import zipfile
print("Starting up the application for you...")
input1 = input("Name the file you wish to be extracted or zipped")
input2 = input("Do you want this file to be zipped or unzipped, z or uz")
if input2 == "uz":
	input3 = input("Name the directory you want the file to be extracted to")
	with zipfile.ZipFile(input1,"r") as zip_ref:
		zip_ref.extractall(input3)
else:
	print("TypeError: Incorrect input, type z for zip, or uz for unzip")
if input2 == "z":
	input4 = input("Insert a zipped file directory here")
	with ZipFile(input4, 'w') as myzip:
		myzip.write(input1)