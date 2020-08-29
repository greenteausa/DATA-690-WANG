 # 690-01 class Notes
 
 1. Learn some data science application in medical field.
 2. Learn surveymonkey.com is a website to create survey and how to summarize the result via python tool and showed out with stastics graph bar.
 3. notebooks.ai and python.org is two ways to script the .py documents.
 4. Learned how to use github and know the steps details clearly.
 
 # chapter 2 
 1. I should exit() first then run the python hello_wold.py.
 2. when the user want to excute all of the their Python code, we can use python. 
    but for those who want to do data analysis or scientific computing we should use ipython.
 3. There are two way that can check the docstring content(introspection).
   - b?
   - help(b) 
     --if b?? with tow question marks, which will show the function's source code.
 4. Use *(wildcard) could help us check all the names matching the wildcard expression. like *add* command, we could see all the function or expresstion which contains "add".
 5.  The command code: %run any script.py  in the notebook could be identical to run the program on the command line.
 6.  % load script.py  could import a script into a code cell.
 7. I tired paste and cpaster command code which doesn't work.  ???
 8. There are a lot of keyboard shortcut.  Ctrl-U ???  Ctrl-L???
 9. np.dot() means
    -For 1-D arrays, it is the inner product of the vectors.
    -For 2-D vectors, it is the equivalent to matrix multiplication. 
    -For N-D arrays, it is a sum product over the last axis of a and the second-last axis of b.
 10.random.randn(50).cumsum() will display the cumulative sums of the array a.
 11. obj.some_method(x,y,z) almost every object has attached functions, known as methods, that have access to the object's internal contents. 
 12. like result = f(a,b,c,d=5,e='foo'). functions can take both positional and keyword arguments.
 13. isinstance(a, int) or isinstance(a,(int, float)) can help check that a object's type is a particular type or among those present in the tuple.
 14. a list can beed nodified, but a tuple can't been modified.
     >>> l = [4,5,6]
     >>> tuple(l)
      (4, 5, 6)
       we can change the list to tuple through this way.
 15. b = a.replace('string','long string') can change a string through this way.
 16. strings are a sequence of unicode characters and therefore can be treated like other sequences, such as a list or tuples???(need explore more in the future)
 17. the back slash character \ is an escape character, meaning that it is used to specify special character like newlinw \n or Unicode characters. need escape them.
 18.the 'r' stand for raw.
 19.template = '{0:.2f}{1:s}' are worth US${2:d}  
   -{0:.2f} means to format the first argument as a floating-point number with two decimal places.
   - {1:s} means to format the second argument as a string.
   - {2:d} means to format the third argument as an exact interger.
   then sue template.format(4.5560,'Argentine Pesos', 1) can apply the values to the function of template.
 20.bool(0) ## 0  default means False, but i is default mean True. any non 0 value is true. 
    
