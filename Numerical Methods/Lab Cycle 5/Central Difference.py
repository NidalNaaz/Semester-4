import math

def centralDifference_First ( f, x, h ):
    return (( f( x + h ) - f( x - h )) / ( 2 * h ) )


def centralDifference_Second ( f, x, h ):
    return (( f( x + h ) + f( x - h ) - ( 2 * f( x )) ) /  h ** 2 )


def f ( x ):
    return math.sin( x )

userFunction = input("Enter a function in terms of x (e.g., math.sin(x), x**2, math.exp(x)): ")
f = lambda x: eval(userFunction)

x = eval( input("Enter value of x in the format : ( math.pi/4, 2, 3.5 ): ") )


h = float( input ("Enter the value of 'h' in decimals : ")) 


firstDerivative = centralDifference_First( f, x , h )
secondDerivative = centralDifference_Second( f, x, h )

print( "Approximate values of first and second derivatives (respectively) : " , firstDerivative , ", " , secondDerivative , ".") 
