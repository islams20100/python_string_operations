from ast import excepthandler


def Repeated_Substring(s):
    try:
        compare = ''
        for i in range(len(s)):
            compare+= s[i]
            rep = s.count(compare)
            if rep * len(compare) == len(s):
                return (compare,rep)
    except TypeError:
        print('TypeError occur')
    except SyntaxError:
        print('SyntaxError occur')
    except:
        print('Some Error happen')


def Simple_string_matching(a,b):
    try :
        sub = ''
        pos = a.find('*')
        if len(a)-1 > len(b): # len a  > len b without space
            return False
        
        if pos == -1 : # no asctric
            if a == b: # a == b
                return True
            else:return False
        else:
            if a.replace('*','') == b: # replace * with ''
                return True
            else:
                idx = -1 #iterator in b
                while idx != len(b):
                    idx+=1
                    if a[idx] == b[idx]:
                        continue
                    else:
                        if a[idx] == '*':
                            count = idx
                            while count != len(b):
                                sub+=b[count]
                                if a.replace('*',sub) == b:
                                    return True
                                count+=1
                            return False
                        else:
                            return False
                return False
    except TypeError:
        print('TypeError occur')
    except SyntaxError:
        print('SyntaxError occur')
    except:
        print('Some Error happen')


def is_palindrome(s):
    try :
        s = s.lower()
        reverse_st = s[::-1]
        if s == reverse_st:
            return True
        else:
            return False
    except TypeError:
        print('TypeError occur')
    except SyntaxError:
        print('SyntaxError occur')
    except:
        print('Some Error happen')


def find_nth_occurrence(substring, string, occurrence=1):
    try:
        lst = [i for i in range(len(string)) if string.startswith(substring, i)]
        if occurrence > len(lst):
            return -1
        else: return lst[occurrence-1]
    except TypeError:
        print('TypeError occur')
    except SyntaxError:
        print('SyntaxError occur')
    except:
        print('Some Error happen')