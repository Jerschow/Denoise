import h5py
import numpy as np
import os


def overwrite(write_file_name):
	os.system('rm ' + write_file_name)
	os.system('touch ' + write_file_name)


def store(write_file_name, read_file, data_name, data):
	overwrite(write_file_name)
	write_file = h5py.File(write_file_name, 'w')
	for key in read_file:
		if key == data_name:
			#making an nd array with same dimensions as the one in read_file[data]
			write_file.create_dataset(data_name, data = data)
		else:
			write_file.create_dataset(key, read_file[key])
	
	write_file.close()


WRITE_FILE_NAME = "denoised_raw.h5"
READ_FILE_NAME = 'raw.h5'
IMAGES_KEY_NAME = 'raw'


raw_file = h5py.File(READ_FILE_NAME, 'r')
#data stored in dataset raw just needs to be the same shape as in the read file
#so I made an array with the same shape with all entries 0
store(WRITE_FILE_NAME, raw_file, IMAGES_KEY_NAME, np.zeros(raw_file['raw'].shape))

raw_file.close()