# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 10:47:07 2019

@author: Karthik.V
"""

__author__ = 'Karthik'
 
import unittest
import os
import HTMLTestRunner
import sys
import MasterProjectUtils



 
direct = os.getcwd()
appName = ''


def getApplicationName():
    ApplicationName = sys.argv[1]
    return ApplicationName

def load_modules_from_path(path):
       """
       Import all modules from the given directory
       """
       # Check and fix the path
       if path[-1:] != '/':
           path += '/'
    
       # Get a list of files in the directory, if the directory exists
       if not os.path.exists(path):
            raise OSError("Directory does not exist: %s" % path)
    
       # Add path to the system path
       sys.path.append(path)
       mylist = []
       # Load all the files in path
       for f in os.listdir(path):
           # Ignore anything that isn't a .py file
           if len(f) > 3 and f[-3:] == '.py':
               modname = f[:-3]
               # Import the module
               #print (modname)
               mylist.append(modname)
               __import__(modname, globals(), locals(), ['*'])
       return mylist
 
    

def my_import(name):
    components = name.split('.')
    mod = __import__(components[0])
    for comp in components[1:]:
        mod = getattr(mod, comp)
    return mod

#print(getApplicationName())
appDir = '../'+getApplicationName() 
#appDir = '../EM1' 
htmlDir = '/Reports/'+getApplicationName()+'.html'
#htmlDir = '/Reports/EM1.html'
#print(appDir)
    
class MyTestSuite(unittest.TestCase):
    
    
    
    
    def getClasses():
        dirpath = os.path.abspath(appDir)
        mylist1 = load_modules_from_path(dirpath)
        return mylist1
    
    def test_Issue():
        selenium_test = unittest.TestSuite()
        list1 = MyTestSuite.getClasses()
        print('Below are the classes that got loaded')
        for i in list1: 
            print(i)
        #print(os.path.abspath('../driver/chromedriver.exe'))
        #print(list1[0])
        #print(my_import(list1[0]+'.'+list1[0]))
        #print(MasterProjectUtils.readFromExcel('EM1','Sheet1',1,0))
        #print(MasterProjectUtils.getTotalNumRows('EM1','Sheet1'))
        count = 1
        while (count<MasterProjectUtils.getTotalNumRows(getApplicationName(),'Sheet1')):
            #print(count)
            #print(MasterProjectUtils.readFromExcel('EM1','Sheet1',count,0))
            selenium_test.addTests([
            unittest.defaultTestLoader.loadTestsFromTestCase(my_import(MasterProjectUtils.readFromExcel(getApplicationName(),'Sheet1',count,0)+'.'+MasterProjectUtils.readFromExcel(getApplicationName(),'Sheet1',count,0))),
            #unittest.defaultTestLoader.loadTestsFromTestCase(MyGoogleTest.MyGoogleTest),
            ])
            count = count + 1
        
 
            
        outfile = open(direct + htmlDir, "wb")
 
        runner1 = HTMLTestRunner.HTMLTestRunner(
            stream=outfile,
            title='Test Report',
            description=getApplicationName()+'-Selenium Test Execution in nightly build'
        )
        #runner1.STYLESHEET_TMPL = '<link rel="stylesheet" href="my_stylesheet.css" type="text/css">'
        runner1.run(selenium_test)
 
 
 
 
 
if __name__ == '__main__':
    MyTestSuite.test_Issue()
   # unittest.main()
    #print(ApplicationName)