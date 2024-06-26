from setuptools import setup, Extension
import sys

if sys.version.startswith("2"):
    print >>sys.stderr, "arm_now is only for python3"
    sys.exit(1)

setup(name='arm_now',
        version='1.27',
        author='@chaignc',
        url='https://github.com/antifob/arm_now',
        packages=['arm_now'],
        py_modules=['arm_now'],
        entry_points = {
            'console_scripts': [
                'arm_now = arm_now:main',
                ],
            },
        install_requires=[
            'exall',
            'requests',
            'docopt',
            'pySmartDL',
            'python-magic',
            'distro'
            ],
        keywords = ['emulator', 'arm', 'mips', 'powerpc', 'x86', 'qemu']
        )
