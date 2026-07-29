#wrapping data and method into single unit(class) is called encapsulation.
#encapsulation is achieved by using private members.
class student:
    __id=25
    __name="sahil"


    def set_id(self,id):
        self.__id=id

    def get_id(self):
        return self.__id


    def set_name(self,name):
        self.__name=name

    def get_name(self):
        return self.__name

st=student()
st.set_id(256)
print(st.get_id())
print(st.get_name())