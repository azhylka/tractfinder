setup(
    name='tractfinder',
    version='0.1.0',
    description='Tractfinder: fibre tract segmentation with tumour deformation modelling',
    author='Fiona Young',
    package_dir={'': 'lib'},
    packages=find_packages(where='lib'),
    include_package_data=True,
    scripts=[
        'bin/tractfinder',
        'bin/mrtrix3.py',
        'bin/make_tractfinder_atlas'
    ],
    install_requires=[
        'numpy',
        'scipy',
        'scikit-image',
        'pyvista'
    ],
    python_requires='>=3.8',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)',
        'Operating System :: OS Independent'
    ],
)