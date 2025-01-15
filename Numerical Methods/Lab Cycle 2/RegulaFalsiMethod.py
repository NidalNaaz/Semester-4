def getFunction( ) :
    functionInput = input( "Enter the function: " ) 
    return lambda x: eval( functionInput )


def regulaFalsi( function, a, b ) :
    if ( function( a ) * function( b )  >= 0 ) :
        print("Conditions for regula falsi method not met. ")
        return 
    
    c = a 
    while abs(( b - a ) >= 0.01 ) :
        
        c = ( ( a * function( b )) - ( b * function( a )) ) / ( function( b ) - function( a ) )

        if abs( function( c ) < 1e-6 ) :
            break

        if ( function( a ) * function( c )  < 0 ) :
            b = c 

        else :
            a = c 

        
    print("The value of root is : ","%.4f"%c)

functionCheck = getFunction()
value1 = ( int ( input ( "Enter the first limit: " ) ) )
value2 = ( int ( input ( "Enter the second limit: " ) ) )

regulaFalsi( functionCheck, value1 , value2 )
