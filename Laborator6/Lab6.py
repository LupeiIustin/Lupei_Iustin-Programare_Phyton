


# 1.Write a function that extracts the words from a given text as a parameter. A word is defined as a sequence of alpha-numeric characters.
 

test_string = "Geeksforgeeks is best Computer Science Portal"
print ("The original string is : " +  test_string)
res = test_string.split()
print ("The list of words is : " +  str(res))

#2.Write a function that receives as a parameter a regex string, a text string and a whole number x, 
#  and returns those long-length x substrings that match the regular expression.

# 7. Verify using a regular expression whether a string is a valid CNP.

# Option Explicit

#     Function EsteAdresaBuna(oAdresaDeValidat As String) As Boolean
#      'On Error GoTo Catch
#        Dim i As Integer, x As Integer
#        Dim objRegExp As New RegExp
#        Dim blnIsValidEmail As Boolean
#        Dim CNP(13) As Integer
#         objRegExp.IgnoreCase = True
#         objRegExp.Global = True
#         objRegExp.Pattern = "\b[1-8]\d{2}(0[1-9]|1[0-2])(0[1-9]|[12]\d|3[01])(0[1-9]|[1-4]\d|5[0-2]|99)\d{4}\b"
#                              ^[1-9]\d{2}(0[1-9]|1[0-2])(0[1-9]|[12]\d|3[01])(0[1-9]|[1-4]\d|5[0-2]|99)(00[1-9]|0[1-9]\d|[1-9]\d\d)\d$
       
#         blnIsValidEmail = objRegExp.Test(oAdresaDeValidat)