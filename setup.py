import setuptools

# with open("README.md", "r") as fh:
#     long_description = fh.read()

setuptools.setup(name='IntelliMaint',
		version='0.0.1',
		author='IPTLP0032',
		author_email="iptgithub@intellipredikt.com",
		description="A prognostics package by IPT",
		install_requires=['sklearn', 'GPy', 'minisom', 'scipy', 'matplotlib', 'numpy>=1.16.1', 'mplcursors'],
		packages=setuptools.find_packages(),
		include_package_data=True,
		package_data={
		'IntelliMaint.examples.data.battery_data':['*'],
		'IntelliMaint.examples.data.bearing_data': ['*'],
		'IntelliMaint.examples.data.phm08_data.csv':['*']
		},
		# dependency_links=[
  #     'git+ssh://git@github.com/caisr-hh/group-anomaly-detection.git#egg=grand-0.2.0',
  # ],
		python_requires='>=3.5',
	)
