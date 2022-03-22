from setuptools import setup
import versioneer

setup(
    name="morphocluster",
    packages=["morphocluster"],
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    include_package_data=True,
    install_requires=[
        "flask>=1.0.2",
        "psycopg2-binary",
        "pandas",
        "sqlalchemy",
        "etaprogress",
        "h5py>=2.8.0",
        "scikit-learn",
        "scipy",
        "redis >= 3.0, < 3.1",
        "hiredis",
        "flask-restful",
        "alembic",
        "Flask-SQLAlchemy",
        "flask-redis",
        "Flask-Migrate",
        "timer_cm",
        "fire",
        "marshmallow>=3.0.0b20",
        "match_arrays",
        "Flask-RQ2",
        "tqdm",
        "Click",
        "chardet",
        "environs", # For envvar parsing
    ],
    setup_requires=["pytest-runner"],
    tests_require=["pytest"],
    entry_points={"console_scripts": ["morphocluster = morphocluster.scripts:main"]},
)
