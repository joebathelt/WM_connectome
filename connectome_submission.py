import os
from subprocess import call

in_folder = '/imaging/jb07/CALM/CALM_BIDS/'
out_folder = '/imaging/jb07/CALM/Modularity/scripts/'
filename = lambda subject: '/imaging/jb07/CALM/Modularity/connectome/_subject_id_' + subject + '/_model_CSD/_threshold_10/calc_matrix/mapflow/_calc_matrix0/' + subject + '_FA_matrix.txt'
in_file = lambda subject: in_folder + subject + '/dwi/' + subject + '_dwi.nii.gz'
subject_list = sorted([subject for subject in os.listdir(in_folder) if not os.path.isfile(filename(subject))])
subject_list = ['CBU150256', 'CBU150650', 'CBU150651', 'CBU160072', 'CBU160883', 'CBU170028', 'CBU170512', 'CBU170521', 'CBU170571', 'CBU170599', 'CBU170679', 'CBU170686', 'CBU170693', 'CBU170702', 'CBU170731']

for subject in subject_list:
	if os.path.isfile(in_file(subject)):
		file = open(out_folder + subject + '_connectome.sh', 'w')
		cmd = "python /home/jb07/joe_python/GitHub/Modularity/connectome_pipeline.py " + \
		"--base_directory '/imaging/jb07/CALM/CALM_BIDS/' " + \
		"--subject_list " + subject + ' ' + \
		"--template_directory '/home/jb07/joe_python/GitHub/Modularity/NKI/' " + \
		"--out_directory '/imaging/jb07/CALM/Modularity/' " + \
		"--parcellation_directory '/home/jb07/joe_python/GitHub/Modularity/FreeSurfer_templates/' " + \
		"--acquisition_parameters '/imaging/jb07/CALM/CALM_BIDS/acqparams.txt' " + \
		"--index_file '/imaging/jb07/CALM/CALM_BIDS/index.txt' "
		file.write(cmd)
		file.close()

		cmd = 'qsub ' + out_folder + subject + '_connectome.sh -l walltime=48:00:00'
		call(cmd, shell=True)
