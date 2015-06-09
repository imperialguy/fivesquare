from setuptools import setup, find_packages

requires = [
    'coverage==4.0a5',
    'Flask==0.10.1',
    'itsdangerous==0.24',
    'Jinja2==2.7.3',
    'MarkupSafe==0.23',
    'nose==1.3.4',
    'pep8==1.6.2',
    'Werkzeug==0.10.1',
    'unittest2==1.0.1',
    'WTForms==2.0.2',
    'pymongo==2.8',
    'mongoengine==0.9.0'
]

tests_require = requires

docs_extras = [
    'Sphinx',
    'docutils',
    'repoze.sphinx.autointerface']

setup(name='fivesquare',
      version='0.1',
      description='sample code for hinge',
      classifiers=[
          "Programming Language :: Python",
          "Framework :: Django",
          "Topic :: Internet :: WWW/HTTP",
          "Topic :: Internet :: WWW/HTTP :: WSGI :: Application", ],
      author='',
      author_email='vpkcareer2011@gmail.com',
      url='',
      keywords='web wsgi django flask',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      test_suite='nose.collector',
      install_requires=requires,
      tests_require=tests_require,
      extras_require={
          'docs': docs_extras, },
      entry_points="""\
      """,
      )
