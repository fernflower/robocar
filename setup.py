from setuptools import setup


setup(name='robocar',
      version='0.1',
      install_requires=[
          "bottle",
          "paho-mqtt"
      ],
      packages=['robocar',
                'robocar.host'],
      include_package_data=True,
      )
