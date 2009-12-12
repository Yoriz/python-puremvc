from distutils.core import setup, Command

class test(Command):
    """
    Run all available tests.
    """
    user_options = []
    initialize_options = lambda s:None
    finalize_options = lambda s:None
    def run(self):
        import sys
        import os
        CWD = os.getcwd()
        PUREMVC = os.path.join(CWD, "src")
        TEST = os.path.join(CWD, "unittest")
        sys.path[0:0] = (PUREMVC, TEST)
        import main
        main.runAllTests()


setup(name='PureMVC Python',
      version='1.1',
      description='PureMVC Python Framework',
      author='Toby de Havilland',
      author_email='toby.de.havilland@puremvc.org',
      url='http://www.puremvc.org',
	  package_dir={'': 'src'},
      packages=['puremvc', 'puremvc.patterns'],
      cmdclass = {
          "test": test,
        }
     )
