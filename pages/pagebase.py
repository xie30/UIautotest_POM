

class PageBase(object):
    '''
        page基类，所有page都继承这个类
    '''

    def __init__(self, driver, baseurl='www'):
        self.driver = driver
        self.baseurl = baseurl

    def find_element(self, *ele):
        return self.driver.find_element(*ele)

    #输入文本
    def input_text(self, text, loc):
        self.find_element(*loc).send_keys(text)  #这里为什么一定要带个*号---类似于元组的打包
        '''
        args和kwargs不仅可以在函数定义中使用，还可以在函数调用中使用。
        在调用时使用就相当于pack（打包）和unpack（解包），类似于元组的打包和解包。
        解包：
        def test_args_kwargs(arg1, arg2, arg3):
            print("arg1:", arg1)
            print("arg2:", arg2)
            print("arg3:", arg3)
        
            args = ("two", 3, 5)
            test_args_kwargs(*args)
            
            #result:
            arg1: two
            arg2: 3
            arg3: 5
        '''

    def click(self, loc):
        self.find_element(*loc).click()

    def find(self, loc):
        return self.find_element(*loc)

    #鼠标悬浮出现点击
    def mouse_over_click(self):
        pass

    def robot_list(self, r):
        return self.find_element(*r)

    def contract_list(self, l):
        return self.find_element(*l)