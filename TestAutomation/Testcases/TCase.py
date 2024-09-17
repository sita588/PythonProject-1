import Library.CommonModule
import Pages.Login.abc

objA=Library.CommonModule.A()
objA.startBrowserA()

objB=Library.CommonModule.B()
objB.startBrowserB()
print("----------------------")


objC=Pages.Login.abc.C()
objC.testing()
